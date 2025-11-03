
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock, quantity):
        self.stocks[stock.symbol] = {'stock': stock, 'quantity': quantity}

    def buy_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            print("Stock not found in portfolio")

    def sell_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if quantity <= self.stocks[symbol]['quantity']:
                self.stocks[symbol]['quantity'] -= quantity
            else:
                print("Not enough stock in portfolio")
        else:
            print("Stock not found in portfolio")

    def portfolio_value(self):
        total_value = 0
        for stock_data in self.stocks.values():
            total_value += stock_data['quantity'] * stock_data['stock'].price
        return total_value

def main():
    apple_stock = Stock('AAPL', 150)
    microsoft_stock = Stock('MSFT', 200)

    portfolio = Portfolio()
    portfolio.add_stock(apple_stock, 10)
    portfolio.add_stock(microsoft_stock, 5)

    while True:
        print("\n1. Buy Stock")
        print("2. Sell Stock")
        print("3. Check Portfolio Value")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.buy_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.sell_stock(symbol, quantity)
        elif choice == '3':
            print("Portfolio Value: $", portfolio.portfolio_value())
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
