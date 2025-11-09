import requests, json

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                " AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "q=0.9,en-US;q=0.8,en;q=0.7",
}

def get_game_info(name, cc):
    search_response = requests.get(
        "https://store.steampowered.com/api/storesearch/",
        timeout=5,
        params={"term": name, "cc": cc, "l": "ukrainian"},
        headers=HEADERS).json()

    if not search_response.get("items"):
        return None

    game_id = str(search_response['items'][0]['id'])
    
    details_response = requests.get(
        "https://store.steampowered.com/api/appdetails",
        timeout=5,
        params={"appids": game_id, "cc": cc},
        headers=HEADERS
    ).json()

    if 'data' not in details_response[game_id]:
        return None
    
    return details_response[game_id]['data']