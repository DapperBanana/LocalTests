
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.quantity = 0

    def buy(self, qty):
        self.quantity += qty

    def sell(self, qty):
        if self.quantity >= qty:
            self.quantity -= qty
            return True
        else:
            return False

class StockTradingSystem:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, price):
        stock = Stock(symbol, price)
        self.stocks[symbol] = stock

    def buy_stock(self, symbol, qty):
        if symbol in self.stocks:
            self.stocks[symbol].buy(qty)
            print(f"Bought {qty} shares of {symbol}")
        else:
            print(f"Stock {symbol} not found")

    def sell_stock(self, symbol, qty):
        if symbol in self.stocks:
            if self.stocks[symbol].sell(qty):
                print(f"Sold {qty} shares of {symbol}")
            else:
                print(f"Not enough shares of {symbol} to sell")
        else:
            print(f"Stock {symbol} not found")

    def display_portfolio(self):
        for symbol, stock in self.stocks.items():
            if stock.quantity > 0:
                print(f"{symbol}: {stock.quantity} shares @ {stock.price}")

# Sample usage
sts = StockTradingSystem()
sts.add_stock("AAPL", 150.50)
sts.add_stock("GOOG", 1100.00)

sts.buy_stock("AAPL", 10)
sts.buy_stock("GOOG", 5)

sts.display_portfolio()

sts.sell_stock("AAPL", 5)
sts.sell_stock("GOOG", 3)

sts.display_portfolio()
