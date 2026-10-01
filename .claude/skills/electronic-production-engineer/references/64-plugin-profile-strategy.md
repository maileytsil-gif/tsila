# Plug-in profile strategy

## Purpose
A profile teaches the bridge how a specific instrument/effect maps to the common semantic vocabulary without hard-coding fragile numeric indexes.

## What Live exposes (the limit for every tool)
- Live fills a plug-in's device panel automatically only up to 64 parameters. Above that the panel is empty and the LOM (bridge and Producer Pal alike) sees `Device On` only, until parameters are added with Configure, a MIDI/macro mapping, or by moving the control while recording automation. Cap: 128 per instance (not confirmed for Serum 2); `-_PluginAutoPopulateThreshold=128` in `Options.txt` is unconfirmed for VST3 [TEST].
- The Configure order is the index in `device.parameters`; device title bar → "Save as Default Configuration" gives new instances the same list and order (not Serum's "Save as Default Preset").
- Serum 2 FX parameters appear only after right-click → Automate inside Serum (Xfer staff, forum), sometimes after bypass/unbypass; most Serum edits need screen control ([serum2.md](../../vst-sound-design/references/serum2.md)). Sources: [serum2-automation-et-migration.md](../../sound-designer-serum/references/serum2-automation-et-migration.md), § 12 of [serum2-cartographie.md](../../sound-designer-serum/references/serum2-cartographie.md).
- Measured here ([fiches.md](../../effets-plugins/references/fiches.md), Live 12.4.5, VST3): exposed: REQ 6, Q10, SSLEQ, API-2500, L2, J37, MetaFlanger, bx_glue, Ozone Imager 2 (Width, Stereoize); `Device On` only: Serum 2 (unconfigured), Pro-Q 4, F6, Curves AQ, soothe3, TDR Nova, Insight 2, Tonal Balance Control 3, SPAN; not probed: L4, Pro-C 3, SSL G-Master, R-Bass/MaxxBass, Analog Obsession, Komplete Kontrol, Maschine 3 [TEST: `lom.py params <deviceRef>`, one line = window only].

## Profile identity
A profile should include:
- vendor
- product
- plug-in format (Serum 2 is installed as VST3 and AU: one profile per format)
- detected class/display name
- profile version
- plug-in version (Serum 2 cannot load data saved by a newer version)
- saved default Configure layout assumed or not, and the parameter count seen
- semantic mappings by parameter name/original name and optional stable parameter identity supplied by the implementation
- safe ranges / protected controls
- notes about quantized values (`setparam` needs `raw`)

## Priority in this studio
By what can be profiled now, then by use:
1. Waves REQ 6, API-2500, L2, J37, MetaFlanger; Plugin Alliance bx_glue (exposed, used in the mix chains)
2. Ableton native Racks/devices used in the template
3. Serum 2 (after a saved default Configure layout)
4. FabFilter Pro-Q 4, soothe3 (after Configure [TEST])
5. Waves L4, F6, SSL G-Master, R-Bass / MaxxBass; FabFilter Pro-C 3; Analog Obsession RazorClip / TheBus (probe first)
6. Komplete Kontrol and Maschine 3 plug-ins (screen-only here)

## Profile learning workflow
1. In a copy of the Set or a throwaway Set, load one instance with `lom.py load`.
2. `lom.py params <deviceRef>`; if only `Device On`, build the Configure list (user or screen control) and save it as default configuration.
3. Match only high-confidence semantic targets.
4. Exercise each mapped control through a small approved range (`snapshot` → `setparam` → display check → `restore`), confirmed by screenshot or by the user's ear.
5. Save the mapping profile (format: `bridge/profile-example.json`).
6. Revalidate after plug-in updates, and names/indexes in each session.

## Komplete Kontrol / NKS
NKS is useful as a semantic browsing and pre-mapping layer but is not treated as the bridge API. Maschine 3.6 and Komplete Kontrol 3.5 have no API here: foreground screen control only ([native-instruments-control](../../native-instruments-control/SKILL.md)). Prefer parameters exposed by Ableton/LOM. Do not reverse-engineer NKS files as the primary control strategy.

## GUI fallback
A missing function may produce a `gui_fallback` action, approved like any write ([plugins.md](../../ableton-live-session/references/plugins.md)): open the window with `ppal-select` (`openPluginWindow: true`) or the device's window button; screenshot before and after every gesture, coordinates from the latest screenshot. Serum 2 takes background clicks (toggles, tabs, preset browser) but not knob drags or typed values → full screen control or the user; Pro-Q 4 ignores typing; soothe3 accepts double-click + value + Enter. Window edits are neither journaled nor in a bridge snapshot: save the Set before, record values in the project memory after, re-scan exposed state if any.
