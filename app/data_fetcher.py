import yfinance as yf

class StockDataFetcher:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch_data(self):
        stock_data = yf.download(self.ticker)
        return stock_data

    def get_latest_price(self):
        stock_data = self.fetch_data()
        return stock_data['Close'][-1] if not stock_data.empty else None

    def get_historical_data(self, start_date=None, end_date=None):
        return yf.download(self.ticker, start=start_date, end=end_date)
