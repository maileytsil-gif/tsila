---
titre: "Serum 2 — content setup (rich6feet/serum : contenu d'usine, dossiers, presets)"
source: https://raw.githubusercontent.com/rich6feet/serum/main/docs/serum2-content-setup.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: traitement des claviers : soothe2 (résonances), Vulf Compressor, Pro-Q 4, Ozone Imager, Serum 2, revues
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Serum 2 Content Setup

This generator only writes wavetable / sample / multisample / spectral paths
that exist on **your** Serum 2 install. So when you ask for a "spectral pad" or
"granular drone", you actually get one — not a phantom path that fails to load.

To make that work, the app needs to know where your Serum 2 content lives.

## How content paths work in Serum 2

A `.SerumPreset` file stores **relative** paths like
`S2 Tables/Default Shapes.wav` or `Factory/Spatial/Space Coins.flac`. Serum 2
resolves those relative to its content root, which on a default install is:


| OS      | Content root                            |
| ------- | --------------------------------------- |
| Windows | `%USERPROFILE%\Documents\Xfer\Serum 2\` |
| macOS   | `~/Music/Xfer/Serum 2/`                 |
| Linux   | `~/.config/Xfer/Serum 2/`               |


A second legacy root is also searched (`Documents\Xfer\Serum\` etc.) so users
who carry wavetables forward from Serum 1 don't have to reorganise.

## Step 1: Run the content scanner

The scanner probes a long list of likely Serum 2 install locations, walks each
existing root in full, and classifies any `.wav`, `.flac`, `.aif`, or `.sfz`
file by extension and parent folder name. It then writes
`assets/serum2-content-index.json`.

```bash
node scripts/scan-serum2-content.mjs
```

### Three content trees, five oscillator modes

Serum 2 has five oscillator modes (Wavetable, Sample, Granular, MultiSample,
Spectral) but only three on-disk content trees:


| Tree            | Used by                              | Path convention in presets                                                         |
| --------------- | ------------------------------------ | ---------------------------------------------------------------------------------- |
| `Tables/`       | Wavetable osc                        | `Analog/MB Saw.wav`, `S2 Tables/Default Shapes.wav`, `Spectral/Monster 8 [SL].wav` |
| `Samples/`      | Sample / Granular / **Spectral** osc | `Factory/Synth/Modern Wub.flac`, `Factory Non-Tonal/Drum/Kick/808 Kick A 01.flac`  |
| `Multisamples/` | MultiSample osc                      | `Factory/Plucked/Oud.sfz`, `Factory/Keys/Elec.Piano Wurli.sfz`                     |


**Spectral is a MODE, not a separate content kind.** Per the user guide
(p.106): *"In addition to tonal and non-tonal factory presets, you can load
Serum wavetables as samples."* The Spectral oscillator picks files from the
same `Samples/` tree that Sample and Granular use. Confirmed from factory
presets: `BA - Versatile` loads `Factory/Plucked/Balafon Short.flac` into
Spectral; `DR - Snare Fill` loads `Factory Non-Tonal/Drum/Rim/505 Rim.flac`.
There is no separate "spectral content pack" — if you have samples installed,
spectral works.

**Path prefix stripping.** Serum 2 stores paths *relative to the tree root* —
without the top-level `Tables/`, `Samples/`, or `Multisamples/` prefix. The
scanner strips those prefixes when populating the index so generated presets
write paths Serum can actually resolve.

### Extensions and how each is classified


| Extension                                                                              | Default classification                            |
| -------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `.sfz`                                                                                 | multisample (always)                              |
| `.wav` under `Tables/`                                                                 | wavetable                                         |
| `.wav`/`.flac`/`.aif` under `Samples/Factory/Spatial/`, `…/Noises/`, `…/Textures/`     | granular (preferred for granular-mode prompts)    |
| `.wav`/`.flac`/`.aif` anywhere else under `Samples/` or `Multisamples/<inst> Samples/` | sample                                            |
| `.wav`/`.flac` under `Impulses/`                                                       | skipped (convolution IRs, not oscillator content) |


### The probe list covers all of these automatically:

- `%USERPROFILE%\Documents\Xfer\Serum 2\` (default Windows)
- `%OneDrive%\Documents\Xfer\Serum 2\` (OneDrive-redirected Documents — very common on Windows 10/11)
- `%OneDriveConsumer%\Documents\Xfer\Serum 2\` (OneDrive Personal)
- `%OneDriveCommercial%\Documents\Xfer\Serum 2\` (OneDrive Business)
- `~/Music/Xfer/Serum 2/` (default macOS)
- `~/.config/Xfer/Serum 2/` (Linux)
- `%PROGRAMDATA%\Xfer\Serum 2\` and `%PUBLIC%\Documents\Xfer\Serum 2\` (Windows shared content)
- `C:\Xfer\Serum 2\`, `D:\Xfer\Serum 2\`, …, `H:\Xfer\Serum 2\` (custom drives)
- Any path you list in `.serum2-content-roots` at the project root, one per line.

Run with `--verbose` (the default) to see exactly which probes hit and which
were skipped — the JSON index also records every probe under `index.probes`
for inspection from the UI.

### If none of the probes match

Open Serum 2, right-click any factory wavetable, choose **Show in
Explorer / Finder**, copy the parent folder, and re-run:

```bash
node scripts/scan-serum2-content.mjs --root "<paste path here>"
```

Or pin it permanently by writing the path into a file at the project root
named `.serum2-content-roots` (one path per line):

```
D:\My Drive\Xfer\Serum 2
\\NAS\Audio\Xfer\Serum 2
```

### Inside the desktop app

The **Serum 2 Content** panel has:

- A "Rescan content" button that runs the scanner with no terminal.
- A "Custom Serum 2 content root" text field for one-off path overrides.
- An expandable "Show every path the scanner probed" report so you can see
exactly which candidates were tried and which existed.

## Step 2: Generate as normal

Once the index exists, the exporter consults it on every preset build:

- Requested wavetable found in your library → it's written verbatim.
- Wavetable not found → fuzzy-match falls back to the closest installed file,
or `S2 Tables/Default Shapes.wav` (which always ships with Serum 2). A
`contentWarnings` entry tells you exactly which substitution happened.
- Granular / sample / multisample / spectral source missing → that oscillator
is downgraded to wavetable mode rather than ship a broken preset, again
with a recorded warning.

The Electron `desktop:save-generated` IPC returns these warnings as
`result.contentWarnings`, and the app shows them next to the export confirmation.

## Step 3: Install missing factory content

If the **Serum 2 Content** panel shows zero spectral / granular / multisample
files, you don't have the factory packs installed yet. Get them via:

1. Sign into your Xfer Records account at [https://xferrecords.com/](https://xferrecords.com/).
2. Visit your downloads page and grab the latest **Serum 2 Content Pack**
  installer for your OS. (Serum 2 ships content separately from the plugin
   binary so users can store it on a different drive.)
3. Run the installer. By default it writes to the content root listed above.
4. Click **Rescan content** in the app (or rerun the scanner script).

## Common gotchas


| Symptom                                 | Likely fix                                                                                                                                                  |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All counts are 0 even after install     | Pass `--root` with the actual install path; check that you have read access.                                                                                |
| "Spectral mode picks the wrong sample"  | Spectral pulls from your `Samples/` tree. Add tags to your prompt that match the file path (e.g. "synth modern wub" picks `Factory/Synth/Modern Wub.flac`). |
| Multisamples count is 0                 | Look for `Factory/Keys/*.sfz` etc.; if missing install the "Multisample Instruments" content pack.                                                          |
| Generator picks an unexpected wavetable | Check `contentWarnings` in the export panel — fuzzy match may be substituting because the named table isn't in your library.                                |
| Custom user wavetables not seen         | Drop them into `Documents/Xfer/Serum 2/Tables/` (Windows) and rescan.                                                                                       |


## Where the index lives

`assets/serum2-content-index.json` is written by the scanner and read by
`scripts/serum2-pack-core.mjs`. It's safe to commit (so other users on the same
machine inherit the same view), or to gitignore if it's purely a local cache.
