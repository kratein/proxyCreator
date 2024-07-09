import requests
import utilsAPI
from Card import Card

def dlPngCard(card: Card, pathFolderSave: str):
    if len(card.card_faces) != 0:
        if "image_uris" in card.card_faces[0].keys():
            print(f"{card.name} est double face on va la traiter à part")
            dlPngCardFace(card, pathFolderSave)
            return
    response = requests.get(card.image_uris["png"], stream=True)
    if response.status_code == 200:
        filename = str(card.name).replace("/", "")
        local_filename = f"{pathFolderSave}/{filename}.png"
        with open(local_filename, 'wb+') as file: 
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"Image téléchargé et enregistré sous : {local_filename}")
    else: 
        print(f"Erreur du téléchargement : {response.status_code}")

def fileToCardFR(filepath: str)->list:
    cards = []
    with open(filepath, 'r') as file:
        for line in file: 
            card = utilsAPI.getFRCardByName(line)
            cards.append(card)
    return cards

def dlPngFace(card: Card, pathFolderSave: str, face: int):
    try:
        response = requests.get(card.card_faces[face]["image_uris"]["png"], stream=True)
        if response.status_code == 200:
            filename = f"{card.name}_{face}.png"
            filename = filename.replace("/", "")
            local_filename = f"{pathFolderSave}/{filename}"
            with open(local_filename, 'wb+') as file: 
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"Image téléchargé et enregistré sous : {local_filename}")
        else: 
            print(f"Erreur du téléchargement : {response.status_code}")
    except Exception as e:
      print(f'Erreur lors du dl de {card.name} \n {e}')


def dlPngCardFace(card: Card, pathFolderSave: str):
    dlPngFace(card, pathFolderSave, 0)
    dlPngFace(card, pathFolderSave, 1)


