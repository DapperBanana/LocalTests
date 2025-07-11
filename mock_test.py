
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def buy_stock(self, symbol, price, shares):
        if symbol in self.stocks:
            self.stocks[symbol].shares += shares
        else:
            self.stocks[symbol] = Stock(symbol, price)
            self.stocks[symbol].shares = shares

    def sell_stock(self, symbol, shares):
        if symbol in self.stocks:
            if self.stocks[symbol].shares >= shares:
                self.stocks[symbol].shares -= shares
            else:
                print("Not enough shares to sell")
        else:
            print("Stock not found in portfolio")

    def show_portfolio(self):
        for symbol, stock in self.stocks.items():
            print(f"Stock: {symbol}, Shares: {stock.shares}, Price: {stock.price}")

def main():
    portfolio = Portfolio()

    while True:
        print("\n1. Buy Stock\n2. Sell Stock\n3. Show Portfolio\n4. Exit")
        choice = input("Enter option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            price = float(input("Enter stock price: "))
            shares = int(input("Enter number of shares to buy: "))
            portfolio.buy_stock(symbol, price, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares to sell: "))
            portfolio.sell_stock(symbol, shares)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
