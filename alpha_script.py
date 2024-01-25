
class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def buy(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        else:
            print("Not enough shares to sell.")
            return False

    def display(self):
        print(f"Stock: {self.symbol}, Price: {self.price}, Quantity: {self.quantity}")


class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def buy_stock(self, symbol, quantity):
        if symbol in self.stocks:
            stock = self.stocks[symbol]
            stock.buy(quantity)
        else:
            print("Stock not found.")

    def sell_stock(self, symbol, quantity):
        if symbol in self.stocks:
            stock = self.stocks[symbol]
            if stock.sell(quantity):
                del self.stocks[symbol]
        else:
            print("Stock not found.")

    def display_portfolio(self):
        for stock_symbol, stock in self.stocks.items():
            stock.display()


def main():
    apple = Stock("AAPL", 150, 10)
    microsoft = Stock("MSFT", 300, 5)

    portfolio = Portfolio()
    portfolio.add_stock(apple)
    portfolio.add_stock(microsoft)

    portfolio.display_portfolio()

    portfolio.buy_stock("AAPL", 5)
    portfolio.buy_stock("GOOG", 3)

    portfolio.sell_stock("AAPL", 7)
    portfolio.sell_stock("GOOG", 2)

    portfolio.display_portfolio()


if __name__ == "__main__":
    main()
