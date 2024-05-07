import requests
import time
from colorama import Fore, init
from tabulate import tabulate

# Request for Crypto Price Feeds
def get_price(feed_id, divisor, xlong):
    url = f"https://data.chain.link/api/query-timescale?query=LIVE_STREAM_REPORTS_QUERY&variables=%7B%22feedId%22%3A%22{feed_id}%22%7D"
    price = requests.get(url).json()["data"]["liveStreamReports"]["nodes"][0]["price"]
    price = round(float(price) / divisor, xlong)
    return price

# Request for Dollar/Euro
def get_eur_price():
    url = "https://data.chain.link/api/query?query=FEED_DATA_QUERY&variables=%7B%22schemaName%22%3A%22ethereum-mainnet%22%2C%22contractAddress%22%3A%220x02f878a94a1ae1b15705acd65b5519a46fe3517e%22%7D"
    price = requests.get(url).json()["data"]["chainData"]["nodes"][0]["inputs"]["answer"]
    price = round(float(price) / 100000000, 2)
    return price


# Initialize previous prices
previous_prices_dollar = {"BTC": 0, "ETH": 0, "XRP": 0, "SOL": 0, "TRX": 0, "EUR": 0}
previous_prices_euro = {"BTC": 0, "ETH": 0, "XRP": 0, "SOL": 0, "TRX": 0, "EUR": 0}

while True:
    table = [
        [
            "BTC",
            get_price(
                "0x00039d9e45394f473ab1f050a1b963e6b05351e52d71e507509ada0c95ed75b8",
                1000000000000000000,
                2,
            ),
            round(
                get_price(
                    "0x00039d9e45394f473ab1f050a1b963e6b05351e52d71e507509ada0c95ed75b8",
                    1000000000000000000,
                    2,
                )
                / get_eur_price(),
                2,
            ),
        ],
        [
            "ETH",
            get_price(
                "0x000362205e10b3a147d02792eccee483dca6c7b44ecce7012cb8c6e0b68b3ae9",
                1000000000000000000,
                2,
            ),
            round(
                get_price(
                    "0x000362205e10b3a147d02792eccee483dca6c7b44ecce7012cb8c6e0b68b3ae9",
                    1000000000000000000,
                    2,
                )
                / get_eur_price(),
                2,
            ),
        ],
        [
            "XRP",
            get_price(
                "0x0003c16c6aed42294f5cb4741f6e59ba2d728f0eae2eb9e6d3f555808c59fc45",
                1000000000000000000,
                4,
            ),
            round(
                get_price(
                    "0x0003c16c6aed42294f5cb4741f6e59ba2d728f0eae2eb9e6d3f555808c59fc45",
                    1000000000000000000,
                    4,
                )
                / get_eur_price(),
                4,
            ),
        ],
        [
            "SOL",
            get_price(
                "0x0003b778d3f6b2ac4991302b89cb313f99a42467d6c9c5f96f57c29c0d2bc24f",
                1000000000000000000,
                2,
            ),
            round(
                get_price(
                    "0x0003b778d3f6b2ac4991302b89cb313f99a42467d6c9c5f96f57c29c0d2bc24f",
                    1000000000000000000,
                    2,
                )
                / get_eur_price(),
                2,
            ),
        ],
        ["EUR", get_eur_price(), 1],
    ]
    headers = ["Currencies", " in $".rjust(10), "in €".rjust(12)]

    # Compare current prices with previous prices
    for i, row in enumerate(table):
        currency = row[0]
        current_price = row[1]
        if currency in previous_prices_dollar:
            previous_price = previous_prices_dollar[currency]
            if current_price > previous_price:
                table[i][1] = (
                    Fore.GREEN + str(current_price).rjust(10) + Fore.WHITE + " $"
                )
            elif current_price < previous_price:
                table[i][1] = (
                    Fore.RED + str(current_price).rjust(10) + Fore.WHITE + " $"
                )
            else:
                table[i][1] = Fore.WHITE + str(current_price).rjust(10) + " $"

        # Update previous prices
        previous_prices_dollar[currency] = current_price

    # Compare current prices with previous prices
    for i, row in enumerate(table):
        currency = row[0]
        current_price = row[2]
        if currency in previous_prices_euro:
            previous_price = previous_prices_euro[currency]
            if current_price > previous_price:
                table[i][2] = (
                    Fore.GREEN + str(current_price).rjust(10) + Fore.WHITE + " €"
                )
            elif current_price < previous_price:
                table[i][2] = (
                    Fore.RED + str(current_price).rjust(10) + Fore.WHITE + " €"
                )
            else:
                table[i][2] = Fore.WHITE + str(current_price).rjust(10) + " €"

        # Update previous prices
        previous_prices_euro[currency] = current_price

    # Create table to display
    print(tabulate(table, headers, tablefmt="github"))
    print("\n\n")
    
    # Time.sleep to the next price update
    time.sleep(20)
