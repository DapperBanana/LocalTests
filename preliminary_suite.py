
class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

class TradingSystem:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, price, quantity):
        if symbol in self.stocks:
            print(f"Stock {symbol} already exists in the system.")
        else:
            self.stocks[symbol] = Stock(symbol, price, quantity)
            print(f"Stock {symbol} added to the system.")
    
    def buy_stock(self, symbol, quantity):
        if symbol not in self.stocks:
            print(f"Stock {symbol} does not exist in the system.")
        else:
            stock = self.stocks[symbol]
            total_price = stock.price * quantity
            if total_price > stock.quantity:
                print("Insufficient quantity available.")
            else:
                stock.quantity -= quantity
                print(f"Bought {quantity} shares of {symbol} for ${total_price}.")
    
    def sell_stock(self, symbol, quantity):
        if symbol not in self.stocks:
            print(f"Stock {symbol} does not exist in the system.")
        else:
            stock = self.stocks[symbol]
            total_price = stock.price * quantity
            stock.quantity += quantity
            print(f"Sold {quantity} shares of {symbol} for ${total_price}.")
    
    def display_portfolio(self):
        for symbol, stock in self.stocks.items():
            print(f"{symbol}: Price - ${stock.price}, Quantity - {stock.quantity}")

# Usage
ts = TradingSystem()
ts.add_stock("AAPL", 150.50, 100)
ts.add_stock("GOOGL", 2500.75, 50)

ts.display_portfolio()

ts.buy_stock("AAPL", 10)
ts.sell_stock("GOOGL", 5)

ts.display_portfolio()
