# Contrôle des VST/AU dans Ableton

## Paramètres publiés [DOC]

Ableton permet de configurer des paramètres de plug-in que celui-ci **publie à l'hôte**. Certains plug-ins n'exposent pas tous les contrôles de leur interface, et une configuration de paramètres concerne l'instance/usage dans Live.

Source : https://www.ableton.com/en/live-manual/12/working-with-instruments-and-effects/

## Stratégie robuste

1. Inspecter le format réel de l'instance : VST3/AU/etc.
2. Enumerer les paramètres visibles/configurables dans Live.
3. Ne pas utiliser l'index seul comme identité persistante ; stocker nom/signature et vérifier l'index courant.
4. Pour un synthé complexe, créer un Instrument Rack et mapper les paramètres musicaux importants sur quelques macros stables.
5. Le bridge pilote les macros ; le preset interne garde la complexité.

## Serum 2

Un bridge LOM n'est pas automatiquement un éditeur complet de l'interface Serum 2. Édition de wavetable, dessin de LFO, menus contextuels ou contrôles non publiés ne sont pas acquis par le simple fait que Serum est chargé dans Live.

Statut par défaut : **[TEST]** pour chaque paramètre Serum voulu. Faire discovery sur l'instance installée.

## Fallbacks

Si un paramètre n'est pas publié :
- mapper une macro depuis l'interface/host si possible ;
- modifier le preset manuellement puis exposer un macro-contract ;
- n'utiliser une automatisation GUI/computer-control que si l'outil autorisé existe et que l'utilisateur en accepte la fragilité. Ne pas présenter un fallback GUI comme une capacité LOM.
