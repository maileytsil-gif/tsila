# Automation, modulation et contrôle temps réel

## Live : automation vs modulation [DOC]

Ableton distingue l'**automation** (valeur/trajectoire absolue du paramètre) et la **modulation** (variation relative autour d'un état selon le contexte). Les Clip Envelopes n'ont pas exactement le même rôle en Session et Arrangement : le bridge doit savoir dans quel contexte il écrit.

Source : https://www.ableton.com/en/manual/clip-envelopes/

## Max for Live Device Parameters [DOC]

Les paramètres M4L possèdent des propriétés liées au stockage, à l'automation et au mode de modulation. Concevoir un device nécessite de décider ce qui doit être automatisable/stored plutôt que d'exposer arbitrairement tout.

Source : https://docs.cycling74.com/userguide/m4l/device_parameters/

## `live.remote~` [DOC]

`live.remote~` permet un contrôle temps réel d'un DeviceParameter, avec comportement prévu pour le domaine audio/signal. Points critiques :
- il prend le contrôle de la cible tant qu'il est attaché ;
- une latence d'au moins un buffer audio est documentée selon le contexte ;
- la valeur pilotée n'est pas à considérer comme une valeur Set stockée/undoable ;
- affecter l'id 0 libère le contrôle ;
- il ne faut pas utiliser ce mécanisme comme substitut invisible à une automation persistante.

Source : https://docs.cycling74.com/reference/live.remote~/

## Trois preuves différentes

- **set_value proof** : valeur modifiée puis relue.
- **realtime proof** : courbe reçue et paramètre contrôlé pendant le transport, puis correctement relâché.
- **automation proof** : enveloppe éditable/stokée visible ou relue via une méthode supportée, et persistance vérifiée si nécessaire.

Ne jamais déduire une preuve des deux autres.
