"""Tests hors Mac de outils/installer.sh et outils/verifier_skills.py (HOME temporaire, aucun fichier personnel touché).

  python3 -m unittest discover -s outils -p 'test_*.py' -v
"""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

OUTILS = pathlib.Path(__file__).resolve().parent
DEPOT = OUTILS.parent
SKILLS = DEPOT / '.claude' / 'skills'


def installer(home, *args):
    env = dict(os.environ, HOME=str(home))
    return subprocess.run(['bash', str(OUTILS / 'installer.sh'), *args], env=env, capture_output=True, text=True)


class Installer(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.home = pathlib.Path(self._tmp.name)
        (self.home / '.claude').mkdir()
        (self.home / '.qwen').mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def test_simulation_n_ecrit_rien(self):
        r = installer(self.home, '--skill', 'resampling')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('SIMULATION', r.stdout)
        self.assertFalse((self.home / '.claude' / 'skills').exists())
        self.assertFalse((self.home / '.qwen' / 'skills').exists())

    def test_claude_copie_qwen_relie(self):
        r = installer(self.home, '--skill', 'resampling', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        copie = self.home / '.claude' / 'skills' / 'resampling'
        lien = self.home / '.qwen' / 'skills' / 'resampling'
        self.assertEqual((copie / 'SKILL.md').read_bytes(), (SKILLS / 'resampling' / 'SKILL.md').read_bytes())
        self.assertTrue(lien.is_symlink())
        self.assertEqual(lien.resolve(), copie.resolve())
        again = installer(self.home, '--skill', 'resampling', '--appliquer')
        self.assertIn('Rien à changer', again.stdout)

    def test_ancienne_version_sauvegardee_hors_des_skills(self):
        ancien = self.home / '.qwen' / 'skills' / 'resampling'
        ancien.mkdir(parents=True)
        (ancien / 'SKILL.md').write_text('---\nname: resampling\ndescription: ancienne\n---\n')
        r = installer(self.home, '--skill', 'resampling', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        sauvegardes = list((self.home / '.skills-sauvegardes').glob('*/qwen/resampling/SKILL.md'))
        self.assertEqual(len(sauvegardes), 1)
        self.assertIn('ancienne', sauvegardes[0].read_text())
        self.assertTrue((self.home / '.qwen' / 'skills' / 'resampling').is_symlink())

    def test_registre_de_signature_conserve(self):
        installer(self.home, '--claude', '--skill', 'drums-signature', '--appliquer')
        registre = self.home / '.claude' / 'skills' / 'drums-signature' / 'scripts' / 'signature.json'
        registre.write_text('{"kick": "valide par l utilisateur"}')
        skill = self.home / '.claude' / 'skills' / 'drums-signature' / 'SKILL.md'
        skill.write_text(skill.read_text() + '\nmodification locale\n')
        r = installer(self.home, '--claude', '--skill', 'drums-signature', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(registre.read_text(), '{"kick": "valide par l utilisateur"}')
        self.assertEqual(skill.read_bytes(), (SKILLS / 'drums-signature' / 'SKILL.md').read_bytes())

    def test_producer_pal_ajoute_sans_ecraser(self):
        reglages = self.home / '.qwen' / 'settings.json'
        reglages.write_text(json.dumps({'model': {'name': 'qwen3-coder-plus'}}))
        r = installer(self.home, '--producer-pal-qwen', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(reglages.read_text())
        self.assertEqual(data['model'], {'name': 'qwen3-coder-plus'})
        self.assertEqual(data['mcpServers']['producer-pal']['command'], 'npx')
        self.assertIn('déjà déclaré', installer(self.home, '--producer-pal-qwen', '--appliquer').stdout)

    def test_skill_inconnu_refuse(self):
        r = installer(self.home, '--skill', 'nexiste-pas')
        self.assertEqual(r.returncode, 2)


class Verificateur(unittest.TestCase):
    def test_depot_propre(self):
        r = subprocess.run([sys.executable, str(OUTILS / 'verifier_skills.py')], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_qwen_voit_les_memes_skills(self):
        lien = DEPOT / '.qwen' / 'skills'
        self.assertTrue(lien.is_symlink())
        self.assertEqual(sorted(p.name for p in lien.iterdir()), sorted(p.name for p in SKILLS.iterdir()))


if __name__ == '__main__':
    unittest.main()
