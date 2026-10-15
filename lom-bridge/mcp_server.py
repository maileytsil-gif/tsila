#!/usr/bin/env python3
"""mcp_server.py — connecteur MCP (stdio) du LOM Bridge : donne à Claude (Claude Desktop, Claude Code, tout client MCP)
la lecture du Set Ableton Live, puis, si on l'autorise, l'écriture par les mêmes commandes que `lom.py`.

    pip install "mcp>=2"
    python3 mcp_server.py            # lecture seule : le Set n'est jamais modifié
    python3 mcp_server.py --write    # ou LOM_MCP_WRITE=1 : ajoute les outils d'écriture

Parle au Remote Script par UDP (comme `lom.py`) ; `lom.py serve` n'est pas nécessaire. Le jeton vient de `connection.json`
(`LOM_BRIDGE_CONN` pour un autre chemin) et n'apparaît dans aucune réponse. Jamais exposés : `/py`, `/set`, `/call`, `/reload`.
Les écritures d'automation passent par `live_automation_preview` puis `live_automation_commit` (mêmes empreintes que
`agent_gateway.py` : la moindre différence de spec ou de Set refuse l'écriture). Rien ici ne prouve un rendu audio :
un agent n'écoute pas le Set.

Configuration d'un client MCP (exemple Claude Desktop / Claude Code, chemin absolu) :
    {"mcpServers": {"lom-bridge": {"command": "python3", "args": ["/chemin/vers/lom-bridge/mcp_server.py"]}}}
"""
import argparse
import json
import os
import sys
import threading
from contextlib import contextmanager
from typing import Any, Literal, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lom                      # noqa: E402
import agent_gateway as gw      # noqa: E402

try:
    from pydantic import BaseModel, Field
    from mcp.server.mcpserver import MCPServer
    from mcp.server.mcpserver.exceptions import ToolError
    from mcp.types import ToolAnnotations
except ImportError as exc:      # pragma: no cover
    raise SystemExit('dépendance absente (%s) : pip install "mcp>=2"' % exc)

CONNECTOR_VERSION = "0.1.0"
READ_TIMEOUT, WRITE_TIMEOUT, COMMIT_TIMEOUT = 60.0, 240.0, 600.0
INSTRUCTIONS = """Pilote le Set Ableton Live ouvert par le LOM Bridge (C3 = 60).
Début de séance : live_ping (version, mode d'écriture), puis live_state ; relire l'état réel avant d'agir, l'utilisateur corrige dans Live entre deux étapes.
Une étape par échange : annoncer le plan, exécuter ou faire valider une seule étape, relire après.
Les outils d'écriture n'existent que si le connecteur a été lancé avec --write ; avant d'écrire, le Set doit être sauvé sous un nouveau nom.
Automation : live_automation_preview, lire le plan, puis live_automation_commit avec les deux empreintes reçues.
Jamais « entendu » : tu n'écoutes ni le Set ni un rendu ; distingue réglé, relu, mesuré (live_meters, relatif seulement) et proposé.
Un nouvel effet natif de Live n'entre pas dans les chaînes de mix ; les traitements passent par des plug-ins tiers."""

_write_lock = threading.Lock()


class Note(BaseModel):
    pitch: int = Field(ge=0, le=127, description="Numéro MIDI, C3 = 60")
    start: float = Field(ge=0, description="Début en temps (noires), relatif au début du clip")
    duration: float = Field(gt=0, description="Durée en temps (noires)")
    velocity: int = Field(default=100, ge=1, le=127)
    mute: bool = False


# ---------- accès au bridge ----------
@contextmanager
def bridge(timeout):
    """Un Bridge (une socket UDP) par appel : le fichier de connexion est relu, donc un Live relancé est suivi sans redémarrer ce serveur."""
    try:
        b = lom.Bridge(timeout=timeout, conn=lom.read_connection(os.environ.get("LOM_BRIDGE_CONN") or lom.CONN_FILE))
    except (RuntimeError, OSError, ValueError) as exc:
        raise ToolError(str(exc))
    try: yield b
    finally: b.sock.close()


def fail(r):
    """Réponse en échec du bridge -> ToolError qui garde les codes E_… (E_STALE : replanifier, E_ROLLED_BACK : rien n'est modifié…)."""
    codes = list(r.get("codes", [])) + ["E_ERROR"] * len(r["errors"])
    lines = ["[%s] %s" % (c, e) for c, e in zip(codes, r["errors"])]
    if r["rows"]: lines.append("lignes reçues : " + json.dumps(r["rows"], ensure_ascii=False)[:1500])
    return ToolError("\n".join(lines) or "échec sans détail")


def run(command, args=(), timeout=READ_TIMEOUT, write=False, times=False):
    """Envoie une commande ; renvoie les lignes du bridge, ou lève ToolError. `times` : « mesure|temps » devient un temps absolu."""
    def go():
        with bridge(timeout) as b:
            a = lom.http_args(list(args), b.beats_per_bar) if times else list(args)
            r = b.send(command, *a)
            return r, (lom.version_warning(r["rows"]) if command == "/ping" else None)
    if write:
        with _write_lock: r, warning = go()
    else: r, warning = go()
    if not r["ok"]: raise fail(r)
    return r["rows"], warning


def apply_runner(spec, timeout):
    """`run(dry)` attendu par gw.preview_spec / gw.commit_spec : même forme que la réponse de POST /apply du serveur HTTP."""
    def go(dry):
        logs = []
        try:
            with bridge(timeout) as b: results = lom.apply_spec(b, spec, dry, logs.append)
        except (ValueError, RuntimeError) as exc: raise ToolError(str(exc))
        return {"log": logs, "results": results}
    return go


def parse_json_row(rows, key):
    row = next((r for r in rows if r and r[0] == key), None)
    if row is None or len(row) < 2: return None
    try: return json.loads(row[1])
    except (TypeError, ValueError): return None


# ---------- serveur ----------
READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False, open_world_hint=False)
WRITES = ToolAnnotations(read_only_hint=False, destructive_hint=False, open_world_hint=False)
WRITES_REPLACING = ToolAnnotations(read_only_hint=False, destructive_hint=True, open_world_hint=False)


def build_server(write=False):
    mcp = MCPServer("lom-bridge", title="LOM Bridge (Ableton Live)", description="Lecture et écriture du Set Ableton Live par le LOM Bridge",
                    instructions=INSTRUCTIONS, version=CONNECTOR_VERSION)

    # ----- lecture -----
    @mcp.tool(name="live_ping", annotations=READ_ONLY)
    def live_ping() -> dict[str, Any]:
        """Teste la liaison avec Live : version du bridge et de Live, session, commandes, limites. Dit si les outils d'écriture sont actifs (`write_enabled`)."""
        rows, warning = run("/ping")
        return {"rows": rows, "warnings": [warning] if warning else [], "write_enabled": write, "connector_version": CONNECTOR_VERSION}

    @mcp.tool(name="live_state", annotations=READ_ONLY)
    def live_state() -> dict[str, Any]:
        """Carte du Set en JSON : tempo, signature, transport, boucle, pistes (type, mute/solo, volume, pan, envois, devices, clips d'arrangement), repères. À lire en début de séance et avant toute écriture."""
        rows, _ = run("/state")
        state = parse_json_row(rows, "state")
        if state is None: raise ToolError("réponse /state illisible : " + json.dumps(rows, ensure_ascii=False)[:500])
        return {"state": state}

    @mcp.tool(name="live_read", annotations=READ_ONLY)
    def live_read(command: str, args: Optional[list[str | int | float]] = None) -> dict[str, Any]:
        """Commande du bridge en lecture seule. command : /track /param /params /solve /clips /plan /read /events /jobs /children /get /info /path /snapshots /locators /journal /ping /state,
        /transport sans argument, /notes get <piste> <clipRef|t> [tA tB]. Exemples : ("/param", ["AUDIO - Sub", "mixer", "Volume"]), ("/clips", ["AUDIO - Sub"]),
        ("/notes", ["get", "PAD", "17|1"]). Temps : nombre de temps depuis 1|1 ou « mesure|temps » (17|3.5). Les références d'objets `o:<session>:<n>` viennent du bridge, jamais inventées."""
        command, args = command if command.startswith("/") else "/" + command, args or []
        if not gw.read_only(command, args): raise ToolError("commande hors liste blanche lecture seule : %s" % command)
        rows, _ = run(command, args, times=True)
        return {"rows": rows}

    @mcp.tool(name="live_journal", annotations=READ_ONLY)
    def live_journal(n: int = 10) -> dict[str, Any]:
        """Dernières écritures journalisées par le bridge (heure, commande, arguments, résultat ou code d'erreur), la plus ancienne d'abord."""
        rows, _ = run("/journal", [max(1, min(int(n), 100))])
        entries = [json.loads(r[1]) for r in rows if r and r[0] == "entry" and len(r) > 1]
        return {"entries": entries, "file": next((r[1] for r in rows if r and r[0] == "journal"), None)}

    @mcp.tool(name="live_automation_preview", annotations=READ_ONLY)
    def live_automation_preview(spec: dict[str, Any]) -> dict[str, Any]:
        """Plan serveur d'une spec d'automation d'arrangement, SANS rien écrire. spec : {"beatsPerBar"?: 4, "automations": [{"track": "AUDIO - Sub", "device": "mixer", "param": "Volume",
        "unit": "rel|disp|raw", "res": 8, "curve": "lin", "hold": false, "accept": ["fades"], "points": [["5|1", -5], ["9|1", 0]]}]} (param explicite exigé, ≤ 32 entrées, ≤ 256 Kio).
        Renvoie `sha256` (spec), `plan_sha256` (plan relu) et le plan de chaque entrée : à lire avec l'utilisateur avant live_automation_commit. Plan refusé si une entrée est en erreur ou si la plage n'est pas couverte."""
        try: spec, digest, expected = gw.validate_spec(spec)
        except ValueError as exc: raise ToolError(str(exc))
        try: return gw.preview_spec(digest, expected, apply_runner(spec, WRITE_TIMEOUT))
        except ValueError as exc: raise ToolError(str(exc))

    if not write: return mcp

    # ----- écriture (--write) -----
    @mcp.tool(name="live_automation_commit", annotations=WRITES_REPLACING)
    def live_automation_commit(spec: dict[str, Any], sha256: str, plan_sha256: str) -> dict[str, Any]:
        """Écrit l'automation d'une spec déjà prévisualisée. Replanifie puis compare : refus si la spec (`sha256`) ou le plan (`plan_sha256`, donc le Set) diffère de live_automation_preview.
        Chaque entrée est une étape d'annulation Live (Cmd+Z) ; une écriture partielle est signalée avec le journal. Contrôler ensuite dans Live (`verify_in_live`)."""
        try: spec, digest, expected = gw.validate_spec(spec)
        except ValueError as exc: raise ToolError(str(exc))
        with _write_lock:
            try: return gw.commit_spec(digest, expected, sha256, plan_sha256, apply_runner(spec, COMMIT_TIMEOUT))
            except ValueError as exc: raise ToolError(str(exc))

    @mcp.tool(name="live_setparam", annotations=WRITES)
    def live_setparam(track: str, device: str, param: str, value: float, unit: Literal["disp", "raw"] = "disp", override: bool = False) -> dict[str, Any]:
        """Règle un paramètre (device = nom du device, ou « mixer » pour Volume, Pan, Send A…) et le relit : avant / après / état d'automation. `disp` = valeur affichée (dB, Hz…), `raw` = valeur brute (obligatoire
        pour un paramètre quantifié). Refusé si le paramètre est automatisé, sauf override=true (une écriture manuelle surcharge alors l'automation)."""
        rows, _ = run("/setparam", [track, device, param, float(value), unit] + (["override"] if override else []), WRITE_TIMEOUT, write=True)
        return {"rows": rows}

    @mcp.tool(name="live_snapshot", annotations=WRITES)
    def live_snapshot(track: str, scope: Optional[str] = None) -> dict[str, Any]:
        """Photo des valeurs d'une piste (mixer + devices, ou un seul : nom de device ou « mixer »), gardée jusqu'au redémarrage de Live. À prendre avant de régler ; retour : identifiant pour live_restore."""
        rows, _ = run("/snapshot", [track] + ([scope] if scope else []), WRITE_TIMEOUT, write=True)
        return {"rows": rows}

    @mcp.tool(name="live_restore", annotations=WRITES_REPLACING)
    def live_restore(snapshot_id: str, override: bool = False) -> dict[str, Any]:
        """Remet les valeurs d'un snapshot en une étape d'annulation, relit, et défait l'étape si un paramètre refuse. Refusé si un paramètre est automatisé, sauf override=true."""
        rows, _ = run("/restore", [snapshot_id] + (["override"] if override else []), WRITE_TIMEOUT, write=True)
        return {"rows": rows}

    @mcp.tool(name="live_notes_write", annotations=WRITES_REPLACING)
    def live_notes_write(mode: Literal["set", "add"], track: str, clip: str | float, notes: list[Note], window_start: Optional[float] = None, window_end: Optional[float] = None) -> dict[str, Any]:
        """Écrit des notes MIDI dans un clip d'arrangement. mode « set » remplace toutes les notes du clip (ou celles de la fenêtre [window_start, window_end[, en temps relatifs au clip ; une note hors fenêtre est refusée),
        « add » ajoute. clip : référence `o:<session>:<n>` (live_read /clips) ou temps qui tombe dans le clip (« 17|1 »). C3 = 60. Une étape d'annulation, relecture note à note, défaite si Live n'a pas écrit exactement ce qui était demandé."""
        if (window_start is None) != (window_end is None): raise ToolError("window_start et window_end vont ensemble")
        if mode == "add" and window_start is not None: raise ToolError("la fenêtre ne s'applique qu'au mode set")
        if not notes: raise ToolError("notes vide : l'effacement d'un clip n'est pas exposé")
        payload = json.dumps([n.model_dump() for n in notes])
        window = [] if window_start is None else [float(window_start), float(window_end)]
        rows, _ = run("/notes", [mode, track, clip, payload] + window, WRITE_TIMEOUT, write=True, times=True)
        return {"rows": rows}

    @mcp.tool(name="live_load_device", annotations=WRITES)
    def live_load_device(track: str, name: str, source: Literal["plugins", "sounds", "instruments", "audio_effects", "midi_effects", "drums", "max_for_live", "user_library"] = "plugins",
                         replace: Optional[str] = None) -> dict[str, Any]:
        """Charge un device par le navigateur de Live, SANS hot-swap : ajouté en fin de chaîne, ou à la place du device `replace`. Contrôlé après coup (+1 device, aucun autre remplacé, aucune autre piste touchée), sinon
        E_NOT_APPLIED et Cmd+Z. Nom exact, sinon sous-chaîne unique (« Serum 2 » existe en VST3 et AU : préciser). Pas de nouvel effet natif de Live dans les chaînes de mix."""
        rows, _ = run("/load", [track, name, source] + (["replace=" + replace] if replace else []), WRITE_TIMEOUT, write=True)
        return {"rows": rows}

    @mcp.tool(name="live_transport", annotations=WRITES)
    def live_transport(action: Literal["play", "stop", "pos", "loop_on", "loop_off", "loop"], position: str | float | None = None, loop_length: Optional[float] = None) -> dict[str, Any]:
        """Transport de Live. play (position facultative) · stop · pos (position, refusé pendant la lecture) · loop_on · loop_off · loop (position = début, loop_length en temps). Temps : nombre de temps ou « mesure|temps »."""
        needs = {"pos": ("position",), "loop": ("position", "loop_length")}.get(action, ())
        given = {"position": position, "loop_length": loop_length}
        if any(given[k] is None for k in needs): raise ToolError("%s exige : %s" % (action, ", ".join(needs)))
        args = {"play": ["play"] + ([position] if position is not None else []), "stop": ["stop"], "pos": ["pos", position], "loop_on": ["loop", "on"],
                "loop_off": ["loop", "off"], "loop": ["loop", position, loop_length]}[action]
        rows, _ = run("/transport", args, WRITE_TIMEOUT, write=True, times=True)
        return {"rows": rows}

    @mcp.tool(name="live_locator", annotations=WRITES)
    def live_locator(time: str | float, name: str) -> dict[str, Any]:
        """Pose un repère d'arrangement à `time`, ou le renomme s'il en existe déjà un à cet instant."""
        rows, _ = run("/locator", [time, name], WRITE_TIMEOUT, write=True, times=True)
        return {"rows": rows}

    @mcp.tool(name="live_meters", annotations=WRITES)
    def live_meters(start: str | float, seconds: float, tracks: Optional[list[str]] = None) -> dict[str, Any]:
        """Lit les vu-mètres pendant la lecture (≤ 30 s) : transport arrêté → lecture lancée à `start` puis arrêtée et curseur restauré ; déjà en lecture → rien n'est touché. Crête par piste (post-devices et post-fader)
        et master (pré-devices) ; les dB sont RELATIFS (fiables ±1 dB entre −7 et −16 dB), pas une mesure de niveau absolue."""
        if not 0 < seconds <= 30: raise ToolError("seconds doit être dans ]0, 30]")
        rows, _ = run("/meters", [start, float(seconds)] + (tracks or []), WRITE_TIMEOUT, write=True, times=True)
        return {"rows": rows}

    return mcp


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="expose aussi les outils d'écriture (sinon lecture seule ; ou LOM_MCP_WRITE=1)")
    a = ap.parse_args(argv)
    write = a.write or os.environ.get("LOM_MCP_WRITE") == "1"
    print("LOM Bridge MCP %s (stdio) — %s" % (CONNECTOR_VERSION, "écriture ACTIVE" if write else "lecture seule"), file=sys.stderr, flush=True)
    build_server(write).run("stdio")


if __name__ == "__main__":
    main()
