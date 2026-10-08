#!/usr/bin/env python3
"""Génère un WAV stéréo silencieux pour servir de support d'automation.
Usage: make_silence.py [mesures=12] [bpm=120] [dossier=/Volumes/Seagate Portable Drive/abl proj/1 Project/Samples/Imported]"""
import sys, wave, os
mes = int(sys.argv[1]) if len(sys.argv) > 1 else 12
bpm = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
d = sys.argv[3] if len(sys.argv) > 3 else os.path.expanduser('/Volumes/Seagate Portable Drive/abl proj/1 Project/Samples/Imported')
os.makedirs(d, exist_ok=True)
sr = 44100; sec = mes * 4 * 60.0 / bpm
p = os.path.join(d, 'silence %d mesures %gbpm.wav' % (mes, bpm))
w = wave.open(p, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
w.writeframes(b'\x00\x00\x00\x00' * int(sec * sr)); w.close()
print(p, round(sec, 3), 's')
