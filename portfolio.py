import pandas as pd
from stock import Stock


class Portfolio:
    def __init__(self, portfolio_name):
        self.stocks = []
        self.portfolioName = portfolio_name

    def parse_portfolio(self):
        df = pd.read_excel('stocks.xlsx')

        for index, df_stock in df.iterrows():
            self.stocks.append(Stock(df_stock['Ticker'], df_stock['Shares'], df_stock['BuyPrice']))
