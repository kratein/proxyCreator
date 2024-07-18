import requests
import utilsAPI
import strManipulation
from Card import Card


def dl_png_card(card: Card, pathFolderSave: str):
    if len(card.card_faces) != 0:
        if "image_uris" in card.card_faces[0].keys():
            print(f"{card.name} est double face on va la traiter à part")
            dl_png_card_face(card, pathFolderSave)
            return
    response = requests.get(card.image_uris["png"], stream=True)
    if response.status_code == 200:
        filename = str(card.name).replace("/", "")
        local_filename = f"{pathFolderSave}/{filename}.png"
        with open(local_filename, "wb+") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Image téléchargé et enregistré sous : {local_filename}")
    else:
        print(f"Erreur de téléchargement : {response.status_code}")


def file_to_card(filepath: str, language: str) -> list:
    cards = []
    with open(filepath, "r") as file:
        for line in file:
            cardName = strManipulation.remove_digits(line)
            if language == "en":
                card = utilsAPI.get_EN_card_by_name(cardName)
            elif language == "fr":
                card = utilsAPI.get_FR_card_by_name(cardName)
            else:
                card = None
            cards.append(card)
    return cards


def dl_png_face(card: Card, pathFolderSave: str, face: int):
    try:
        response = requests.get(card.card_faces[face]["image_uris"]["png"], stream=True)
        if response.status_code == 200:
            filename = f"{card.name}_{face}.png"
            filename = filename.replace("/", "")
            local_filename = f"{pathFolderSave}/{filename}"
            with open(local_filename, "wb+") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"Image téléchargé et enregistré sous : {local_filename}")
        else:
            print(f"Erreur du téléchargement : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors du dl de {card.name} \n {e}")


def dl_png_card_face(card: Card, pathFolderSave: str):
    dl_png_face(card, pathFolderSave, 0)
    dl_png_face(card, pathFolderSave, 1)


def extract_unique_cards(
    originalDeckList: str, updateDeckList: str, outputFilePath: str
):
    """_summary_

    Args:
        originalDeckList (str): _description_
        updateDeckList (str): _description_
        outputFilePath (str): _description_

    Returns:
        str: _description_
    """
    originalCardsList = []
    updateCardsList = []
    with open(originalDeckList, "r") as file:
        for line in file:
            originalCardsList.append(line)
    with open(updateDeckList, "r") as file:
        for line in file:
            updateCardsList.append(line)
    newCards = [item for item in updateCardsList if item not in originalCardsList]
    with open(outputFilePath, "w+") as file:
        for card in newCards:
            file.write(f"{card}")
    print(
        f"{len(newCards)} cartes ont été détéctées et enregistrées dans {outputFilePath}"
    )
