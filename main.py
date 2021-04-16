"""
Étapes d'entrainement:
    - Ouvrir les maps d'entrainement avec leur target et les formater
    - Mettre bout à bout les points de toutes les maps pour faire une map qui contient un maximum de patterns
(A) - Entrainer un algorithme de Classification non supervisé de Time Series pour déterminer les différents patterns
(A) - Pour chaque map, prédire les patterns avec l'algorithme
    - Pour chaque prédiction, formater le résultat pour créer un dataset
(B) - Entrainer un algorithme de Classification supervisé pour déterminer le type de maps (tech, speed, jump, etc)
(B) - Analyse de performance de l'algorithme

Étapes d'utilisation après l'entrainement:
    - Ouvrir la maps à analyser sans sa target et la formater
(A) - Prédire les patterns pour mettre à jour les infos de la map
(B) - Prédire le type de map (Résultat final)

"""