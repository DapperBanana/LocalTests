
class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

class Portfolio:
    def __init__(self):
        self.stocks = []

    def buy_stock(self, symbol, price, quantity):
        stock = Stock(symbol, price, quantity)
        self.stocks.append(stock)

    def sell_stock(self, symbol, quantity):
        for stock in self.stocks:
            if stock.symbol == symbol:
                if stock.quantity >= quantity:
                    stock.quantity -= quantity
                    print(f"Sold {quantity} shares of {symbol} at ${stock.price}")
                    break
                else:
                    print("Not enough shares to sell")
                    break
        else:
            print(f"No {symbol} stock in portfolio")

    def portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.price * stock.quantity
        print(f"Portfolio value: ${total_value}")

portfolio = Portfolio()

while True:
    print("\nStock Trading System Menu:")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio Value")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        symbol = input("Enter stock symbol: ")
        price = float(input("Enter stock price: "))
        quantity = int(input("Enter quantity to buy: "))
        portfolio.buy_stock(symbol, price, quantity)

    elif choice == "2":
        symbol = input("Enter stock symbol: ")
        quantity = int(input("Enter quantity to sell: "))
        portfolio.sell_stock(symbol, quantity)

    elif choice == "3":
        portfolio.portfolio_value()

    elif choice == "4":
        break
