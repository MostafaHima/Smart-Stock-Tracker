# Importing necessary modules
from get_stock_data import StockData
from get_stock_news import StockNews
from send_mail import send_mail

# Initialize the StockData class
init_stock_prices = StockData()

# Get the stock symbol from the user
stock_symbol = init_stock_prices.get_symbol_name()

# Fetch the latest stock price data
stock_prices = init_stock_prices.get_stock_data()
print("Getting Price Successfully!")

# Initialize the StockNews class with the stock symbol and latest date
init_stock_news = StockNews(symbol=stock_symbol, date=init_stock_prices.lastest_day)

# Fetch the latest news article related to the stock
article = init_stock_news.get_news_data()

# Send an email with the stock data and news insights
send_mail(
    subject=f"Stock Update: {stock_symbol} Prices & Insights",
    day=init_stock_prices.lastest_day,
    open_price=stock_prices["open_price"],  # Opening price of the stock
    high_price=stock_prices["high_price"],  # Highest price of the stock
    low_price=stock_prices["low_price"],   # Lowest price of the stock
    close_price=stock_prices["close_price"],  # Closing price of the stock
    title=article["title"],  # Title of the news article
    author=article["author"],  # Author of the news article
    content=article["content"],  # Content of the news article
    url=article["url"],  # URL of the full article
    url_image=article["image_url"]  # Image URL from the article
)
