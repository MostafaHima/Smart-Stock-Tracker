import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class StockData:
    def __init__(self):
        # API endpoint and API key setup
        self.endpoint = 'https://www.alphavantage.co/query'
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY_1")
        self.symbol = None  # To store the stock symbol
        self.prices = {}  # To store stock price details
        self.lastest_day = None  # To store the latest trading day

    def get_symbol_name(self):
        # Prompt user for a stock symbol
        symbol_input = input("Symbol here please: ")
        params = {
            "apikey": self.api_key,
            "function": "SYMBOL_SEARCH",
            "keywords": symbol_input
        }

        # Send a GET request to the API
        response = requests.get(url=self.endpoint, params=params)

        if response.status_code == 200:
            try:
                # Parse the JSON response to extract the stock symbol
                data = response.json()["bestMatches"]
                self.symbol = data[0]["1. symbol"]
            except Exception:
                # Handle cases where the symbol is not found
                print("Try another symbol or check your input.")
            return self.symbol
        else:
            # Print error status if the API request fails
            print(f"Error: {response.status_code}")

    def get_stock_data(self):
        # Set parameters for retrieving daily stock data
        params = {
            "apikey": self.api_key,
            "function": "TIME_SERIES_DAILY",
            "symbol": self.symbol
        }

        # Send a GET request to the API
        response = requests.get(url=self.endpoint, params=params)
        if response.status_code == 200:
            # Parse the JSON response to extract daily stock prices
            data = response.json()["Time Series (Daily)"]
            self.lastest_day = max(data.keys())  # Get the most recent trading day
            prices = data[self.lastest_day]
            self.prices["open_price"] = prices["1. open"]
            self.prices["high_price"] = prices["2. high"]
            self.prices["low_price"] = prices["3. low"]
            self.prices["close_price"] = prices["4. close"]
            return self.prices
        else:
            # Print error status if the API request fails
            print(f"Error {response.status_code}")
