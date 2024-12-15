# StockWise Assistant

## Description
An interactive tool using APIs to fetch stock data and prices, display the latest news about the stock, and send a detailed report via email using SMTP.

---

## Features
- **Fetch Stock Data**: Retrieves real-time stock data including opening, closing, high, and low prices using the Alpha Vantage API.
- **Get News Articles**: Fetches the latest news articles related to the stock from NewsAPI.
- **Email Reports**: Sends a comprehensive email report with stock data and news insights using SMTP.

---

## Requirements
- Python 3.9 or higher
- API keys for:
  - [Alpha Vantage](https://www.alphavantage.co/)
  - [NewsAPI](https://newsapi.org/)
- SMTP email service credentials

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/StockWise-Assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Smart Stock Tracker
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Set up your environment variables for API keys and SMTP credentials:
   - `ALPHAVANTAGE_API_KEY`: Your Alpha Vantage API key
   - `NEWSAPI_API_KEY`: Your NewsAPI key
   - `SMTP_EMAIL`: Your email address
   - `SMTP_PASSWORD`: Your email password

2. Run the main script:
   ```bash
   python main.py
   ```
3. Enter the stock name when prompted, and the tool will handle the rest!

---

## File Structure
- **get_stock_data.py**: Handles fetching stock data from Alpha Vantage.
- **get_stock_news.py**: Fetches news articles related to the stock from NewsAPI.
- **send_mail.py**: Sends email reports using SMTP.
- **main.py**: Orchestrates the flow of the application.

---

## Example Output
### Email Content
- **Subject**: Stock Update: [Stock Symbol] Prices & Insights
- **Body**:
  - Date: [Latest Trading Day]
  - Open Price: [Price]
  - High Price: [Price]
  - Low Price: [Price]
  - Close Price: [Price]
  - News Title: [Article Title]
  - Author: [Article Author]
  - Content: [Article Summary]
  - Read more: [Article URL]


