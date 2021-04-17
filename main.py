import os

from src.converters import convert_element
from src.fileParser import parse_file

"""
Étapes d'entrainement:
    - Ouvrir les maps d'entrainement avec leur target et les formater
    - Mettre bout à bout les points de toutes les maps pour faire une map qui contient un maximum de patterns
(A) - Entrainer un algorithme de Clustering de Time Series pour déterminer les différents patterns
(A) - Pour chaque map, prédire les patterns avec l'algorithme
    - Pour chaque prédiction, formater le résultat pour créer un dataset
(B) - Entrainer un algorithme de Classification pour déterminer le type de maps (tech, speed, jump, etc)
(B) - Analyse de performance de l'algorithme

Étapes d'utilisation après l'entrainement:
    - Ouvrir la maps à analyser sans sa target et la formater
(A) - Prédire les patterns pour mettre à jour les infos de la map
(B) - Prédire le type de map (Résultat final)

"""


def print_format(format):
    print(format['FileName'], ":")
    for key in format:
        if "elements" not in key:
            print("\t-", key, ":", format[key])
        else:
            print("\t-", key, ":")
            for i in format[key]:
                print("\t\t-", i)


train_folder = "./maps/train/"

# On récupère les maps d'entrainement
train_files = []
for root, directories, files in os.walk(train_folder):
    # Uniquement les fichiers dans train_folder (ignore les sous-dossiers) qui sont au format .osu
    if root in train_folder:
        for file in files:
            if file.endswith(".osu"):
                train_files.append(file)

# On format toutes les maps
train_formats = []
for file in train_files:
    train_formats.append(parse_file(train_folder + file))

# Affichage des maps formatées
for map_format in train_formats:
    print_format(map_format)

print()
circles = []
for e in train_formats[0]['elements']:
    for c in convert_element(e):
        circles.append(c)

for c in circles:
    print(c)
