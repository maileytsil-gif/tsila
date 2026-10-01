---
titre: "mikeb55 Big-Band-Arranging — audit de réutilisation des modules (structure du dépôt, registres, moteurs)"
source: https://raw.githubusercontent.com/mikeb55/Big-Band-Arranging/main/docs/big_band_reuse_audit.md
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: big band ; arrangement
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Document communautaire [HEUR] : valeurs à vérifier avant de les tenir pour établies.

# Big Band Module Reuse Audit

## 1. Repo Structure Overview

```
Big-Band-Arranging/
├── charts/Beatrice/           # Main chart: 3-chorus Beatrice arrangement
│   ├── 01_leadsheet/          # Piano lead sheets (MusicXML, Sibelius)
│   ├── 02_reharm/             # Reharm logic, chorus styles, GCE evaluation
│   ├── 03_arrangement/        # Failed AI orchestration record
│   └── 06_notes/              # Bora lessons, Toshi assignments
├── archive/local_failed_generations/  # V1–V16 Python scripts, MusicXML, GCE reports
├── Assignments/               # Reharm docs, create_reharm scripts
├── Big Band Books/            # Reference PDFs, ChatGPT summaries
├── docs/                      # Alternate arrangement analysis
├── Engines/                   # .gitkeep placeholders (Mighty_Ten, reharm_tests)
├── migration/                 # Repo move, next steps
├── Research/                 # Harmonic analysis, arranging books
├── Session 0–6/               # Course exercises, assignments, plans
└── scripts/                   # open_big_band_repo, safe_rehome_repo
```

---

## 2. Candidate Files Worth Mining

| File Path | Purpose | Reuse Value |
|-----------|---------|-------------|
| `charts/Beatrice/02_reharm/Beatrice_lesson_notes_V4.md` | 3-chorus concept: Chorus 1 full ensemble, Chorus 2 reduced pads, Chorus 3 rhythmic hits; sectional contrast | **High** |
| `charts/Beatrice/02_reharm/Beatrice_reharm_rationale_V4.md` | Chorus role table (reference / lyrical / modern); harmonic density per chorus | **High** |
| `charts/Beatrice/02_reharm/chorus2_wheeler_style.md` | Horn-section orchestration: trumpets open voicings, saxes melody+3-part, trombones pedal; section contrast | **High** |
| `charts/Beatrice/02_reharm/chorus2_scofield_style.md` | Sax melody+syncopation; trombones bass/counter-rhythms; rhythmic hits vs sustained | **High** |
| `charts/Beatrice/02_reharm/chorus2_shorter_style.md` | Sparse harmonic rhythm; trumpets pads; sax unison; trombones pedal/guide-tone | **Medium** |
| `charts/Beatrice/02_reharm/chorus2_upperstructure_style.md` | Trumpets upper-structure triads; saxes melody+#11; trombones root/shell | **Medium** |
| `charts/Beatrice/02_reharm/chorus2_polyphonic_style.md` | Two-part counterpoint; section contrast linear vs vertical | **Medium** |
| `charts/Beatrice/02_reharm/Beatrice_reharm_summary.md` | Possible horn section colours table (Chorus × Trumpets/Saxes/Trombones) | **High** |
| `archive/local_failed_generations/V10.0-Refinement-Notes.md` | Guide-tone spine, sax soli, counterpoint, brass balance, shout chorus, density control, rhythm section | **High** |
| `archive/local_failed_generations/V12.0-Arranger-Diagnostic.md` | Diagnostic checklist: range, brass balance, sax register, guide-tone, counterpoint, motivic reuse, density, shout, rhythm section | **High** |
| `archive/local_failed_generations/beatrice_v3_arrangement.py` | RANGES dict, drop-2 voicing, get_density(), get_texture(), walking_bass_notes(), validate_ranges() | **Medium** |
| `charts/Beatrice/03_arrangement/none_of_these_work.md` | Anti-patterns: density explosions, all sections simultaneous, rhythm overpowering horns, shout without preparation | **High** |
| `charts/Beatrice/02_reharm/GCE_evaluation_V4.md` | GCE criteria: melodic integrity, harmonic interest, chorus differentiation, arranging potential | **Medium** |
| `docs/alternate-arrangement-analysis.md` | Engine-based alternate arrangement concepts; sectional logic; BIAB suitability | **Low** (chamber-focused) |
| `Research/modern_big_band_arranging_books.md` | Book references: Nestico, Garcia, Pease, section writing | **Low** (reference only) |
| `charts/Beatrice/02_reharm/Beatrice-3-Chorus-Reharm-V1.md` | Chorus 1/2/3 texture descriptions; sectional boundaries | **Medium** |
| `charts/Beatrice/02_reharm/Beatrice_melody_transfer_notes.md` | Shell voicings, variation points, voice-leading | **Low** (Beatrice-specific) |
| `archive/local_failed_generations/transfer_beatrice_melody.py` | shell_voicing() chord-to-pitch logic | **Low** |
| `archive/local_failed_generations/generate_beatrice_v3.py` | shell_voicing(), chord symbol parsing | **Low** |
| `Session 5/Vol 2 Session 5 Assignement/V16-Beatrice-Plan.md` | Sibelius playback, swing marking, engraving checklist | **Low** (notation-only) |

---

## 3. Reusable Concepts by Category

### Section Allocation

- **Chorus 1:** Full ensemble; melody in saxes or trumpet; block voicings.
- **Chorus 2:** Reduced texture; sustained pads; open voicings; Wheeler-style colour.
- **Chorus 3:** Rhythmic hits; counterlines; tutti on dominant approaches; climax.
- **Horn section colours table** (Beatrice_reharm_summary.md): Trumpets/Saxes/Trombones roles per chorus.
- **Section contrast:** Full ensemble on A sections; reduced on bridge; Wheeler-style transparency.

### Texture States

- **Full ensemble:** Block voicings; tutti.
- **Reduced:** Sax-only (21–22); thin before shout (bar 40).
- **Sax soli:** Top voice melody; inner voices stepwise; drop-2.
- **Brass punctuation:** Staccato hits on beats 2 and 4.
- **Pad:** Sustained, open voicings; 4ths and 5ths.

### Density Arcs

- **get_density(m_idx, chorus)** in beatrice_v3_arrangement.py: 0=thin, 1=medium, 2=full; shout chorus builds to full.
- **Max two sections** except at climactic moments (V10).
- **Bar 40 thinned** before full shout (trumpet 1 + rhythm only).
- **Chorus 3 bars 12–16:** Density 2 (full).

### Shout / Soli / Pad Logic

- **Shout chorus:** Syncopated brass figures on beats 2 and 4; sax rhythmic backgrounds; texture contrast; bar before thinned.
- **Sax soli:** Bebop passing tones in inner voices; stepwise motion; tenuto for blend.
- **Pad:** Trumpets open voicings; sustained; Wheeler-style.
- **Punctuation:** Brass staccato; sax hits; anticipatory hits on beat 4-and.

### Rhythm Section Behavior

- **Bass:** Walking bass with approach tones; roots + 5th + 3rd + 7th pattern.
- **Piano:** Sparse comping; varied rhythms; half-note chords at climax.
- **Guitar:** Freddie Green–style quarter-note comping.
- **Drums:** Setup fill before shout (bar 40); rests in sparse sections.

### Phrase-to-Section Mapping

- **3 choruses × 16 bars** = 48 bars.
- **Engine architecture** (V12): Wheeler (13–24) → Polyphonic/Sax soli (25–32) → Shorter/Scofield (33–40) → Thad Jones shout (41–48).
- **get_texture(m_idx):** Block = (m_idx - 12) // 4, cycles 0–3.
- **Rehearsal marks:** Chorus 1, Chorus 2, Chorus 3; Bar 13.

### Voicing / Register Rules

- **RANGES** (beatrice_v3_arrangement.py): trumpet (54–86), trombone (40–70), alto (61–81), tenor (56–76), bari (36–60).
- **Drop-2** for sax and brass.
- **Voice-leading:** voice_lead_to_nearest(); stepwise motion; clamp_midi().
- **Guide-tone spine:** Alto 2 carries 3rds and 7ths.
- **Brass spacing:** Trombones wider below middle C.

### Anti-Monotony / Validation Logic

- **validate_ranges():** Check each part against RANGES; report violations.
- **V12 diagnostic checklist:** Instrument range, brass balance, sax register, guide-tone clarity, counterpoint independence, motivic reuse, density, shout intensity, rhythm section.
- **none_of_these_work.md:** Reject density explosions, all sections simultaneous, rhythm overpowering horns, shout without preparation.

---

## 4. Specific Notes

### Sax / Brass / Rhythm Role Separation

- **Yes.** Chorus style docs and V10/V12 explicitly assign: trumpets (melody, punctuation, pads), saxes (melody, soli, backgrounds), trombones (bass, pedal, harmonic foundation).
- Rhythm section roles: bass walking, piano comping, drums setup/rests.

### Reduced-Score or Sketch Workflow

- **Yes.** Lead sheet (melody + chord symbols only) precedes full orchestration.
- V4 reharm is the harmonic reference; Bora’s 12 bars are the structural foundation.
- Piano reduction exists (V6.x) as intermediate.

### Event-List Allocation Ideas

- **Partial.** Python scripts allocate notes to parts by chord symbol + melody; no formal event-list abstraction.
- Logic: chord → chord_to_pitches() → drop-2 voicing → assign to part by index.
- No explicit event-list schema; allocation is inline in loops.

### Background Figure Design

- **Yes.** Sax soli inner voices: stepwise motion, chord tones + passing tones.
- Brass punctuations: staccato on beats 2 and 4.
- Motivic reuse: short-short-long in Tpt2, sax hits.
- Counterpoint: trumpet guide-tone counterline on offbeats; trombone 7th in bass.

### Cadence Build Logic

- **Yes.** Chorus 3 bars 12–16 = shout; density builds.
- Bar 40 thinned before bar 41 full shout.
- Dominant approaches (Gm9 C7, etc.) prepare tutti.

### Dynamic Density Planning

- **Yes.** get_density() maps measure index and chorus to 0/1/2.
- Block-based (4-bar blocks) with chorus override for shout.
- V10: “Max two sections except at climactic moments.”

### Useful Arranging Checklists

- **Yes.** V10 Refinement validation list; V12 diagnostic checklist.
- Items: range, guide-tone, sax soli, counterpoint, brass balance, shout, rhythm section, density.

### Big-Band-Specific Validation Ideas

- **Yes.** Instrument range clamping; brass balance (Tpt1 overload); sax register (bari low); guide-tone clarity; shout anticipations; rhythm section setup.
