
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self, cash):
        self.cash = cash
        self.stocks = {}

    def buy_stock(self, stock, quantity):
        cost = stock.price * quantity
        if cost > self.cash:
            print("Insufficient funds!")
            return
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity
        self.cash -= cost

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            if self.stocks[stock.symbol] >= quantity:
                self.stocks[stock.symbol] -= quantity
                self.cash += stock.price * quantity
            else:
                print("Not enough shares to sell!")
        else:
            print("You do not own this stock!")

    def show_portfolio(self):
        print("Cash: $", self.cash)
        print("Stocks:")
        for symbol, quantity in self.stocks.items():
            print(symbol + ": " + str(quantity) + " shares")

# Create some stocks
apple = Stock("AAPL", 150.00)
google = Stock("GOOGL", 2000.00)

# Create a portfolio
portfolio = Portfolio(10000)

# Perform some trades
portfolio.buy_stock(apple, 10)
portfolio.buy_stock(google, 5)
portfolio.sell_stock(apple, 3)

# Display the portfolio
portfolio.show_portfolio()
