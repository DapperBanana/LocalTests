
class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.symbol} ({self.name}) - Price: ${self.price}"


class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add_stock(self, stock, quantity):
        self.stocks[stock] = self.stocks.get(stock, 0) + quantity
    
    def remove_stock(self, stock, quantity):
        if stock in self.stocks:
            self.stocks[stock] -= quantity
            if self.stocks[stock] <= 0:
                del self.stocks[stock]
    
    def get_value(self):
        value = 0
        for stock, quantity in self.stocks.items():
            value += stock.price * quantity
        return value


def buy_stock(portfolio, stock, quantity):
    portfolio.add_stock(stock, quantity)
    print(f"Bought {quantity} shares of {stock.symbol}.")


def sell_stock(portfolio, stock, quantity):
    if stock in portfolio.stocks:
        if portfolio.stocks[stock] >= quantity:
            portfolio.remove_stock(stock, quantity)
            print(f"Sold {quantity} shares of {stock.symbol}.")
        else:
            print("Not enough shares to sell.")
    else:
        print("Stock not found in portfolio.")


def main():
    apple = Stock("AAPL", "Apple Inc.", 150.0)
    microsoft = Stock("MSFT", "Microsoft Corporation", 250.0)
    google = Stock("GOOGL", "Alphabet Inc.", 350.0)

    portfolio = Portfolio()
    print("Welcome to the stock trading system!")
  
    while True:
        print("\nMenu:")
        print("1. Buy stock")
        print("2. Sell stock")
        print("3. View portfolio")
        print("4. Quit")
  
        choice = input("Enter your choice (1-4): ")
  
        if choice == "1":
            print("Available stocks:")
            print(apple)
            print(microsoft)
            print(google)
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            if symbol == "AAPL":
                buy_stock(portfolio, apple, quantity)
            elif symbol == "MSFT":
                buy_stock(portfolio, microsoft, quantity)
            elif symbol == "GOOGL":
                buy_stock(portfolio, google, quantity)
            else:
                print("Invalid stock symbol.")
  
        elif choice == "2":
            print("Your portfolio:")
            if len(portfolio.stocks) > 0:
                for stock, quantity in portfolio.stocks.items():
                    print(f"{stock.symbol} - Quantity: {quantity}")
                symbol = input("Enter stock symbol: ")
                quantity = int(input("Enter quantity: "))
                if symbol == "AAPL":
                    sell_stock(portfolio, apple, quantity)
                elif symbol == "MSFT":
                    sell_stock(portfolio, microsoft, quantity)
                elif symbol == "GOOGL":
                    sell_stock(portfolio, google, quantity)
                else:
                    print("Invalid stock symbol.")
            else:
                print("Your portfolio is empty.")
  
        elif choice == "3":
            print("Your portfolio:")
            if len(portfolio.stocks) > 0:
                for stock, quantity in portfolio.stocks.items():
                    print(f"{stock.symbol} ({stock.name}) - Quantity: {quantity}")
                print(f"Total portfolio value: ${portfolio.get_value()}")
            else:
                print("Your portfolio is empty.")
  
        elif choice == "4":
            print("Thank you for using the stock trading system!")
            break
  
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
