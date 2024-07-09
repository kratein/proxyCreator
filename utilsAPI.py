import apiScryFall, json
from Card import Card

def getFRCardByName(name: str)->Card:
    response = apiScryFall.getCardByName(name)
    jsonResponse = json.loads(response.content)
    if response.status_code == 200:
        jsonResponse = json.loads(response.content)
        cardEn = Card(jsonResponse)
    else:
        print(f"La carte {name} n'a pas été trouvé") 

    response = apiScryFall.getCardFR(cardEn.set, cardEn.collector_number)
    if response.status_code == 200:
        jsonResponse = json.loads(response.content)
        cardFr = Card(jsonResponse)
        return cardFr
    elif response.status_code == 404:
        print(f"La carte {cardEn.name} n'est pas disponible en français")
        return cardEn