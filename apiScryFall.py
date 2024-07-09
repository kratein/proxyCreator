#https://scryfall.com/docs/api
import requests, json

def getCardByName(name: str)->requests.Response:
    url = f"https://api.scryfall.com/cards/named?fuzzy={name}"
    response = requests.get(url)
    return response

def getCardFR(set: str, collector_number: int)->requests.Response:
    url = f"https://api.scryfall.com/cards/{set}/{collector_number}/fr"
    response = requests.get(url)
    return response