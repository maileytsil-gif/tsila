# Diagnostic et recettes de mixage

## Trois tests avant tout plugin

1. **Mute** : enlever la source suspecte en contexte; si le problème disparaît, ajuster son rôle et sa durée.
2. **Niveau** : monter/descendre la source à volume comparable au résultat traité; un traitement plus fort paraît souvent meilleur à tort.
3. **Section et mono** : comparer le moment problématique au passage précédent, puis en mono et sur deux systèmes. Ne régler que le problème observé.

## Recette A — Kick/sub sur un drop house

Écouter kick seul, sub seul, puis ensemble à volume modéré; noter hauteur perçue, durée et collision de transitoires. Si deux notes de basse se succèdent sur le kick, raccourcir d'abord leur release. Si un conflit persiste : Compressor déjà en place (toléré par la règle 6), sinon Pro-C 3 (à prober) ou API-2500 sur sub, sidechain externe venant du kick, attack courte comme point de départ, release choisie au tempo et à l'oreille, ratio modéré; ajuster le seuil selon la réduction audible souhaitée et relire le premier temps. Variante plus précise : Pro-Q 4 avec bande dynamique externe sur une zone de conflit mesurée, si le conflit se limite à une partie du spectre. Le ducking ne doit pas couvrir une erreur de phase, de notes ou de routage. Écouter en mono et avec/sans sidechain. Voir [FabFilter, sidechain externe Pro-C 3](https://www.fabfilter.com/help/pro-c/support/externalsidechaining) et [Ableton, référence des effets audio](https://www.ableton.com/en/manual/live-audio-effect-reference/).

## Recette B — Bass House, bass mid qui disparaît

Mettre kick + sub + snare + bass mid en boucle; désactiver l'élargisseur et la reverb du bass mid. Vérifier que ses attaques ne tombent pas toujours sous kick/snare; raccourcir les notes ou placer une réponse entre les coups. Ajouter une légère saturation harmonique seulement si les petits haut-parleurs ne reproduisent pas le motif; comparer à volume égal et garder le sub sur sa piste séparée. Si une résonance gêne uniquement certaines syllabes, essayer une bande dynamique peu profonde dans Pro-Q 4 ou un traitement sélectif; ne pas sculpter un « trou » fixe sur tout le bus sans entendre la collision. Varier deux timbres en appel-réponse plutôt que les additionner en permanence.

## Recette C — Future Rave, lead large + voix

Écouter refrain avec uniquement voix, lead sec, kick/sub; repérer les mots masqués. Essayer dans cet ordre : baisser le lead pendant la première syllabe, changer son voicing/registre, raccourcir sa release, filtrer sa reverb sur un retour, puis EQ dynamique sur le lead déclenchée par la voix si nécessaire. Garder la voix directe assez nette; automatiser les envois de delay/reverb dans les fins de phrases. Si la grande reverb recouvre le kick, ducker **le retour de reverb** plutôt que la voix entière. Comparer A/B à niveau égal; vérifier que la largeur n'annule pas la mélodie en mono.

## Recette D — Tech House, groove des hats sans aigus douloureux

Distinguer hats fermés, hats ouverts, clap et noise FX; écouter à faible niveau 16 mesures. Couper ou diminuer l'élément qui rend chaque contretemps identique. Ajuster vélocités, longueur et attaque avant une EQ radicale. Si dureté localisée : trouver le passage offensant en solo puis en contexte, essayer une correction dynamique modérée ou un de-esser; valider sur le drop et le break. Panoramiquer les percussions de soutien, conserver clap et pulsation forts comme ancrage.

## Recette E — Minimal, espace et micro-événements

Commencer kick + basse + un seul élément repère. N'ajouter une texture que si son retrait est perceptible en contexte; moduler son panoramique ou la profondeur avec parcimonie, garder son énergie grave contrôlée. Faire deux versions de 16 mesures : avec percussion supplémentaire et sans; préférer celle où la phrase et la tension se lisent le mieux. Dans un passage peu dense, même une petite résonance ou un click de sample devient audible : éditer fondus et fins de loops.

## Recette F — Break, riser, impact et retour

Comparer dernière mesure du break, silence éventuel et quatre premiers kicks du drop. Sur les retours d'effets du break, automatiser volume, filtres et coupe de queue; sur l'impact, séparer attaque/noise/corps tonal. Si kick + corps grave perdent de l'énergie en mono, réduire le corps de l'impact ou son overlap. Préparer trois options A/B : sans impact; attaque seule; attaque + air. Préserver une version où le premier temps respire.

## Recette G — Analyse spectrale et vectorielle honnête

Dans Live, Utility mono et SPAN (Spectrum serait un nouveau natif, règle 6) pour inspecter des passages identiques à niveau égal. Pour chaque section, consigner : crête, RMS court ou autre métrique disponible, contenu sub/bas médium, attaque du kick, énergie Mid/Side par bande, corrélation et forme du vectorscope si l'instrument de mesure existe. Noter la durée des mesures et le calibrage du meter. Une image ou un nombre ne démontre pas à lui seul la qualité du mix; valider par écoute en mono et stéréo. Attention à la latence ou au traitement de phase lorsque des bus parallèles se combinent : contrôler leur addition avant de compenser au hasard.

## Ordre de contrôle final et livraison

- Vérifier que la référence n'est pas traitée par la chaîne master du projet; comparer à niveau raisonnablement proche et sur des passages de même fonction.
- Écouter début, fin, transitions, plus forte section, passage le plus calme; supprimer clicks et queues coupées involontaires.
- Vérifier les bus, effets de retour et sorties Maschine pour éviter un double routage ou un écrêtage masqué par le limiteur.
- Exporter dans le format demandé par le destinataire, conserver une version du mix sans limitation supplémentaire, inspecter le fichier **exporté** dans un nouveau projet ou lecteur.
- Pour stems : définir précisément l'inclusion des reverbs, delays et traitements de bus; vérifier que leur somme correspond approximativement au mix attendu et que les départs/longueurs sont alignés.
- Ne pas annoncer « prêt pour label » uniquement sur une mesure LUFS : arrangement, tonalité, balance, transitoires, mono, finitions et exigences du destinataire restent à contrôler.
