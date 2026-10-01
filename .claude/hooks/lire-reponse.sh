#!/bin/bash
# Hook Stop : lit à voix haute la dernière réponse de Claude avec « say » (macOS).
# Sans effet là où « say » n'existe pas (session cloud, Linux).
# Réglages (variables d'environnement, voir .claude/settings.json) :
#   CLAUDE_VOIX        voix macOS (défaut Thomas ; liste : say -v '?' | grep fr_)
#   CLAUDE_VOIX_DEBIT  mots par minute (défaut 185)
#   CLAUDE_VOIX_OFF=1  coupe la lecture
command -v say >/dev/null 2>&1 || exit 0
[ "${CLAUDE_VOIX_OFF:-0}" = "1" ] && exit 0
dossier="$(cd "$(dirname "$0")" && pwd)"
texte="$(python3 "$dossier/texte_reponse.py")"
[ -z "$texte" ] && exit 0
pkill -x say >/dev/null 2>&1
( printf '%s' "$texte" | say -v "${CLAUDE_VOIX:-Thomas}" -r "${CLAUDE_VOIX_DEBIT:-185}" ) >/dev/null 2>&1 &
disown 2>/dev/null
exit 0
