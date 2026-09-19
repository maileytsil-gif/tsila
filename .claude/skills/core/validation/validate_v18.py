#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
from jsonschema import Draft202012Validator
import mido
ROOT=Path(__file__).resolve().parents[2]
SC=ROOT/'core/schemas'
checks=[]
def ok(name,passed,detail=''): checks.append({'check':name,'passed':bool(passed),'detail':detail})
def validate(instance_path,schema_name):
    obj=json.loads(Path(instance_path).read_text()); schema=json.loads((SC/schema_name).read_text()); errs=list(Draft202012Validator(schema).iter_errors(obj)); ok(f'schema:{Path(instance_path).name}',not errs,'; '.join(e.message for e in errs[:3])); return obj
# current examples
for ex in sorted((ROOT/'core/examples').glob('*')):
    if not ex.is_dir(): continue
    mapping=[('production-brief.json','production-brief.schema.json'),('cultural-style-lock.json','cultural-style-lock.schema.json'),('groove-spec.json','groove-spec.schema.json'),('bass-interlock-spec.json','bass-interlock-spec.schema.json'),('harmony-spec.json','harmony-spec.schema.json'),('sound-spec.json','sound-spec.schema.json'),('automation-spec.json','automation-spec.schema.json'),('ableton-clip-plan.json','ableton-clip-plan.schema.json'),('bridge-action-batch.json','bridge-action-batch.schema.json')]
    for f,s in mapping:
        p=ex/f
        if p.exists(): validate(p,s)
# provenance
reg=json.loads((ROOT/'core/provenance/source-registry.json').read_text()); ids={x['id'] for x in reg['sources']}
pat=json.loads((ROOT/'data/patterns/patterns-v18.json').read_text())
for p in pat['patterns']:
    ev=p['evidence']; missing=[x for x in ev['source_ids'] if x not in ids]
    ok('pattern-provenance:'+p['pattern_id'],not missing,'missing='+','.join(missing))
    if ev['level'] in ('DOC','ATTRIB'): ok('documented-has-source:'+p['pattern_id'],bool(ev['source_ids']))

# Semantic invariants for examples
known_caps={'read_tracks_devices','ensure_track','create_clip','write_notes','write_parameter','serum_exposed_parameters','rack_macros','realtime_remote','automation_persistent','transport_observer','rollback'}
hybrid=json.loads((ROOT/'data/hybridization/hybridization-matrix.json').read_text())
for ex in sorted((ROOT/'core/examples').glob('*')):
    if not ex.is_dir(): continue
    gp=ex/'groove-spec.json'; bp=ex/'bass-interlock-spec.json'; hp=ex/'harmony-spec.json'; ap=ex/'automation-spec.json'; pb=ex/'production-brief.json'; ba=ex/'bridge-action-batch.json'
    if gp.exists():
        g=json.loads(gp.read_text()); bpb=g['meter']['numerator']*(4/g['meter']['denominator']); total=g['bars']*bpb; sem=[]
        for r in g['roles']:
            for e in r['events']:
                if e['bar']>g['bars'] or e['beat']>=bpb or e['beat']<0: sem.append((r['role_id'],e))
                ab=(e['bar']-1)*bpb+e['beat']+e.get('micro_offset_beats',0)
                if ab<0 or ab+e['duration_beats']>total+0.25: sem.append((r['role_id'],'out_of_clip',e))
        ok('groove-event-bounds:'+ex.name,not sem,str(sem[:3]))
        for specname in ['bass-interlock-spec.json','harmony-spec.json']:
            sp=ex/specname
            if sp.exists():
                obj=json.loads(sp.read_text()); bad=[]
                for e in obj['events']:
                    if e['bar']>g['bars'] or e['beat']>=bpb or e['beat']<0: bad.append(e)
                ok('event-bounds:'+ex.name+':'+specname,not bad,str(bad[:3]))
        if ap.exists():
            a=json.loads(ap.read_text()); bad=[x for x in a['lanes'] if x['end_beat']<=x['start_beat'] or x['end_beat']>total+0.001]
            ok('automation-bounds:'+ex.name,not bad,str(bad[:3]))
    if pb.exists():
        brief=json.loads(pb.read_text()); cult=brief.get('cultural',{}); primary=cult.get('primary_axis'); secondary=cult.get('secondary_axis'); status='OK'
        if primary and secondary:
            matches=[r for r in hybrid['rules'] if r['foundation']==primary and r['borrowed']==secondary]
            status=matches[0]['status'] if matches else 'UNMAPPED'
        ok('hybridization-not-rejected:'+ex.name,status!='REJECT','status='+status)
        ok('no-authenticity-claim:'+ex.name,not cult.get('authenticity_claim',False))
    if ba.exists():
        batch=json.loads(ba.read_text()); ids=[a['request_id'] for a in batch['actions']]
        ok('unique-action-ids:'+ex.name,len(ids)==len(set(ids)))
        unknown=sorted(set(a['requires_capability'] for a in batch['actions'])-known_caps)
        ok('known-capabilities:'+ex.name,not unknown,','.join(unknown))
        pos={x:i for i,x in enumerate(ids)}; backward=[]
        for a in batch['actions']:
            for d in a['depends_on']:
                if pos.get(d,10**9)>=pos[a['request_id']]: backward.append((a['request_id'],d))
        ok('dependency-order:'+ex.name,not backward,str(backward[:3]))

# MIDI parse
mids=list(ROOT.rglob('*.mid'))
bad=[]
for p in mids:
    try:
        mf=mido.MidiFile(p); notes=sum(1 for t in mf.tracks for msg in t if msg.type=='note_on' and msg.velocity>0)
        if notes<1: bad.append(str(p.relative_to(ROOT))+':no-notes')
    except Exception as e: bad.append(str(p.relative_to(ROOT))+':'+str(e))
ok('midi-semantic-parse',not bad,f'{len(mids)} midi files; '+('; '.join(bad[:5]) if bad else 'all parse and contain notes'))
# Root historical hygiene
old=list(ROOT.glob('VALIDATION-v*.json'))+[x for x in ROOT.glob('CHANGELOG-v*.md') if x.name!='CHANGELOG-v18.md']
ok('root-history-clean',not old,'old-root-files='+','.join(x.name for x in old))
# Action dependencies resolve
for ex in sorted((ROOT/'core/examples').glob('*')):
    p=ex/'bridge-action-batch.json'
    if p.exists():
        batch=json.loads(p.read_text()); action_ids={a['request_id'] for a in batch['actions']}; missing=[]
        for a in batch['actions']:
            for d in a['depends_on']:
                if d not in action_ids: missing.append((a['request_id'],d))
        ok('action-deps:'+ex.name,not missing,str(missing))
passed=all(x['passed'] for x in checks)
report={'schema_version':'18.0','passed':passed,'checks':checks}
(ROOT/'VALIDATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':passed,'checks':len(checks),'failed':[x for x in checks if not x['passed']]},indent=2))
sys.exit(0 if passed else 1)
