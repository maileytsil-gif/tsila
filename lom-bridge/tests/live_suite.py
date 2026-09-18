#!/usr/bin/env python3
"""Suite d'essais DANS Live (Set jetable ou copie) : python3 tests/live_suite.py [--keep]
Crée une piste MIDI « LOM TEST » (2 clips 16–32, 32–48) et une piste audio « LOM TEST AUDIO » (clip 16–24 depuis un WAV généré),
rejoue les scénarios, vérifie par lecture réelle, puis supprime les pistes (sauf --keep). Ne touche à aucune autre piste."""
import sys, os, time, json, wave, struct, math, threading, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lom
KEEP = "--keep" in sys.argv
b = lom.Bridge(timeout=240); m = lom.Bridge(timeout=20)
FAILS = []
def check(label, cond, detail=""):
    print(("OK   " if cond else "FAIL ") + label + ("" if cond else "  -> " + str(detail)))
    if not cond: FAILS.append(label)
def py(code):
    r = m.send("/py", code)
    if not r["ok"]: raise RuntimeError(r["errors"])
    return r["rows"][0][0]
def read(track, ref, tA, tB, res=1):
    r = b.send("/read", track, ref, tA, tB, res)
    if not r["ok"]: raise RuntimeError(r["errors"])
    return [(x[0], round(float(x[1]), 4)) for x in r["rows"]]
def shape(track, ref, pts, unit="raw", res=8, curve="lin", hold=0, accept=("expressions",)):
    return b.send("/shape", *lom.shape_args(track, ref, unit, res, curve, hold, list(accept), pts))

wav = os.path.join(tempfile.gettempdir(), "lom_suite_tone.wav")
with wave.open(wav, "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100)
    w.writeframes(b"".join(struct.pack("<h", int(6000 * math.sin(2 * math.pi * 220 * i / 44100))) for i in range(44100 * 4)))

print("== ping :", b.send("/ping")["rows"])
check("transport arrêté", py("int(song.is_playing)") == "0", "arrêter la lecture avant la suite")
n0 = int(py("len(song.tracks)"))
py("song.create_midi_track(-1); t=song.tracks[len(song.tracks)-1]; t.name='LOM TEST'; s=t.clip_slots[0]; c=s.create_clip(16.0); t.duplicate_clip_to_arrangement(c, 16.0); t.duplicate_clip_to_arrangement(c, 32.0); s.delete_clip(); result='ok'")
py("song.create_audio_track(-1); t=song.tracks[len(song.tracks)-1]; t.name='LOM TEST AUDIO'; s=t.clip_slots[0]; c=s.create_audio_clip(%r); t.duplicate_clip_to_arrangement(c, 16.0); s.delete_clip(); result='ok'" % wav)
vol = b.send("/param", "LOM TEST", "mixer", "Volume")["rows"][0][0]; pan = b.send("/param", "LOM TEST", "mixer", "Pan")["rows"][0][0]
avol = b.send("/param", "LOM TEST AUDIO", "mixer", "Volume")["rows"][0][0]
check("références opaques", str(vol).startswith("o:") and str(avol).startswith("o:"), (vol, avol))

# 1. saut descendant au début du clip 2
r = shape("LOM TEST", vol, [(16, 1.0), (32, 1.0), (32, 0.0), (48, 0.0)]); check("shape saut", r["ok"], r["errors"])
v = read("LOM TEST", vol, 31.5, 32.5, 4); check("saut au bord : 1,0 avant, 0,0 dès 32", v[1][1] > 0.95 and v[2][1] < 0.05, v)
# 2. voisinage strictement identique
shape("LOM TEST", vol, [(16, 0.0), (32, 1.0)]); before = read("LOM TEST", vol, 16, 32, 16)
r = shape("LOM TEST", vol, [(20, 0.5), (24, 0.5)]); after = read("LOM TEST", vol, 16, 32, 16)
bad = [(t, x, y) for (t, x), (_, y) in zip(before, after) if not (20 <= t <= 24) and abs(x - y) > 0.002]
check("192 points hors fenêtre inchangés", before and not bad, bad[:3])
check("bord gauche exact (19.9375 sur la droite, 20 = 0,5)", abs(dict(after)[19.9375] - 0.2461) < 0.003 and abs(dict(after)[20.0] - 0.5) < 0.002, [x for x in after if 19.9 < x[0] < 20.1])
# 3. validations /read et /plan
for args, key in (((16, 20, -1), "res"), ((20, 16, 1), "plage"), ((-4, 16, 1), "plage"), ((16, 20, 0), "res")):
    r = b.send("/read", "LOM TEST", vol, *args); check("read invalide refusé %s" % (args,), not r["ok"] and key in str(r["errors"]), r["errors"])
r = b.send("/plan", *lom.shape_args("LOM TEST", vol, "raw", 8, "lin", 0, [], [(20, 0.5)])); check("fenêtre nulle refusée", any("durée nulle" in str(x) for x in r["rows"]), r["rows"][-2:])
r = b.send("/plan", *lom.shape_args("LOM TEST AUDIO", avol, "raw", 8, "lin", 0, [], [(16, 0.2), (20, 0.4)])); check("audio sans accept=fades refusé", any("fondus" in str(x) for x in r["rows"]), r["rows"][-2:])
r = b.send("/plan", *lom.shape_args("LOM TEST", vol, "disp", 8, "lin", 0, ["expressions"], [(16, -6), (20, 40)])); check("saturation refusée sans accept=clamp", any("saturée" in str(x) for x in r["rows"]), r["rows"][-2:])
r = b.send("/plan", *lom.shape_args("LOM TEST", vol, "disp", 8, "lin", 0, ["expressions", "clamp"], [(16, -6), (20, 40)]))
plan = json.loads([x for x in r["rows"] if x[0] == "plan"][0][1]); check("saturation acceptée et signalée", plan["errors"] == [] and plan["points"][1]["clamped"] == 1, plan["warnings"])
# 4. audio : fusion avec l'automation existante (échantillonnage), autre paramètre conservé
r = shape("LOM TEST AUDIO", avol, [(16, 0.85), (20, 0.55), (24, 0.85)], accept=("fades",)); check("shape audio 1", r["ok"], r["errors"])
apan = b.send("/param", "LOM TEST AUDIO", "mixer", "Pan")["rows"][0][0]
r = shape("LOM TEST AUDIO", apan, [(16, -0.8), (24, 0.8)], accept=("fades",)); check("shape audio pan", r["ok"], r["errors"])
t0 = time.time(); r = shape("LOM TEST AUDIO", avol, [(17, 0.3), (18, 0.3)], accept=("fades",)); dt = time.time() - t0
check("shape audio 2 (échantillonnage %.1fs)" % dt, r["ok"], r["errors"])
v = dict(read("LOM TEST AUDIO", avol, 16, 24, 1)); check("ancienne rampe conservée à 20 (0,55) et 22 (0,7), 0,3 sur 17–18", abs(v[20.0] - 0.55) < 0.01 and abs(v[22.0] - 0.70) < 0.01 and abs(v[17.0] - 0.3) < 0.01, v)
p = dict(read("LOM TEST AUDIO", apan, 16, 24, 2)); check("pan conservé par Live", abs(p[20.0] - 0.0) < 0.02 and abs(p[16.0] + 0.8) < 0.02, p)
# 5. annulation par id d'une tâche en file, et d'une tâche en cours
b2 = lom.Bridge(timeout=0.5); r1 = b2.send("/read", "LOM TEST", vol, 16, 48, 4)   # expire côté client, continue côté serveur
jobs = m.send("/jobs")["rows"]; check("tâche en cours visible", any(j[1] == "/read" for j in jobs), jobs)
rid = [j[0] for j in jobs if j[1] == "/read"][0]; r = m.send("/cancel", rid); check("annulation par id acceptée", r["ok"] and r["rows"][0][1] >= 1, r)
time.sleep(0.5); check("file vide après annulation", m.send("/jobs")["rows"] == [], m.send("/jobs")["rows"])
# 6. curseur restauré après lecture
py("song.current_song_time=7.0"); time.sleep(0.3); read("LOM TEST", vol, 16, 20, 1); time.sleep(0.3)
check("curseur restauré", py("song.current_song_time") == "7.0", py("song.current_song_time"))
# 7. clip supprimé entre plan et exécution
r = b.send("/plan", *lom.shape_args("LOM TEST", vol, "raw", 8, "lin", 0, ["expressions"], [(40, 0.2), (44, 0.4)])); check("plan valide", any(x[0] == "ok" for x in r["rows"]), r["rows"][-1:])
# (la revalidation se fait au démarrage de la tâche : on supprime le clip juste après l'envoi, avant le tick suivant)
sock_cmd = threading.Thread(target=lambda: py("t=[x for x in song.tracks if x.name=='LOM TEST'][0]; c=[c for c in t.arrangement_clips if c.start_time==32.0][0]; t.delete_clip(c); result='deleted'"))
sock_cmd.start(); r = shape("LOM TEST", vol, [(40, 0.2), (44, 0.4)]); sock_cmd.join()
check("revalidation : clip disparu -> refus ou succès cohérent", (not r["ok"] and "disparu" in str(r["errors"])) or r["ok"], r)
if not KEEP:
    py("for name in ('LOM TEST','LOM TEST AUDIO'):\n    t=[x for x in song.tracks if x.name==name][0]; song.delete_track(list(song.tracks).index(t))\nresult='cleaned'")
    check("pistes de test supprimées", int(py("len(song.tracks)")) == n0, py("len(song.tracks)"))
print("\n%d échec(s)" % len(FAILS), FAILS)
sys.exit(1 if FAILS else 0)
