
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

class Portfolio:
    def __init__(self):
        self.cash = 1000
        self.stocks = []

    def buy_stock(self, stock, shares):
        total_cost = stock.price * shares
        if self.cash >= total_cost:
            self.cash -= total_cost
            stock.shares += shares
            self.stocks.append(stock)
            print(f'Bought {shares} shares of {stock.symbol} at ${stock.price} per share')
        else:
            print('Insufficient cash to buy stock')

    def sell_stock(self, symbol, shares):
        for stock in self.stocks:
            if stock.symbol == symbol:
                if stock.shares >= shares:
                    total_cost = stock.price * shares
                    self.cash += total_cost
                    stock.shares -= shares
                    print(f'Sold {shares} shares of {symbol} at ${stock.price} per share')
                    if stock.shares == 0:
                        self.stocks.remove(stock)
                else:
                    print('Insufficient shares to sell')
                return
        print('Stock not found in portfolio')

    def display_portfolio(self):
        print('Cash: $' + str(self.cash))
        for stock in self.stocks:
            print(f'{stock.symbol} - Shares: {stock.shares} - Price: ${stock.price}')

# Create some stocks
apple = Stock('AAPL', 150)
google = Stock('GOOGL', 2000)

# Create a portfolio
portfolio = Portfolio()

# Trading
portfolio.buy_stock(apple, 5)
portfolio.buy_stock(google, 2)
portfolio.display_portfolio()
portfolio.sell_stock('AAPL', 3)
portfolio.display_portfolio()
