import pandas as pd
from stock import Stock

class Portfolio:
    def __init__(self, portfolio_name):
        self.stocks = []
        self.portfolioName = portfolio_name

    def parse_portfolio(self):
        portfolio = pd.read_excel('stocks.xlsx')
        i = 0
        for stock in portfolio["Ticker"]:
            ticker = portfolio['Ticker'][i]
            shares = portfolio['Shares'][i]
            buy_price = portfolio['BuyPrice'][i]
            self.stocks.append(Stock(ticker, shares, buy_price))
            i += 1
