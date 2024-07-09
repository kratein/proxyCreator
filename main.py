import utilsAPI, tools

def main():
    print("Bienvenue dans l'outil de création de proxy")
    print("Que veux-tu faire ?")
    print("1. Télécharger les png en français depuis un fichier")
    choice = input()

    if choice == "1":
        print("Entre le chemin complet vers le fichier de référence")
        filepath = input()
        print("Indique le dossier de téléchargement")
        saveFolder = input()
        cards = tools.fileToCardFR(filepath)
        for card in cards:
            tools.dlPngCard(card, saveFolder)
        print(f"Les {len(cards)} cartes ont été téléchargées dans {saveFolder}")


if __name__ == "__main__":
    main()

