#!/usr/bin/env python3
"""Small helper for exact MIDI transposition. Uses MIDI note numbers as canonical IDs."""
import argparse
PCS={'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}
NAMES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def transpose(notes, semitones):
    out=[]
    for x in notes:
        n=x+semitones
        if not 0<=n<=127: raise ValueError(f'out of MIDI range: {n}')
        pc=NAMES[n%12]; octv=n//12-1
        out.append((n,f'{pc}{octv}'))
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('semitones',type=int); ap.add_argument('notes',nargs='+',type=int)
    a=ap.parse_args(); print(transpose(a.notes,a.semitones))
