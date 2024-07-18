# https://scryfall.com/docs/api
import requests


def get_card_by_name(name: str) -> requests.Response:
    """exec a get request to api scryfall with fuzzy params

    Args:
        name (str): value use to fuzzy params

    Returns:
        requests.Response: response from api scryfall
    """
    url = f"https://api.scryfall.com/cards/named?fuzzy={name}"
    response = requests.get(url)
    return response


def get_card_FR(set: str, collectorNumber: int) -> requests.Response:
    """exec a get request to api scryfall with a specific set and collector number to get card in french

    Args:
        set (str): short code for set card
        collectorNumber (int): collector number of card in set

    Returns:
        requests.Response: response from api scryfall
    """
    url = f"https://api.scryfall.com/cards/{set}/{collectorNumber}/fr"
    response = requests.get(url)
    return response
