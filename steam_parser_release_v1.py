#!/usr/bin/python3
import requests, os, json
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def question():
    name = Prompt.ask("[bold cyan]Enter game name[/bold cyan]")
    if name == "exit":
        console.print("Okey, bye!", style="bold bright_black")
        exit()
    cc  = Prompt.ask("[bold cyan]Which country's currency[/bold cyan]", choices=["ua", "de", "it", "us", "jp"])
    return name, cc

def get_info(name, cc):
    clear_screen()

    response = requests.get("https://store.steampowered.com/api/storesearch/", timeout=5,
                            params={"term": name, "cc": cc, "l": "ukrainian"}).json()

    if not response.get("items"):
        console.print("[bold magenta]Game not found![/bold magenta]")
        return None

    game_id = str(response['items'][0]['id'])
    response = requests.get("https://store.steampowered.com/api/appdetails", timeout=5,
                            params={"appids": game_id, "cc": cc}).json()

    if 'data' not in response[game_id]:
        console.print("This game is banned in your country :exclamation:", style="bold red")
        return None
    else:
        return response[game_id]['data']

def print_info(response):
    if not response:
        return
    clear_screen()

    console.print(f"[bold violet]Name:[/bold violet] [white]{response['name']}[/white]")
    console.print(f"[bold violet]Game ID:[/bold violet] [white]{response['steam_appid']}[/white]")

    if 'publishers' in response:
        console.print(f"[bold violet]Publishers:[/bold violet] [white]{response['publishers'][0]}[/white]")
    else:
        console.print("[bold violet]Publishers:[/bold violet] [white]?[/white]")

    if response['is_free']:
        console.print(f"[bold green]Price:[/bold green] [bright_green]Free to play![/bright_green]")
    else:
        if response['price_overview']['discount_percent'] == 0:
            console.print(f"[bold violet]Price:[/bold violet] [bright_white]{response['price_overview']['final_formatted']}[/bright_white]")
        else:
            console.print(
                f"[bold violet]Price:[/bold violet] [bright_yellow]{response['price_overview']['discount_percent']}% off - {response['price_overview']['final_formatted']}[/bright_yellow]"
            )

    descriptions = [genre['description'] for genre in response['genres']]
    console.print(f"[bold violet]Genres:[/bold violet] [white]{', '.join(descriptions)}[/white]")

if __name__ == "__main__":
    clear_screen()
    while True:
        console.print("======================= [bold cyan]Software by Dargram[/bold cyan] =======================", style="italic bright_black")
        try:
            name, cc = question()
            print_info(get_info(name, cc))
        except IndexError:
            console.print("[bold magenta]Game doesn't exist![/bold magenta]")
