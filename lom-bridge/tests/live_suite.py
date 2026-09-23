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

ping = b.send("/ping")["rows"]; print("== ping :", ping[0])
check("ping : version du bridge = version du script sur le disque", lom.version_warning(ping) is None, lom.version_warning(ping))
check("ping : liste des commandes", any(r[0] == "commands" and "/shape" in r for r in ping), ping)
check("transport arrêté", py("int(song.is_playing)") == "0", "arrêter la lecture avant la suite")
def verified(r):
    return next((x for x in r["rows"] if x and x[0] == "verified"), None)
n0 = int(py("len(song.tracks)"))
py("song.create_midi_track(-1); t=song.tracks[len(song.tracks)-1]; t.name='LOM TEST'; s=t.clip_slots[0]; c=s.create_clip(16.0); t.duplicate_clip_to_arrangement(c, 16.0); t.duplicate_clip_to_arrangement(c, 32.0); s.delete_clip(); result='ok'")
py("song.create_audio_track(-1); t=song.tracks[len(song.tracks)-1]; t.name='LOM TEST AUDIO'; s=t.clip_slots[0]; c=s.create_audio_clip(%r); t.duplicate_clip_to_arrangement(c, 16.0); s.delete_clip(); result='ok'" % wav)
vol = b.send("/param", "LOM TEST", "mixer", "Volume")["rows"][0][0]; pan = b.send("/param", "LOM TEST", "mixer", "Pan")["rows"][0][0]
avol = b.send("/param", "LOM TEST AUDIO", "mixer", "Volume")["rows"][0][0]
check("références opaques", str(vol).startswith("o:") and str(avol).startswith("o:"), (vol, avol))

# 1. saut descendant au début du clip 2
r = shape("LOM TEST", vol, [(16, 1.0), (32, 1.0), (32, 0.0), (48, 0.0)]); check("shape saut", r["ok"], r["errors"])
vr = verified(r); check("relecture exacte après écriture MIDI (écart ≤ tolérance)", vr is not None and vr[4] == "exact" and vr[1] > 0 and vr[2] <= vr[3], vr)
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
vr = verified(r); check("relecture par curseur après écriture audio (5 points, écart ≤ tolérance)", vr is not None and vr[4] == "sampled" and vr[1] == 5 and vr[2] <= vr[3], vr)
v = dict(read("LOM TEST AUDIO", avol, 16, 24, 1)); check("ancienne rampe conservée à 20 (0,55) et 22 (0,7), 0,3 sur 17–18", abs(v[20.0] - 0.55) < 0.01 and abs(v[22.0] - 0.70) < 0.01 and abs(v[17.0] - 0.3) < 0.01, v)
p = dict(read("LOM TEST AUDIO", apan, 16, 24, 2)); check("pan conservé par Live", abs(p[20.0] - 0.0) < 0.02 and abs(p[16.0] + 0.8) < 0.02, p)
# 4b. song.undo() après une écriture audio (relecture par curseur entre la fin de l'étape et un éventuel undo) défait bien l'écriture, pas autre chose
before_undo = read("LOM TEST AUDIO", avol, 16, 24, 1)
r = shape("LOM TEST AUDIO", avol, [(21, 0.1), (22, 0.1)], accept=("fades",)); check("shape audio 3", r["ok"], r["errors"])
v = dict(read("LOM TEST AUDIO", avol, 16, 24, 1)); check("0,1 écrit sur 21–22", abs(v[21.0] - 0.1) < 0.01, v)
py("song.undo(); result='undone'"); time.sleep(0.3)
after_undo = read("LOM TEST AUDIO", avol, 16, 24, 1)
check("song.undo() défait exactement l'écriture du bridge (une étape)", all(abs(x - y) < 0.005 for (_, x), (_, y) in zip(before_undo, after_undo)), (before_undo, after_undo))
# 4c. automation surchargée (valeur modifiée à la main) : refus tant que l'automation n'est pas réactivée
py("t=[x for x in song.tracks if x.name=='LOM TEST AUDIO'][0]; t.mixer_device.volume.value=0.6; result=int(t.mixer_device.volume.automation_state)")
st = py("t=[x for x in song.tracks if x.name=='LOM TEST AUDIO'][0]; result=int(t.mixer_device.volume.automation_state)")
r = b.send("/plan", *lom.shape_args("LOM TEST AUDIO", avol, "raw", 8, "lin", 0, ["fades"], [(17, 0.4), (18, 0.4)]))
check("plan refusé sur automation surchargée (état %s)" % st, st != "2" or any("surchargée" in str(x) for x in r["rows"]), r["rows"][-3:])
py("song.re_enable_automation(); result='ok'"); time.sleep(0.2)
check("automation réactivée", py("t=[x for x in song.tracks if x.name=='LOM TEST AUDIO'][0]; result=int(t.mixer_device.volume.automation_state)") == "1")
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
# 8. commandes typées (0.6.0)
r = m.send("/transport"); check("transport : état", r["ok"] and r["rows"][0][0] == "transport" and r["rows"][0][1] == 0, r)
r = m.send("/transport", "pos", 20.0); check("transport pos 20", r["ok"] and abs(float(r["rows"][0][2]) - 20.0) < 1e-6, r)
r = b.send("/meters", 16.0, 2.0, "LOM TEST AUDIO"); check("meters : 2 s lus, transport rendu arrêté", r["ok"] and r["rows"][0][3] >= 10 and py("int(song.is_playing)") == "0", r)
check("meters : curseur restauré à 20", py("song.current_song_time") == "20.0", py("song.current_song_time"))
mrow = [x for x in r["rows"] if x[0] == "meter" and x[2] == "LOM TEST AUDIO"]; check("meters : crête audible sur la piste de test (ton 220 Hz)", mrow and mrow[0][4] > 0.05, mrow)
r = m.send("/setparam", "LOM TEST", "mixer", "Pan", 25.0); check("setparam pan 25 (disp) relu", r["ok"] and "25" in str(r["rows"][0][6]), r)
r = m.send("/setparam", "LOM TEST AUDIO", "mixer", "Volume", 0.5, "raw"); check("setparam sur volume automatisé refusé sans override", not r["ok"] and "automatisé" in str(r["errors"]), r)
r = m.send("/snapshot", "LOM TEST", "mixer"); sid = r["rows"][0][1]; check("snapshot mixer", r["ok"] and r["rows"][0][2] >= 2, r)
m.send("/setparam", "LOM TEST", "mixer", "Pan", -40.0); r = m.send("/restore", sid); pan_disp = m.send("/param", "LOM TEST", "mixer", "Pan")["rows"][0][5]
check("restore remet le pan à 25", r["ok"] and "25" in str(pan_disp), (r, pan_disp))
r = m.send("/locator", 24.0, "LOM TEST REPÈRE"); check("locator posé à 24", r["ok"] and abs(float(r["rows"][0][2]) - 24.0) < 1e-6, r)
r = m.send("/locator", 24.0, "LOM TEST REPÈRE 2"); check("locator renommé sans suppression", r["ok"] and r["rows"][0][3] == "LOM TEST REPÈRE 2", r)
py("c=[c for c in song.cue_points if abs(c.time-24.0)<1e-6][0]; song.current_song_time=24.0; song.set_or_delete_cue(); song.current_song_time=20.0; result='cue removed'")
r = m.send("/state"); st = json.loads(r["rows"][0][1]); check("state : pistes de test présentes", any(t["name"] == "LOM TEST" for t in st["tracks"]) and st["tracks"][-1]["kind"] == "master", r["errors"])
# 9. codes d'erreur et journal (0.7.0)
r = m.send("/track", "PISTE QUI N EXISTE PAS"); check("code d'erreur stable sur piste introuvable", not r["ok"] and r["codes"] == ["E_NOT_FOUND"], (r["codes"], r["errors"]))
r = m.send("/journal", 3); check("journal : la dernière entrée est une écriture de cette suite", r["ok"] and any(x[0] == "entry" and json.loads(x[1])["cmd"] in ("/shape", "/setparam", "/restore", "/locator", "/transport") for x in r["rows"]), r["rows"][-1:])
check("signature lue dans Live", b.beats_per_bar() in (3, 4, 5, 6, 7), b.beats_per_bar())
# 10. /load et /notes (0.8.0)
n_dev = int(py("t=[x for x in song.tracks if x.name=='LOM TEST AUDIO'][0]; result=len(t.devices)"))
r = m.send("/load", "LOM TEST AUDIO", "Utility", "audio_effects"); check("load Utility (natif) ajouté en fin de chaîne", r["ok"] and r["rows"][0][5] == n_dev + 1 and r["rows"][0][7] == "added", (r["errors"], r["rows"]))
r = m.send("/load", "LOM TEST AUDIO", "Utility", "audio_effects", "replace=Utility"); check("load replace=Utility : même nombre de devices", r["ok"] and r["rows"][0][5] == n_dev + 1 and r["rows"][0][7] == "replaced", (r["errors"], r["rows"]))
r = m.send("/load", "LOM TEST", "Serum 2"); check("load « Serum 2 » ambigu (VST3 + AU) refusé, ou chargé si une seule entrée", (not r["ok"] and r["codes"] == ["E_AMBIGUOUS"]) or r["ok"], (r["codes"], r["errors"]))
r = m.send("/notes", "set", "LOM TEST", 16.0, json.dumps([[60, 0.0, 1.0, 100], [64, 1.0, 1.0, 90], [67, 2.0, 2.0, 80]])); check("notes set : 3 notes écrites et relues", r["ok"] and r["rows"][0][5] == 3, (r["errors"], r["rows"]))
r = m.send("/notes", "set", "LOM TEST", 16.0, json.dumps([[62, 1.0, 0.5, 110]]), 1.0, 2.0); check("notes set fenêtré 1–2 : 3 notes au total", r["ok"] and r["rows"][0][5] == 3, (r["errors"], r["rows"]))
r = m.send("/notes", "get", "LOM TEST", 16.0); check("notes get : 60@0, 62@1, 67@2", r["ok"] and [(x[1], x[2]) for x in r["rows"][1:]] == [(60, 0.0), (62, 1.0), (67, 2.0)], r["rows"])
# 11. commandes de lecture et /clear (couverture P4 : chaque commande a au moins un contrôle ici)
r = m.send("/clips", "LOM TEST"); check("clips : 1 ou 2 clips d'arrangement listés", r["ok"] and 1 <= len(r["rows"]) <= 2 and str(r["rows"][0][0]).startswith("o:"), r)
r = m.send("/params", py("t=[x for x in song.tracks if x.name=='LOM TEST AUDIO'][0]; result=ref(t.devices[0])") if n_dev + 1 else vol, "Gain")
check("params <deviceRef> [filtre] : au moins un paramètre", r["ok"] and len(r["rows"]) >= 1, r)
r = m.send("/solve", vol, -6.0); check("solve −6 dB : valeur brute dans ]0, 1[ et affichage ≈ −6", r["ok"] and 0 < float(r["rows"][0][0]) < 1 and "-6" in str(r["rows"][0][1]), r)
r = m.send("/events", "LOM TEST", vol, 16.0, 48.0); check("events : enveloppes exposées du clip MIDI créé dans cette session", r["ok"] and len(r["rows"]) >= 2, r)
r = m.send("/locators"); check("locators : liste (repère de test retiré)", r["ok"] and not any(x[2].startswith("LOM TEST") for x in r["rows"]), r)
r = m.send("/snapshots"); check("snapshots : le snapshot mixer de la suite est listé", r["ok"] and any(x[0] == sid for x in r["rows"]), r)
before_clear = read("LOM TEST", vol, 16, 32, 1)
r = b.send("/clear", "LOM TEST", vol, 20.0, 24.0, "expressions"); check("clear 20–24 : relu", r["ok"] and r["rows"][0][0] == "cleared" and verified(r) is not None and verified(r)[4] in ("exact", "sampled"), r)
after_clear = dict(read("LOM TEST", vol, 16, 32, 1))
check("clear : hors fenêtre inchangé, dans la fenêtre = droite entre les bords", all(abs(after_clear[t] - v) < 0.005 for t, v in before_clear if t < 20 or t > 24) and abs(after_clear[22.0] - (after_clear[20.0] + after_clear[24.0]) / 2) < 0.01, (before_clear, after_clear))
if not KEEP:
    py("for name in ('LOM TEST','LOM TEST AUDIO'):\n    t=[x for x in song.tracks if x.name==name][0]; song.delete_track(list(song.tracks).index(t))\nresult='cleaned'")
    check("pistes de test supprimées", int(py("len(song.tracks)")) == n0, py("len(song.tracks)"))
print("\n%d échec(s)" % len(FAILS), FAILS)
sys.exit(1 if FAILS else 0)
