import tools
import fileManipulation
import imageManipulation
import os

def main():
    # Display the welcome message and options to the user
    print("Bienvenue dans l'outil de création de proxy")
    print("Que veux-tu faire ?")
    print("1. Télécharger les png depuis un fichier")
    print("2. Comparer deux listes de cartes pour en extraire les cartes différences")
    print("3. Trier les images dans des dossiers différents par 9")
    print("4. Construire la page pour impression recto")
    
    # Get the user's choice
    choice = input()

    if choice == "1":
        # Option 1: Download PNGs from a file
        print("Entrez le chemin complet vers le fichier de référence")
        filepath = input()  # Get the path to the reference file
        print("Indiquez le dossier de téléchargement")
        saveFolder = input()  # Get the download folder
        print("fr/en ?")
        language = input()  # Get the language preference
        cards = tools.file_to_card(filepath, language)  # Convert file to card list
        for card in cards:
            tools.dl_png_card(card, saveFolder)  # Download each card as PNG
        print(f"Les {len(cards)} cartes ont été téléchargées dans {saveFolder}")
    elif choice == "2":
        # Option 2: Compare two card lists to extract differences
        print("Entrez le chemin complet vers le fichier de votre deck liste originale")
        originalDeckList = input()  # Get the path to the original deck list
        print("Entrez le chemin complet vers le fichier de votre deck liste mise à jour")
        updateDeckList = input()  # Get the path to the updated deck list
        print("Entrez le chemin complet vers le fichier contenant uniquement les cartes ajoutées")
        outputFilePath = input()  # Get the path for the output file
        tools.extract_unique_cards(originalDeckList, updateDeckList, outputFilePath)  # Extract unique cards
    elif choice == "3":
        # Option 3: Organize images into folders of 9
        print("Entrez le chemin vers le dossier à trier")
        rootDirectory = input()  # Get the root directory to organize
        fileManipulation.organize_png_files(rootDirectory)  # Organize PNG files
    elif choice == "4":
        # Option 4: Create a page for front-side printing
        print("Entrez le chemin vers le dossier de travail")
        workDirectory = input()  # Get the working directory
        for itemName in os.listdir(workDirectory):
            itemPath = os.path.join(workDirectory, itemName)
            if os.path.isdir(itemPath):
                images_cards = fileManipulation.get_all_png(itemPath)  # Get all PNG images
                imageManipulation.resize_all_in_folder(itemPath, images_cards)  # Resize all images
                imageManipulation.create_page_to_print_front(
                    f"{itemPath}/front.png" , images_cards
                )  # Create the front page for printing                


if __name__ == "__main__":
    main()
