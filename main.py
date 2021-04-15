"""

Pour commencer, le format des fichiers .osu des maps ressemble à ça: (ici la version 14)

'
osu file format v14

[General] # Inutile pour notre problème
AudioFilename: machin.mp3                   # Nom du fichier audio de la map
SampleSet: Soft                             # Le pack audio du skin qui sera utilisé pour les hitsound de la map
etc

[Editor] # Inutile pour notre problème
DistanceSpacing: 1                          # Défini la distance de déplacement de la prochaine note selon le temps écoulé depuis la dernière note. Pour l'utilisation de l'éditeur
BeatDivisor: 4                              # C'est le diviseur de temps dans l'editeur. Pour faire simple, 4 battements du metronome valent une mesure. Pour les musiciens qui ont besoin de ces outils pour mieux utiliser l'éditeur
GridSize: 16                                # 4, 8, 16, 32, c'est la distance entre chaques points de la grille d'édition. Il sert à l'utilisation de l'editeur
TimelineZoom: 2.4                           # Paramètre qui sauvegarde le zoom dans l'editeur

[Metadata] # Inutile pour notre problème
Title: machin                               # Titre de la musique
TitleUnicode: 銀閃の風                       # Titre de la musique original (titres en japonais par exemple)
etc

[Difficulty]
HPDrainRate:7                               # Quantité de vie que l'on perd dans le temps et quand on rate une note
CircleSize:4                                # Taille des notes
OverallDifficulty:9                         # Marge d'erreur. Par exemple si la note est à la position 100ms, si on la touche entre 50ms et 150ms on récupère quand même la note (en gros, c'est la fourchette de validation)
ApproachRate:9                              # Temps que les notes restes à l'écran. Plus c'est haut, moins de temps les notes restent à l'écran
SliderMultiplier:1.8                        # Vitesse des slider
SliderTickRate:1                            # Densité des points intermédiaires d'un slider

[Events] # Inutile pour notre problème
# Tout ce qui est lié au storyboard donc les images de fond, les effets visuels, les vidéos, etc

[TimingPoints] # Inutile pour notre problème
# Sert pour l'éditeur puisqu'il permet de mettre à jour le status du bpm, du volume de la musique, des pack de hitsounds, etc mais une foit les cercles positionnés, la map ne change pas selon ces paramètres (pour sa partie "gameplay")
1417,337.078651685393,4,2,3,50,1,0
12203,-100,4,2,10,50,0,0
12709,-100,4,2,3,50,0,0
22990,-100,4,2,2,70,0,0
etc

# format utilisé: Offset, Speed, BeatDivisor, SampleSet, ModificationDuPackHitSound, Volume, Heritage, Kiai

# Offset: poistion dans le temps
# Speed: vitesse des sliders
# BeatDivisor: Modification du BeatDivisor
# SampleSet: 1 pour le HitSound "Normal", 2 pour le HitSound "Soft" et 3 pour le HitSound "Drum"
# ModificationDuPackHitSound: Applique des effets aux HitSounds selon la valeur sélectionnée
# Volume: Défini le volume des HitSounds (et/ou de la musique ?) à partir de l'Offset. Valeurs en %
# Heritage: hérite (0) ou pas (1) de la speed du dernier point qui le défini en brute
# Kiai: Défini si c'est la partie refrain ou pas

# Donc, selon l'héritage on a deux pattern:
#   - Heritage: 1, Speed: BPM * SliderMultiplier
#   - Heritage: 0, Speed: -Variation (SpeedHéritée*Variation/100 ou du moins une formule du genre)
# Chaque fois la première ligne sera donc le premier cas puis il n'y a plus de restrictions après

[Colours] # Inutile pour notre problème
Combo1 : 150,150,150
Combo2 : 244,174,11
Combo3 : 27,9,193
Combo4 : 230,40,13

[HitObjects] # Voila ce qui nous intéresse
72,192,329,5,4,0:0:0:0:
360,192,716,2,0,L|464:192,2,90,0|2|0,0:0|0:0|0:0,0:0:0:0:
72,192,1296,1,0,0:0:0:0:
304,160,1877,5,2,0:0:0:0:
128,160,2264,2,0,L|24:160,2,90,0|0|0,0:0|0:0|0:0,0:0:0:0:
480,160,2845,1,2,0:0:0:0:
176,224,3425,5,2,0:0:0:0:
etc

# formats utilisés:
#   - Circle: x, y, Offset, A, B, HitSound (?:?:?:? les ? étants les 1/2/3 de SampleSet cité plus haut)
#   - Slider: x, y, Offset, A, B, ListePointsBezier, C, DureeSlider, HitSoundOptionnel
#   - Spinner: x, y, Offset, A, B, OffsetFin, HitSound (?:?:?:?)

# x, y: Coordonnées sur la grille
# Offset: cf TimingPoint
# A: Inconnu
# B: Inconnu
# HitSound: Défini les HitSound de la note sous différentes forme, dans la suite 1:3:0:0 le 1 dit qu'il s'agit du son principal "Normal" auquel on ajoute grace au 3 le son secondaire "Drum". Les deux à la fin je nai pas trouvé à quoi ils servent
# ListePointsBezier: Il s'agit d'une liste qui contient tous les points (en dehors du point initial donnée par x,y,Offset) pour produire la courbe de Bezier du slider.
#                    Voici les 2 formats de cette liste:
#                       - L|x:y Le L semble vouloir dire "Linear" mais semble apparaitre que pour 1 seul point dans la liste. Avec une liste à 2 points dont j'ai forcé la linéarité, c'est quand même passé au second format
#                       - P|x1:y1|...|xn:yn Le P semble vouloir dire "Polygonal"
# DureeSlider: Défini le temps (même unité de temps que le Offset) que dure le slider
# C: Inconnu
# HitSoundOptionnel:  Même format que pour HitSound sauf que l'on ajoute une liste avant sous la forme: 0:0|...|0:0 qui correspondent respectivement aux points dans ListPointBezier
'

"""