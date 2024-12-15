import requests
from dotenv import load_dotenv
import os

# Load environment variables for API keys
load_dotenv()

class StockNews:
    def __init__(self, symbol, date):
        # API endpoint and necessary parameters
        self.endpoint = "https://newsapi.org/v2/everything"
        self.api_key = os.getenv("NEWS_API_KEY")  # Load API key from environment
        self.symbol = symbol
        self.date = date
        self.article = {}

    def get_news_data(self):
        # Parameters for the news API request
        params = {
            "q": self.symbol.lower(),  # Search query using the stock symbol
            "from": self.date,         # Filter articles starting from the given date
            "to": self.date,           # Filter articles up to the given date
            "sortBy": "popularity",    # Sort articles by popularity
            "apiKey": self.api_key     # API key for authentication
        }

        # Make the GET request to fetch news data
        response = requests.get(url=self.endpoint, params=params)
        if response.status_code == 200:  # Check for successful response
            data = response.json()  # Parse the response as JSON

            article = data["articles"]
            if article:  # Check if articles are available
                # Extract relevant fields from the first article
                title = article[0]["title"] if "title" in article[0] and article[0]["title"] else "No Title Available"
                author = article[0]["author"] if "author" in article[0] and article[0]["author"] else "Unknown Author"
                content = article[0]["content"] if "content" in article[0] and article[0]["content"] else "No Content Available"
                url = article[0]["url"] if "url" in article[0] and article[0]["url"] else "No URL Available"
                image_url = article[0]["urlToImage"] if "urlToImage" in article[0] and article[0]["urlToImage"] else "No Image URL"
            else:  # No articles available
                title = "No Title Available"
                author = "Unknown Author"
                content = "No Content Available"
                url = "No URL Available"
                image_url = "No Image URL"

            # Store the extracted article data in a dictionary
            self.article = {
                "author": author,
                "title": title,
                "url": url,
                "image_url": image_url,
                "content": content
            }
            print("Getting News Successfully!")
            return self.article

        else:  # Handle HTTP errors
            print(f"Error: {response.status_code} >> {response.raise_for_status()}")
