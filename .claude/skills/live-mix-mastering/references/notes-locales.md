# Notes locales (ajoutées le 15 sept. 2026)

- **Chaîne en place** (valeurs du projet deep chill, `../../ableton-live-session/references/mix-chain.md`) : pistes AUDIO → BUS → BUS MASTER 1 (Pro-Q 4 → bx_glue → J37) → BUS MASTER 2 (API-2500 parallèle → Imager) → BUS MASTER 3 (Tonal Balance Control 3 → SPAN → **L2**, plafond −1,0 dBFS) → Main (Utility 0 dB → Insight 2). REF → Main hors limiteur. « Désactiver les traitements de sonie finale » = contourner le L2 de BUS MASTER 3 (`is_active`), après avoir noté son état.
- **ffmpeg absent sur ce Mac** (ni sox, ni pyloudnorm) : LUFS et true peak se lisent dans Insight 2 en bout de Main ou WLM Plus en mesure seule, par capture d'écran ; `../../live-export-wav/scripts/analyze_wav.py` donne crête sample, RMS, écrêtage, durée.
- **Pas d'effets natifs** dans les chaînes de mix et de mastering (règle de l'utilisateur, liste des tolérances dans `../../ableton-live-session/SKILL.md` règle 6).
- Cibles indicatives : crête pré-limiteur −4 à −6 dBFS, sortie ≤ −1 dBTP, LUFS −14 streaming / −9 à −7 club — à confirmer avec l'utilisateur, jamais imposées.
- Procédure amont : `../../ingenieur-mixage/SKILL.md` (diagnostic, tableau mesuré / écouté / supposé, contrôle qualité) puis `../../mixage/SKILL.md` ; outils : `../../mastering-outils/SKILL.md` ; pilotage des plug-ins : `../../effets-plugins/references/fiches.md`.
