# -*- coding: utf-8 -*-
"""Faux Live sur UDP réel, pour tester la chaîne complète hors Ableton : Remote Script LOMBridge (vrai code) sur les faux
objets de test_offline.py, écoute UDP 7421, fichier de connexion écrit au chemin habituel. Ensuite, dans d'autres terminaux :
    python3 lom.py serve --port 7480          # vrai serveur HTTP
    python3 agent_gateway.py inspect /ping    # vrai client agent
Ce n'est pas Live : rien ici ne prouve un rendu audio ni le comportement réel de l'API Live. Ctrl+C pour arrêter.
Set simulé : « AUDIO - Sub » (clip audio tone 5|1-9|1, n'expose pas ses enveloppes → échantillonnage) et « 3-MIDI » (clips A 5|1-9|1, B 9|1-13|1)."""
import os, sys, tempfile, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_offline import FakeClip, FakeTrack, FakeSong, FollowParam, load_bridge

def main():
    tmp = tempfile.mkdtemp(prefix="lombridge-fake-live-")
    midi = FakeTrack("3-MIDI", [FakeClip("A", 16.0, 32.0), FakeClip("B", 32.0, 48.0)])
    audio = FakeTrack("AUDIO - Sub", [FakeClip("tone", 16.0, 32.0, audio=True)], midi=False, expose=False)
    song = FakeSong([midi, audio])
    # piste audio réelle : le paramètre suit l'automation au curseur (état 1), l'enveloppe reste cachée → échantillonnage + relecture par curseur
    vol = FollowParam("Track Volume", automation_state=1); vol.song, vol.track = song, audio; audio.mixer_device.volume = vol
    mod, b = load_bridge(song, tmp)
    # load_bridge remplace la socket par un faux et le fichier de connexion par un chemin de test : on remet les vrais
    import socket, json
    mod.CONN_FILE = os.environ.get("LOM_BRIDGE_CONN") or os.path.join(os.path.expanduser("~"), "Library", "Application Support", "LOMBridge", "connection.json")
    b._tok = None; b._token()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", mod.RX_PORT)); s.setblocking(False); b._sock = s
    print("faux Live prêt : UDP 127.0.0.1:%d, session %s, connexion %s" % (mod.RX_PORT, b._session(), mod.CONN_FILE), flush=True)
    try:
        while True:
            b.update_display(); time.sleep(0.01)
    except KeyboardInterrupt: pass
    finally:
        s.close()
        print("faux Live arrêté ; clips AUDIO - Sub :", [(c.name, c.start_time, c.end_time) for c in audio.arrangement_clips], flush=True)

if __name__ == "__main__": main()
