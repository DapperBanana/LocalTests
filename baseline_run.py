
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def __str__(self):
        return f"{self.symbol} - ${self.price}"


class Portfolio:
    def __init__(self, money):
        self.money = money
        self.stocks = {}

    def buy_stock(self, stock, quantity):
        cost = stock.price * quantity
        if cost > self.money:
            print("Insufficient funds to buy stock")
            return
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity
        self.money -= cost
        print(f"Bought {quantity} shares of {stock.symbol} at ${stock.price}")

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            if quantity > self.stocks[stock.symbol]:
                print("Insufficient shares to sell")
                return
            self.stocks[stock.symbol] -= quantity
            self.money += stock.price * quantity
            print(f"Sold {quantity} shares of {stock.symbol} at ${stock.price}")
        else:
            print(f"You do not own any shares of {stock.symbol}")

    def display_portfolio(self):
        print(f"Available cash: ${self.money}")
        print("Stocks:")
        for symbol, quantity in self.stocks.items():
            stock = Stock(symbol, 100) # assuming a fixed price for display purposes
            print(f"{symbol}: {quantity} shares - ${stock.price} per share")


# Main program
apple_stock = Stock("AAPL", 150)
google_stock = Stock("GOOGL", 2000)

portfolio = Portfolio(10000)

while True:
    print("\nMenu:")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        stock_symbol = input("Enter stock symbol: ")
        stock_quantity = int(input("Enter quantity: "))
        stock = apple_stock if stock_symbol == "AAPL" else google_stock
        portfolio.buy_stock(stock, stock_quantity)
    elif choice == '2':
        stock_symbol = input("Enter stock symbol: ")
        stock_quantity = int(input("Enter quantity: "))
        stock = apple_stock if stock_symbol == "AAPL" else google_stock
        portfolio.sell_stock(stock, stock_quantity)
    elif choice == '3':
        portfolio.display_portfolio()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
