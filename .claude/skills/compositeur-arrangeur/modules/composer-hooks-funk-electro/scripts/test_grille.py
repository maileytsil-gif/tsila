#!/usr/bin/env python3
"""Tests hors Live des scripts du skill : python3 -m unittest discover -s scripts -p 'test_*.py' -v"""
import glob
import importlib.util
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ICI = pathlib.Path(__file__).resolve().parent
SKILL = ICI.parent
sys.path.insert(0, str(ICI))
import grille  # noqa: E402


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


qwen = charger('qwen_musique', ICI / 'qwen-musique.py')


class Grille(unittest.TestCase):
    def test_octaves(self):
        self.assertEqual(grille.lire_note('C3'), 60)
        self.assertEqual(grille.lire_note('C4', 'scientifique'), 60)
        self.assertEqual(grille.lire_note('F1', 'scientifique'), 29)  # 43,65 Hz = F0 dans Live
        self.assertEqual(grille.nom(29), 'F0')
        self.assertEqual(grille.lire_note('C-2'), 0)
        with self.assertRaises(ValueError):
            grille.lire_note('H3')

    def test_positions_et_ppal(self):
        notes = grille.lire_voix('Ab3[1&:2] C4[2a:1] Eb4[3:3] | %')
        self.assertEqual([n['pas'] for n in notes], [2, 7, 8, 2, 7, 8])
        lignes = [f"v{n['vel']} {grille.duree_ppal(n['duree'])} {grille.nom(n['midi'])} {grille.pos_ppal(n)}" for n in notes[:3]]
        self.assertEqual(lignes, ['v96 n/8 Ab3 1|1.5', 'v96 n/16 C4 1|2.75', 'v96 n3/16 Eb4 1|3'])
        self.assertEqual(notes[3]['mesure'], 2)

    def test_accords_velocite_tension(self):
        notes = grille.lire_voix('F3+Ab3+C4[1:4] Bb3![3a:1:110]')
        self.assertEqual([n['midi'] for n in notes], [65, 68, 72, 70])
        self.assertTrue(notes[-1]['voulue'])
        self.assertEqual(notes[-1]['vel'], 110)

    def test_degres(self):
        _, _, r, _, ivs = grille.lire_accords('Bb13')[0][0]
        self.assertEqual([grille.degre(grille.lire_note(n), r, ivs) for n in ('D3', 'G3', 'Ab3', 'C4')], ['3', '13', 'b7', '9'])
        _, _, r, _, ivs = grille.lire_accords('A7(b9,#9)')[0][0]
        self.assertEqual([grille.degre(grille.lire_note(n), r, ivs) for n in ('Bb3', 'C4', 'C#4')], ['b9', '#9', '3'])

    def test_erreur_de_la_version_codex_detectee(self):
        # m3 d'origine : La naturel présenté comme « tierce majeure de Bb13 »
        notes = grille.lire_voix('A3[1&:2] C4[2a:1] D4[3&:2] C4[4&:1]')
        erreurs = grille.analyser(notes, grille.lire_accords('Bb13'))
        self.assertEqual(len(erreurs), 1)
        self.assertIn('A3', erreurs[0])
        self.assertIn('Ab, Bb', erreurs[0])

    def test_note_de_passage_acceptee(self):
        notes = grille.lire_voix('A3[3&:1] C4[4:1] D4[4&:1]')
        self.assertEqual(grille.analyser(notes, grille.lire_accords('G13')), [])
        self.assertEqual(notes[1]['statut'], 'passage/approche')

    def test_chevauchement(self):
        notes = grille.lire_voix('C3[1:4] C3[1&:2]')
        self.assertTrue(any('chevauche' in e for e in grille.analyser(notes, [])))

    def test_transposition(self):
        self.assertEqual(grille.transposer_accords('Fm9 | Bb13 Eb9/G', -3), 'Dm9 | G13 C9/E')

    def test_references_verifiees(self):
        fichiers = sorted(glob.glob(str(SKILL / 'references' / '*.md')))
        self.assertEqual(grille.main(['--verifier'] + fichiers), 0)
        self.assertGreaterEqual(sum(1 for f in fichiers for _ in grille.blocs(f)), 5)

    def test_accords_identiques_a_theorie(self):
        chemin = SKILL.parent / 'theorie-musicale-electronique' / 'scripts' / 'theorie.py'
        if not chemin.is_file():
            self.skipTest('theorie.py absent (skill installé seul)')
        theorie = charger('theorie', chemin)
        self.assertEqual(grille.QUALITES, theorie.QUALITES)


class Qwen(unittest.TestCase):
    def test_choix_par_pertinence(self):
        refs = qwen.choisir('Thème électro chill avec MIDI et patch Serum 2', maximum=4)
        self.assertIn('chill-electro-jazz.md', refs)
        self.assertIn('atelier-themes.md', refs)
        self.assertEqual(qwen.choisir('bonjour'), qwen.DEFAUT)
        self.assertEqual(qwen.choisir('bonjour', ['sources-videos.md'])[0], 'sources-videos.md')

    def test_references_connues_existent(self):
        for nom in qwen.MOTS:
            self.assertTrue((SKILL / 'references' / nom).is_file(), nom)

    def test_fenetre_respectee(self):
        refs = list(qwen.MOTS)
        systeme, gardees, ecartees, total = qwen.construire(SKILL, 'demande', refs, 12000, 3000)
        self.assertLessEqual(total + qwen.jetons(qwen.SYSTEME) + qwen.jetons('demande'), 12000 - 3000)
        self.assertTrue(ecartees)
        self.assertIn('# Composer un hook jouable', systeme)


class Installation(unittest.TestCase):
    def test_sauvegarde_hors_du_dossier_des_skills(self):
        with tempfile.TemporaryDirectory() as h:
            env = dict(os.environ, HOME=h)
            for _ in range(2):
                subprocess.run(['bash', str(ICI / 'install.sh'), '--claude', '--codex', '--qwen'], env=env, check=True,
                               capture_output=True)
            skills = pathlib.Path(h, '.claude', 'skills')
            # Le skill entier (compositeur-arrangeur) est installé, ce module avec lui.
            self.assertEqual([p.name for p in skills.iterdir()], ['compositeur-arrangeur'])
            module = skills / 'compositeur-arrangeur' / 'modules' / 'composer-hooks-funk-electro'
            self.assertTrue((module / 'GUIDE.md').is_file())
            self.assertFalse((module / 'SKILL.md').exists())
            self.assertEqual(len(list(pathlib.Path(h, '.skills-sauvegardes').iterdir())), 2)
            lien = pathlib.Path(h, '.local', 'bin', 'qwen-musique')
            self.assertTrue(lien.resolve().is_file())
            sortie = subprocess.run([sys.executable, str(lien), '--dry-run', 'kick 808'], env=env,
                                    capture_output=True, text=True, check=True)
            self.assertIn(str(module), sortie.stderr)


if __name__ == '__main__':
    unittest.main()
