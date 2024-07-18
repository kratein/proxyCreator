import apiScryFall
import json
from Card import Card


def get_FR_card_by_name(name: str) -> Card:
    response = apiScryFall.get_card_by_name(name)
    jsonResponse = json.loads(response.content)
    if response.status_code == 200:
        jsonResponse = json.loads(response.content)
        cardEn = Card(jsonResponse)
    else:
        print(f"La carte {name} n'a pas été trouvé")
    response = apiScryFall.get_card_FR(cardEn.set, cardEn.collector_number)
    if response.status_code == 200:
        jsonResponse = json.loads(response.content)
        cardFr = Card(jsonResponse)
        return cardFr
    elif response.status_code == 404:
        print(f"La carte {cardEn.name} n'est pas disponible en français")
        return cardEn


def get_EN_card_by_name(name: str) -> Card:
    response = apiScryFall.get_card_by_name(name)
    jsonResponse = json.loads(response.content)
    if response.status_code == 200:
        jsonResponse = json.loads(response.content)
        return Card(jsonResponse)
    else:
        print(f"La carte {name} n'a pas été trouvé")
        return None
