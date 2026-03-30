import requests
import json
from datetime import datetime

BASE_URL = "https://api.coingecko.com/api/v3"

TOP_COINS = [
    "bitcoin", "ethereum", "tether", "binancecoin", "solana",
    "ripple", "usd-coin", "dogecoin", "cardano", "tron"
]

last_data = None
last_time = None

#Display Helpers
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
WHITE = "\033[37m"

def clear():
    print("\033[2J\033[H", end="")

def divider():
    print(DIM + " " + "-" * 54 + RESET)

def header():
    print()
    print(BOLD + CYAN + "  CRYPTO PRICE TRACKER  " + RESET)
    print()

def format_price(price):
    if price >= 1:
        return f"${price:>12,.2f}"
    else:
        return f"${price:>12,.6f}"

def format_change(change):
    if change is None:
        return DIM + "   N/A   " + RESET
    arrow = GREEN + "^" if change >= 0 else RED + "v"
    color = GREEN if change >= 0 else RED
    return f"{arrow} {color}{change:+.2f}%{RESET}"

def print_table(data):
    """Render a clean table from dict of coin data."""
    print()
    print(BOLD + f"  {'Coin':<18} {'Price (USD)':>14}  {'24hr Change':>12}" + RESET)
    divider()

    for coin_id, info in data.items():
        name  = coin_id.replace("-", " ").title()
        price = info.get("usd", 0)
        change = info.get("usd_24h_change", None)

        price_str = format_price(price)
        change_str = format_change(change)

        print(f"   {YELLOW}{name:<18}{RESET} {price_str} {change_str}")

    divider()
    if last_time:
        print(DIM + f"  Last Updated: {last_time}" + RESET)
    print()

#API CALLS

def fetch_prices(coin_ids):
    global last_data, last_time
    data = None

    ids_param = ",".join(coin_ids)
    params = {
    "ids":         ids_param,
    "vs_currencies": "usd",
    "include_24hr_change": "true"
    }

    try:
        print(DIM + "   Fetching data..." + RESET, end="\r")
        response = requests.get(
            f"{BASE_URL}/simple/price",
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if not data:
            print(RED + "  No data returned...The coin name may be invalid" + RESET)
            return None

        last_data = data
        last_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")


    except requests.exceptions.ConnectionError:
        print(RED + BOLD + "  Connection error...Please check your network.\n" + RESET)
    except requests.exceptions.Timeout:
        print(RED + BOLD + "  Request timeout...Please try again.\n" + RESET)
    except requests.exceptions.HTTPError as e:
        print(RED + BOLD + f"  HTTP error: {e}\n" + RESET)
    except (json.JSONDecodeError, ValueError):
        print(RED + BOLD + "  Error: Received an invalid response from the API.\n" + RESET)
    except Exception as e:
        print(RED + BOLD + f"  Unexpected Error: {e}\n" + RESET)

    return data

def search_coin():
    print()
    coin_input = input(BOLD + "Enter coin to search for: " + RESET).strip().lower()

    if not coin_input:
        print(RED + "  No coin to search for." + RESET)
        return

    coin_ids = coin_input.replace(" ", "-")
    data = fetch_prices([coin_ids])

    if data:
        print_table(data)
    else:
        print(RED + f"  Could not find '{coin_input}'. Check the spelling and try again.\n" + RESET)


#MENU SCREENS

def show_menu():
    clear()
    header()
    print(f"         {YELLOW}1.{RESET} View Top 10 Crypto Prices")
    print(f"         {YELLOW}2.{RESET} Search a Coin")
    print(f"         {YELLOW}3.{RESET} Refresh Last Data")
    print(f"         {YELLOW}4.{RESET} Quit")
    print()
    divider()

def view_top_coins():
    clear()
    header()
    print(BOLD + "   Top 10 Cryptocurrencies:\n" + RESET)
    data = fetch_prices(TOP_COINS)
    if data:
        print_table(data)

def refresh():
    if last_data is None:
        print(RED + "  No data to refresh yet. Fetch data first\n" + RESET)
        return
    clear()
    header()
    print(BOLD + "   Refresh...\n" + RESET)

    coin_ids = list(last_data.keys())
    data     = fetch_prices(coin_ids)
    if data:
        print_table(data)


#------------------------------------------------
#     MAIN
#------------------------------------------------

def main():
    clear()
    header()
    print(WHITE + "  WELCOME TO THE CRYPTO PRICE TRACKER" + RESET)
    print(DIM   + "  Powered by CoinGecko API - live prices, no key needed.\n" + RESET)
    input(DIM   + "  Press ENTER to continue..." + RESET)

    while True:
        show_menu()
        choice = input(BOLD + WHITE + " Enter choice(1-4): " + RESET).strip()

        if choice == "1":
            view_top_coins()
            input(DIM + "  Press ENTER to return to menu..." + RESET)
        elif choice == "2":
            clear()
            header()
            search_coin()
            input(DIM + "  Press ENTER to return to menu..." + RESET)
        elif choice == "3":
            refresh()
            input(DIM + "  Press ENTER to return to menu..." + RESET)
        elif choice == "4":
            clear()
            header()
            print(GREEN + BOLD + " Thanks for using Crypto Tracker. Goodbye for now!\n" + RESET)
            break
        else:
            print(RED + BOLD + "  Invalid input. Please try again.\n" + RESET)
            input(DIM + "  Press ENTER to continue..." + RESET)

if __name__ == "__main__":
    main()

