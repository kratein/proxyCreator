# INTRODUCTION

Cet outil permet de créer facilement des proxy magic à partir d'une liste de nom de cartes

# REQUIREMENTS

L'accès à https://api.scryfall.com est obligatoire pour récupérer les images des cartes à imprimer 

# OPTIONS
- 1. Depuis un fichier contenant le nom des cartes à imprimer, une par ligne.
  -  ce fichier peut également contenir les quantités des cartes, tous les caractères numériques sont ignorés
  -  moi même j'utilise l'export de https://archidekt.com/
- 2. Cette option est là dans le cas d'une mise à jour d'une decklist. Donner l'ancien fichier et le nouveau l'outil se charge d'en sortir les nouvelles cartes
- 3. Pour l'impression on a place 9 cartes par pages, cette option permet de collecter l'ensemble des .png d'un dossier et les ranger dans des sous-dossier par paquet de 9
- 4. Depuis un dossier contenant les 9 images téléchargé depuis l'API scryfall, l'outil redimmensionne ces images et les places dans une feuille A4 transparente