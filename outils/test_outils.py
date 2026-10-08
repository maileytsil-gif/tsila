"""Tests hors Mac de outils/installer.sh et outils/verifier_skills.py (HOME temporaire, aucun fichier personnel touché).

  python3 -m unittest discover -s outils -p 'test_*.py' -v
"""
import json
import os
import shutil
import pathlib
import subprocess
import sys
import tempfile
import unittest

OUTILS = pathlib.Path(__file__).resolve().parent
DEPOT = OUTILS.parent
SKILLS = DEPOT / '.claude' / 'skills'
PETIT = 'ingenieur-mixage'  # skill copié dans les tests
SIGNATURE = 'producteur-rythmique/modules/drums-signature/scripts/signature.json'


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
        r = installer(self.home, '--skill', PETIT)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('SIMULATION', r.stdout)
        self.assertFalse((self.home / '.claude' / 'skills').exists())
        self.assertFalse((self.home / '.qwen' / 'skills').exists())

    def test_claude_copie_qwen_relie(self):
        r = installer(self.home, '--skill', PETIT, '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        copie = self.home / '.claude' / 'skills' / PETIT
        lien = self.home / '.qwen' / 'skills' / PETIT
        self.assertEqual((copie / 'SKILL.md').read_bytes(), (SKILLS / PETIT / 'SKILL.md').read_bytes())
        self.assertTrue((copie / 'modules' / 'mixage' / 'GUIDE.md').is_file())  # les modules suivent le skill
        self.assertTrue(lien.is_symlink())
        self.assertEqual(lien.resolve(), copie.resolve())
        again = installer(self.home, '--skill', PETIT, '--appliquer')
        self.assertIn('Rien à changer', again.stdout)

    def test_ancienne_version_sauvegardee_hors_des_skills(self):
        ancien = self.home / '.qwen' / 'skills' / PETIT
        ancien.mkdir(parents=True)
        (ancien / 'SKILL.md').write_text(f'---\nname: {PETIT}\ndescription: ancienne\n---\n')
        r = installer(self.home, '--skill', PETIT, '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        sauvegardes = list((self.home / '.skills-sauvegardes').glob(f'*/qwen/{PETIT}/SKILL.md'))
        self.assertEqual(len(sauvegardes), 1)
        self.assertIn('ancienne', sauvegardes[0].read_text())
        self.assertTrue((self.home / '.qwen' / 'skills' / PETIT).is_symlink())

    def test_registre_de_signature_conserve(self):
        installer(self.home, '--claude', '--skill', 'producteur-rythmique', '--appliquer')
        registre = self.home / '.claude' / 'skills' / SIGNATURE
        registre.write_text('{"kick": "valide par l utilisateur"}')
        skill = self.home / '.claude' / 'skills' / 'producteur-rythmique' / 'SKILL.md'
        skill.write_text(skill.read_text() + '\nmodification locale\n')
        r = installer(self.home, '--claude', '--skill', 'producteur-rythmique', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(registre.read_text(), '{"kick": "valide par l utilisateur"}')
        self.assertEqual(skill.read_bytes(), (SKILLS / 'producteur-rythmique' / 'SKILL.md').read_bytes())

    def test_retirer_absents_sauvegarde_les_anciens_skills(self):
        installer(self.home, '--skill', PETIT, '--appliquer')
        ancien = self.home / '.claude' / 'skills' / 'resampling'  # un des 44 anciens skills, encore installé
        ancien.mkdir()
        (ancien / 'SKILL.md').write_text('---\nname: resampling\ndescription: ancien\n---\n')
        (self.home / '.qwen' / 'skills' / 'resampling').symlink_to(ancien)
        simulation = installer(self.home, '--retirer-absents')
        self.assertEqual(simulation.returncode, 0, simulation.stderr)
        self.assertIn("resampling n'est plus dans le dépôt", simulation.stdout)
        self.assertTrue(ancien.is_dir())
        r = installer(self.home, '--retirer-absents', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertFalse(ancien.exists())
        self.assertFalse((self.home / '.qwen' / 'skills' / 'resampling').is_symlink())
        self.assertEqual(len(list((self.home / '.skills-sauvegardes').glob('*/claude/resampling/SKILL.md'))), 1)
        self.assertEqual(len(list((self.home / '.skills-sauvegardes').glob('*/qwen/resampling'))), 1)
        self.assertTrue((self.home / '.claude' / 'skills' / PETIT / 'SKILL.md').is_file())
        self.assertTrue((self.home / '.qwen' / 'skills' / PETIT).is_symlink())

    def test_producer_pal_ajoute_sans_ecraser(self):
        reglages = self.home / '.qwen' / 'settings.json'
        reglages.write_text(json.dumps({'model': {'name': 'qwen3-coder-plus'}}))
        r = installer(self.home, '--producer-pal-qwen', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        data = json.loads(reglages.read_text())
        self.assertEqual(data['model'], {'name': 'qwen3-coder-plus'})
        self.assertEqual(data['mcpServers']['producer-pal']['command'], 'npx')
        self.assertIn('déjà déclaré', installer(self.home, '--producer-pal-qwen', '--appliquer').stdout)

    def test_producer_pal_json_commente_refuse_sans_ecrire(self):
        reglages = self.home / '.qwen' / 'settings.json'
        texte = '{\n  // réglages de l utilisateur\n  "model": {"name": "qwen3"}\n}\n'
        reglages.write_text(texte)
        r = installer(self.home, '--producer-pal-qwen', '--appliquer')
        self.assertNotEqual(r.returncode, 0)
        self.assertIn('JSON strict', r.stderr)
        self.assertNotIn('Traceback', r.stderr)
        self.assertEqual(reglages.read_text(), texte)

    def test_producer_pal_mcpservers_null(self):
        reglages = self.home / '.qwen' / 'settings.json'
        reglages.write_text('{"mcpServers": null}')
        r = installer(self.home, '--producer-pal-qwen', '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('producer-pal', json.loads(reglages.read_text())['mcpServers'])

    def test_qwen_skills_deja_lien_vers_claude(self):
        installer(self.home, '--claude', '--skill', PETIT, '--appliquer')
        (self.home / '.qwen' / 'skills').symlink_to(self.home / '.claude' / 'skills')
        r = installer(self.home, '--qwen', '--skill', PETIT, '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('déjà partagé', r.stdout)
        copie = self.home / '.claude' / 'skills' / PETIT
        self.assertTrue(copie.is_dir() and not copie.is_symlink())
        self.assertEqual((copie / 'SKILL.md').read_bytes(), (SKILLS / PETIT / 'SKILL.md').read_bytes())
        self.assertFalse((self.home / '.skills-sauvegardes').exists())

    def test_qwen_skills_lien_ailleurs_laisse_tel_quel(self):
        ailleurs = self.home / 'ailleurs'
        (ailleurs / PETIT).mkdir(parents=True)
        (ailleurs / PETIT / 'SKILL.md').write_text('à moi')
        (self.home / '.qwen' / 'skills').symlink_to(ailleurs)
        r = installer(self.home, '--qwen', '--skill', PETIT, '--appliquer')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('laissé tel quel', r.stderr)
        self.assertEqual((ailleurs / PETIT / 'SKILL.md').read_text(), 'à moi')

    def test_claude_skills_lien_vers_le_depot_ne_touche_pas_au_depot(self):
        # Sur une copie du dépôt : le vrai dépôt n'est jamais exposé à ce cas.
        depot = self.home / 'depot'
        shutil.copytree(OUTILS, depot / 'outils', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(SKILLS / PETIT, depot / '.claude' / 'skills' / PETIT)
        (self.home / '.claude' / 'skills').symlink_to(depot / '.claude' / 'skills')
        env = dict(os.environ, HOME=str(self.home))
        r = subprocess.run(['bash', str(depot / 'outils' / 'installer.sh'), '--claude', '--qwen', '--appliquer'],
                           env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('dossier du dépôt lui-même', r.stdout)
        source = depot / '.claude' / 'skills' / PETIT
        self.assertTrue(source.is_dir() and not source.is_symlink())
        self.assertFalse((self.home / '.skills-sauvegardes').exists())
        self.assertEqual((self.home / '.qwen' / 'skills' / PETIT).resolve(), source.resolve())

    def test_skill_inconnu_refuse(self):
        r = installer(self.home, '--skill', 'nexiste-pas')
        self.assertEqual(r.returncode, 2)
        r = installer(self.home, '--skill', 'resampling')  # un module n'est pas un skill
        self.assertEqual(r.returncode, 2)


class Verificateur(unittest.TestCase):
    def test_depot_propre(self):
        r = subprocess.run([sys.executable, str(OUTILS / 'verifier_skills.py')], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_qwen_voit_les_memes_skills(self):
        lien = DEPOT / '.qwen' / 'skills'
        self.assertTrue(lien.is_symlink())
        self.assertEqual(sorted(p.name for p in lien.iterdir()), sorted(p.name for p in SKILLS.iterdir()))

    def test_un_seul_skill_md_par_skill(self):
        for skill in SKILLS.iterdir():
            if skill.is_dir():
                self.assertEqual([f for f in skill.rglob('SKILL.md')], [skill / 'SKILL.md'], skill.name)

    def _copie(self):
        """Copie du dépôt (skills, outils, bridge, fichiers racine, .qwen) : les liens cassés s'injectent là, jamais dans le dépôt."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        depot = pathlib.Path(tmp.name) / 'depot'
        sans_cache = shutil.ignore_patterns('__pycache__')
        shutil.copytree(SKILLS, depot / '.claude' / 'skills', symlinks=True, ignore=sans_cache)
        shutil.copytree(OUTILS, depot / 'outils', ignore=sans_cache)
        shutil.copytree(DEPOT / 'lom-bridge', depot / 'lom-bridge', ignore=sans_cache)
        shutil.copytree(DEPOT / 'docs', depot / 'docs', ignore=sans_cache)
        for nom in ('AGENTS.md', 'CLAUDE.md', 'QWEN.md', 'README.md'):
            shutil.copy2(DEPOT / nom, depot / nom)
        (depot / '.qwen').mkdir()
        shutil.copy2(DEPOT / '.qwen' / 'settings.json', depot / '.qwen' / 'settings.json')
        (depot / '.qwen' / 'skills').symlink_to('../.claude/skills')
        return depot

    def _verifier(self, depot):
        return subprocess.run([sys.executable, '-B', str(depot / 'outils' / 'verifier_skills.py')],
                              capture_output=True, text=True)

    def _erreurs(self, sortie, motif):
        return [l for l in sortie.splitlines() if l.startswith('ERREUR') and motif in l]

    def test_chemin_suivi_d_arguments(self):
        depot = self._copie()
        module = depot / '.claude' / 'skills' / 'sound-designer-serum' / 'modules' / 'resampling'
        (module / 'essai-liens.md').write_text(
            'Lancer `python3 scripts/absent.py --verifier references/*.md`.\n'
            'Mesurer : `../../../producteur-rythmique/modules/kick-bass-equilibre/scripts/absent_check.py kick.wav sub.wav`.\n'
            'Voir `lire ../module-absent/GUIDE.md` ; valides : `python3 ../../../producteur-rythmique/modules/kick-bass-equilibre/scripts/kick_bass_check.py kick.wav sub.wav`, `../../SKILL.md`, `../synthese-reference/GUIDE.md`.\n',
            encoding='utf-8')
        r = self._verifier(depot)
        self.assertEqual(r.returncode, 1, r.stdout)
        erreurs = self._erreurs(r.stdout, 'essai-liens.md')
        self.assertEqual(len(erreurs), 3, r.stdout)
        for n, cible in ((1, 'scripts/absent.py'),
                         (2, '../../../producteur-rythmique/modules/kick-bass-equilibre/scripts/absent_check.py'),
                         (3, '../module-absent/GUIDE.md')):
            self.assertIn(f'essai-liens.md:{n} : chemin introuvable « {cible} »', r.stdout)

    def test_chemin_relatif_au_dossier_des_skills(self):
        depot = self._copie()
        (depot / '.claude' / 'skills' / 'sound-designer-serum' / 'modules' / 'resampling' / 'essai-liens.md').write_text(
            'Moteur : `sound-designer-serum/references/moteurs-synthese.md`, '
            'kit : `producteur-rythmique/modules/drums-signature/references/sons.md`.\n'
            'Absent : `sound-designer-serum/references/absent.md`.\n', encoding='utf-8')
        r = self._verifier(depot)
        self.assertEqual(self._erreurs(r.stdout, 'essai-liens.md'),
                         ['ERREUR .claude/skills/sound-designer-serum/modules/resampling/essai-liens.md:2 : chemin introuvable '
                          '« sound-designer-serum/references/absent.md »'], r.stdout)

    def test_chemin_relatif_a_la_racine_du_depot(self):
        depot = self._copie()
        (depot / 'corpus' / 'scripts').mkdir(parents=True)
        (depot / 'corpus' / 'scripts' / 'present.py').write_text('', encoding='utf-8')
        (depot / '.claude' / 'skills' / 'sound-designer-serum' / 'modules' / 'resampling' / 'essai-liens.md').write_text(
            'Sur le Mac : `python3 corpus/scripts/present.py --dossier x`.\n'
            'Absent : `python3 corpus/scripts/absent.py`.\n', encoding='utf-8')
        r = self._verifier(depot)
        self.assertEqual(self._erreurs(r.stdout, 'essai-liens.md'),
                         ['ERREUR .claude/skills/sound-designer-serum/modules/resampling/essai-liens.md:2 : chemin introuvable '
                          '« corpus/scripts/absent.py »'], r.stdout)

    def test_fichiers_racine_scannes(self):
        depot = self._copie()
        readme = depot / 'README.md'
        texte = readme.read_text(encoding='utf-8').rstrip('\n')
        n = len(texte.splitlines())
        readme.write_text(texte + '\n\n- `lom-bridge/absent.py` et `outils/absent.sh`\n'
                          '- `python3 compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/absent.py --verifier`\n'
                          '- valides ou hors dépôt : `python3 lom-bridge/agent_gateway.py inspect /ping`, `~/.qwen/absent`, '
                          '`drums-signature` (`references/signature.md`)\n',
                          encoding='utf-8')
        r = self._verifier(depot)
        self.assertEqual(r.returncode, 1, r.stdout)
        for ligne, cible in ((n + 2, 'lom-bridge/absent.py'), (n + 2, 'outils/absent.sh'),
                             (n + 3, 'compositeur-arrangeur/modules/composer-hooks-funk-electro/scripts/absent.py')):
            self.assertIn(f'README.md:{ligne} : chemin introuvable « {cible} »', r.stdout)
        self.assertNotIn(f'README.md:{n + 4} :', r.stdout)

    def test_skill_md_sous_modules_refuse(self):
        depot = self._copie()
        module = depot / '.claude' / 'skills' / 'ingenieur-mixage' / 'modules' / 'mixage'
        (module / 'SKILL.md').write_text('---\nname: mixage\ndescription: x\n---\n# Mixage\n', encoding='utf-8')
        r = self._verifier(depot)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertEqual(len(self._erreurs(r.stdout, 'hors de la racine du skill')), 1, r.stdout)

    def test_module_sans_guide_ou_non_cite(self):
        depot = self._copie()
        nouveau = depot / '.claude' / 'skills' / 'ingenieur-mixage' / 'modules' / 'nouveau-module'
        nouveau.mkdir()
        r = self._verifier(depot)
        self.assertIn('ERREUR ingenieur-mixage/modules/nouveau-module : GUIDE.md absent', r.stdout)
        self.assertIn('ERREUR ingenieur-mixage/SKILL.md : le module « nouveau-module » n\'y est pas cité', r.stdout)
        self.assertIn('ERREUR producteur-live/SKILL.md : « nouveau-module » n\'apparaît pas dans la carte', r.stdout)


if __name__ == '__main__':
    unittest.main()
