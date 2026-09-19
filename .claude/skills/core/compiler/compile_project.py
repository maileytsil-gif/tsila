#!/usr/bin/env python3
"""Compile v18 musical specs into an AbletonClipPlan and conceptual BridgeActionBatch.
This does not execute Live. Capability discovery/readback remains the bridge's responsibility.
"""
from __future__ import annotations
from pathlib import Path
import json, argparse, hashlib

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def event_abs_beat(e, beats_per_bar): return (e['bar']-1)*beats_per_bar + e['beat'] + e.get('micro_offset_beats',0.0)
def note(pitch,start,dur,vel): return {'pitch':int(pitch),'start_beat':round(float(start),6),'duration_beats':round(float(dur),6),'velocity':int(vel)}

def compile_plan(project_id, groove, bass=None, harmony=None, sound=None, automation=None):
    beats_per_bar=groove['meter']['numerator']*(4/groove['meter']['denominator'])
    total=groove['bars']*beats_per_bar
    tracks=[]
    for role in groove['roles']:
        notes=[note(role['midi_note'], event_abs_beat(e,beats_per_bar), e['duration_beats'], e['velocity']) for e in role['events']]
        tracks.append({'track_name':role['track_name'],'kind':'midi','clips':[{'clip_name':project_id+'_'+role['role_id'],'start_beat':0,'length_beats':total,'notes':notes}]})
    if bass:
        notes=[note(e['midi_note'], (e['bar']-1)*beats_per_bar+e['beat'], e['duration_beats'], e['velocity']) for e in bass['events'] if e['function']!='REST_INTENT']
        tracks.append({'track_name':bass['track_name'],'kind':'midi','clips':[{'clip_name':project_id+'_BASS','start_beat':0,'length_beats':total,'notes':notes}]})
    if harmony:
        notes=[]
        for e in harmony['events']:
            s=(e['bar']-1)*beats_per_bar+e['beat']
            for pitch in e['midi_notes']: notes.append(note(pitch,s,e['duration_beats'],e['velocity']))
        tracks.append({'track_name':harmony['track_name'],'kind':'midi','clips':[{'clip_name':project_id+'_HARMONY','start_beat':0,'length_beats':total,'notes':notes}]})
    return {'schema_version':'18.0','project_id':project_id,'bpm':groove['bpm'],'meter':groove['meter'],'tracks':tracks,'sound_bindings':[{'track_name':e['track_name'],'engine':e['engine'],'macros':e.get('macros',{})} for e in (sound or {'elements':[]})['elements']],'automation_lanes':(automation or {'lanes':[]})['lanes']}

def compile_actions(plan):
    acts=[]; seq=1
    def add(cap,target,op,payload,depends=None,risk='low',post=None,rollback=None):
        nonlocal seq
        rid=f"req-{seq:04d}"; seq+=1
        acts.append({'request_id':rid,'depends_on':depends or [],'requires_capability':cap,'target':target,'operation':{'type':op,'payload':payload},'postconditions':post or [],'rollback':rollback or {},'risk':risk})
        return rid
    for tr in plan['tracks']:
        t={'kind':'track','track_signature':tr['track_name'],'clip_signature':None,'device_signature':None,'parameter_signature':None}
        tid=add('ensure_track',t,'ensure_track',{'kind':tr['kind']},post=['track_resolved_or_created'])
        for cl in tr['clips']:
            ct={'kind':'clip','track_signature':tr['track_name'],'clip_signature':cl['clip_name'],'device_signature':None,'parameter_signature':None}
            cid=add('create_clip',ct,'create_clip',{'start_beat':cl['start_beat'],'length_beats':cl['length_beats']},[tid],post=['clip_exists_with_length'],rollback={'type':'restore_snapshot'})
            add('write_notes',ct,'replace_notes',{'notes':cl['notes']},[cid],risk='medium',post=['roundtrip_notes_equal'],rollback={'type':'restore_snapshot'})
    for bind in plan.get('sound_bindings',[]):
        target={'kind':'device','track_signature':bind['track_name'],'clip_signature':None,'device_signature':bind['engine'],'parameter_signature':None}
        add('read_tracks_devices',target,'inspect',{'purpose':'resolve_sound_binding','macros':bind.get('macros',{})},risk='low',post=['device_or_manual_binding_resolved'])
    for lane in plan.get('automation_lanes',[]):
        target={'kind':'device_parameter','track_signature':lane['track_name'],'clip_signature':None,'device_signature':'resolve-current-device-or-rack','parameter_signature':lane['target_macro']}
        op='write_persistent_automation' if lane['persistence']=='persistent_if_supported' else ('start_realtime_control' if lane['persistence']=='realtime' else 'set_value')
        cap='automation_persistent' if op=='write_persistent_automation' else ('realtime_remote' if op=='start_realtime_control' else 'write_parameter')
        add(cap,target,op,dict(lane),risk='medium',post=['readback_or_envelope_verify'],rollback={'type':'restore_snapshot'})
    return {'schema_version':'18.0','project_id':plan['project_id'],'session_policy':'discover-current-session','actions':acts}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--project-id',required=True); ap.add_argument('--groove',required=True); ap.add_argument('--bass'); ap.add_argument('--harmony'); ap.add_argument('--sound'); ap.add_argument('--automation'); ap.add_argument('--out-dir',required=True)
    a=ap.parse_args(); groove=load(a.groove); bass=load(a.bass) if a.bass else None; harmony=load(a.harmony) if a.harmony else None; sound=load(a.sound) if a.sound else None; auto=load(a.automation) if a.automation else None
    plan=compile_plan(a.project_id,groove,bass,harmony,sound,auto); actions=compile_actions(plan)
    od=Path(a.out_dir); od.mkdir(parents=True,exist_ok=True)
    (od/'ableton-clip-plan.json').write_text(json.dumps(plan,indent=2,ensure_ascii=False)+'\n')
    (od/'bridge-action-batch.json').write_text(json.dumps(actions,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'tracks':len(plan['tracks']),'actions':len(actions)},indent=2))
if __name__=='__main__': main()
