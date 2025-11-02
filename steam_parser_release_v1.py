import requests, os, json

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def question():
    name = input("Enter game name: ")
    if name == "exit":
        print("Okey, bye!")
        exit()
    cc  = input("Which country's currency: ")
    return name, cc


def get_info(name, cc):
    clear_screen()

    response = requests.get("https://store.steampowered.com/api/storesearch/", timeout=5, params={"term": name, "cc": cc, "l": "ukrainian" }).json()
    game_id = str(response['items'][0]['id'])

    response = (requests.get("https://store.steampowered.com/api/appdetails", timeout=5, params={"appids": game_id, "cc":cc})).json()


    if 'data' not in response[game_id]:
        print("This game is banned in your country")
        return None
    else:
        return response[game_id]['data']


def print_info(response):
    if not response:
        return
    clear_screen()

    print(f"Name: {response['name']};")
    print(f"Game ID: {response['steam_appid']};")
    print(f"Publishers: {response['publishers'][0]};")

    if response['is_free'] == True:
        print(f"Price: game is free!")
    elif response['is_free'] == False:
        if response['price_overview']['discount_percent'] == 0:
            print(f"Price: full price - {response['price_overview']['final_formatted']};")
        else:
            print(f"Price: with discount {response['price_overview']['discount_percent']}% - {response['price_overview']['final_formatted']};")
    descriptions = []
    for genre in response['genres']:
        descriptions.append(genre['description'])
    print(f"Genres: {', '.join(descriptions)};")


if __name__ == "__main__":
    while True:
        name, cc = question()
        print_info(get_info(name, cc))