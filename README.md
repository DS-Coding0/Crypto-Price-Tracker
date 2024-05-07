# Crypto Price Tracker

This is a simple Python script that uses the Chainlink API to fetch the prices of various cryptocurrencies and the Euro, and displays them in a table. The table is updated every 20 seconds, and it highlights any changes in price since the last update.

## Setup

To run this script, you will need to have Python 3.x installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

Once you have Python installed, you can run the script by navigating to the project directory in your terminal and running the command `python Crypto_Price_Tracker_v01.py`.

## Usage

The script will display a table with the following columns:

- **Currencies**: The name of the currency.
- **in $**: The price of the currency in US Dollars.
- **in €**: The price of the currency in Euros.

The prices are updated every 20 seconds, and any changes in price since the last update are highlighted in green (for an increase) or red (for a decrease).

## Configuration

The script is configured to track the prices of the following currencies:

- Bitcoin (BTC) in Dollar
- Ethereum (ETH) in Dollar
- Ripple (XRP) in Dollar
- Solana (SOL) in Dollar
- Convert Dollar prices in Euro (EUR)

If you want to track the price of a different currency, you can modify the `get_price` function to use the appropriate `feed_id` and `divisor` for that currency. You can find a list of available `feed_ids` on the [Chainlink website](https://data.chain.link/).

## Dependencies

This script uses the following Python libraries:

- `requests`: for making HTTP requests to the Chainlink API.
- `colorama`: for printing colored text in the terminal.
- `tabulate`: for displaying the price data in a table.

You can install these libraries using `pip`, the Python package manager, by running the command `pip install requests colorama tabulate`.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
