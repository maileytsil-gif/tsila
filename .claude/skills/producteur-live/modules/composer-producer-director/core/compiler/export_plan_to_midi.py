#!/usr/bin/env python3
from pathlib import Path
import json,argparse,mido
ap=argparse.ArgumentParser(); ap.add_argument('plan'); ap.add_argument('outdir'); a=ap.parse_args()
plan=json.loads(Path(a.plan).read_text()); out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True); ppq=960
for tr in plan['tracks']:
    mid=mido.MidiFile(ticks_per_beat=ppq); track=mido.MidiTrack(); mid.tracks.append(track)
    ev=[]
    for cl in tr['clips']:
        for n in cl['notes']:
            st=int(round((cl['start_beat']+n['start_beat'])*ppq)); en=st+int(round(n['duration_beats']*ppq))
            ev.append((st,1,n['pitch'],n['velocity'])); ev.append((en,0,n['pitch'],0))
    ev.sort(key=lambda x:(x[0],x[1]))
    last=0
    for tick,on,pitch,vel in ev:
        track.append(mido.Message('note_on' if on else 'note_off',note=pitch,velocity=vel,time=tick-last)); last=tick
    fn=''.join(c if c.isalnum() or c in '-_' else '_' for c in tr['track_name'])+'.mid'; mid.save(out/fn)
print(len(plan['tracks']))
