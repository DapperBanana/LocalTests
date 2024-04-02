
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
            print("Stock not found in portfolio")

    def show_portfolio(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock = Stock(symbol, 100) # In reality, you would fetch the real-time stock price here
            value = stock.price * quantity
            total_value += value
            print(f"{symbol}: {quantity} shares - ${value}")
        
        print(f"Total portfolio value: ${total_value}")

# Main program
portfolio = Portfolio()

while True:
    print("\n1. Buy Stock\n2. Sell Stock\n3. Show Portfolio\n4. Quit")
    choice = input("Enter choice: ")

    if choice == '1':
        symbol = input("Enter stock symbol: ")
        price = float(input("Enter stock price: "))
        quantity = int(input("Enter quantity to buy: "))
        portfolio.buy_stock(symbol, price, quantity)

    elif choice == '2':
        symbol = input("Enter stock symbol: ")
        price = float(input("Enter stock price: "))
        quantity = int(input("Enter quantity to sell: "))
        portfolio.sell_stock(symbol, price, quantity)

    elif choice == '3':
        portfolio.show_portfolio()

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please try again.")
