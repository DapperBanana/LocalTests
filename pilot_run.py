
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def buy_stock(self, symbol, price, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def sell_stock(self, symbol, price, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] >= quantity:
                self.stocks[symbol] -= quantity
            else:
                print("Not enough stocks to sell")
        else:
            print("Stock not in portfolio")

    def portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            total_value += quantity * symbol.price
        return total_value

# Stock symbols and prices
stocks = {
    'AAPL': Stock('AAPL', 150),
    'GOOGL': Stock('GOOGL', 2000),
    'MSFT': Stock('MSFT', 260)
}

portfolio = Portfolio()

while True:
    print("\n1. Buy Stock\n2. Sell Stock\n3. Portfolio Value\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        symbol = input("Enter stock symbol: ")
        if symbol in stocks:
            price = stocks[symbol].price
            quantity = int(input("Enter quantity: "))
            portfolio.buy_stock(symbol, price, quantity)
        else:
            print("Invalid stock symbol")

    elif choice == 2:
        symbol = input("Enter stock symbol: ")
        if symbol in stocks:
            price = stocks[symbol].price
            quantity = int(input("Enter quantity: "))
            portfolio.sell_stock(symbol, price, quantity)
        else:
            print("Invalid stock symbol")

    elif choice == 3:
        print("Portfolio Value: $", portfolio.portfolio_value())

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.")
