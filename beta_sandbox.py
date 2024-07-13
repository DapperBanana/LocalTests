
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity

    def remove_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] -= quantity
            if self.stocks[stock.symbol] <= 0:
                del self.stocks[stock.symbol]

    def portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            total_value += symbol.price * quantity
        return total_value

def main():
    apple_stock = Stock("AAPL", 150)
    google_stock = Stock("GOOGL", 250)
    
    portfolio = Portfolio()
    portfolio.add_stock(apple_stock, 10)
    portfolio.add_stock(google_stock, 5)

    print(f"Portfolio value: ${portfolio.portfolio_value()}")

    apple_stock.update_price(160)
    google_stock.update_price(260)

    print(f"Updated portfolio value: ${portfolio.portfolio_value()}")

if __name__ == "__main__":
    main()
