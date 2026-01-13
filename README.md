# INTRODUCTION

Cet outil permet de faciliter la création de proxys de carte Magic.

## INSTALLATION

1. Installer Python 3
2. Installer les modules pillow et requests
   - `python -m pip install requests`
   - `python -m pip install pillow`

## UTILISATION

Le lancement de l'outil se fait en exécutant le main : `python main.py`.

une fois le logiciel lancé, plusieurs options sont possibles :

1. Option de téléchargement, depuis un fichier contenant le nom des cartes à imprimer, une par ligne.
Ce fichier peut également contenir les quantités des cartes, tous les caractères numériques sont ignorés.
Moi-même j'utilise l'export de https://archidekt.com/.

2. Option de mise à jour.
Cette option est là dans le cas d'une mise à jour d'une decklist.
Donner l'ancien fichier et le nouveau fichier : 
l'outil se charge d'en sortir les nouvelles cartes

3. Option de tri des images des cartes.
Cette option permet de collecter l'ensemble des .png d'un dossier et de les ranger dans des sous-dossier par paquet de 9.

4. Option de création des images à imprimer.
Depuis un dossier contenant 9 images téléchargées depuis l'API scryfall,
l'outil redimmensionne ces images et les places dans une seule et même image au format A4, prête pour l'impression.
