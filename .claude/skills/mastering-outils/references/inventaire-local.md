# Outils repérés sur le Mac d'origine

Lecture des Info.plist VST3 le 14 septembre 2026, sous `/Library/Audio/Plug-Ins/VST3/`. Cette liste est un instantané de fichiers présents : activation, chargement dans Ableton et contrôle à distance n'ont pas été testés lors de la création du skill.

| Outil | Version repérée | Rôle à examiner |
|---|---|---|
| FabFilter Pro-Q 4 | 4.10 | EQ statique, dynamique et spectrale |
| FabFilter Pro-C 3 | 3.00 | Compression |
| Ozone 12 Elements | 12.1.0 | Mastering assisté selon les commandes de cette édition |
| Ozone 11 Elements | 11.3.0 | Ancienne édition présente ; conserver si le projet la nécessite |
| Ozone 11 Equalizer | 11.3.0 | Égalisation |
| Insight 2 | 2.6.0 | Sonie, crêtes et analyse du champ stéréo |
| Tonal Balance Control 3 | 3.1.1 | Comparaison d'équilibre tonal selon l'interface disponible |
| Ozone Imager 2 | 2.3.0 | Largeur et contrôle de l'image stéréo |
| SPAN | 3.23 | Spectre et corrélation |
| TDR Nova | 2.2.2 | EQ dynamique |
| soothe3 | 1.0.5 | Réduction de résonances selon le besoin |
| bx_glue | 1.1.0 | Compression de bus et couleur |
| RazorClip | 1.0.0 | Bundle repéré ; lire son éditeur et son manuel avant de supposer ses fonctions |

## Waves Audio : bundles individuels repérés

Une vérification complémentaire a trouvé les bundles suivants dans `/Applications/Waves/Plug-Ins V16/` ET `/Applications/Waves/Plug-Ins V17/` :

| Fonction à examiner | Bundles repérés |
|---|---|
| Limitation | L1, L2, L3 Multi, L3 Ultra, L3-16, L3-LL Multi, L3-LL Ultra, L4 Ultramaximizer |
| Mesure | WLM, WLM Plus, PAZ |
| Chaîne de mastering | Abbey Road TG Mastering Chain |
| EQ et correction | F6, Q10, LinEQ, Curves AQ, Curves Equator, Curves Resolve, PuigTec |
| Dynamique | API-2500, SSLComp, LinMB, C4, C6, PuigChild, VComp |
| Couleur | J37, KramerTape, Abbey Road Saturator, Abbey Road Vinyl |
| Stéréo | S1, Center |
| Autres traitements | Vitamin, MaxxBass, MaxxVolume |

Ces noms sont ceux des fichiers `.bundle` ; les libellés des composants dans l'hôte peuvent différer. V16/V17 désignent ici les dossiers : vérifier la version chargée et la licence avant usage. Cette lecture ne valide pas le fonctionnement de tous ces plug-ins. Leurs fiches sont dans [waves-mastering.md](waves-mastering.md).

Pro-L et Pro-MB n'ont pas été repérés lors de cette recherche dans les dossiers audio standard ; cela ne démontre pas leur absence dans tous les emplacements. Ne pas les annoncer comme installés, ni suggérer un achat avant d'identifier le besoin et les options disponibles.

L'exposition des paramètres peut varier avec le format du plug-in, sa version et la configuration de l'hôte. La présence d'un seul paramètre de marche/arrêt ne prouve pas une impossibilité totale de pilotage : vérifier la configuration de paramètres et l'interface, sans remplacer l'instance réglée pour ce simple test.
