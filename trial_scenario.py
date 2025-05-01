
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def buy_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity

    def sell_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            if self.stocks[stock.symbol] >= quantity:
                self.stocks[stock.symbol] -= quantity
                return True
            else:
                return False
        else:
            return False

def main():
    apple = Stock("AAPL", 150.0)
    google = Stock("GOOGL", 2500.0)
    portfolio = Portfolio()

    while True:
        print("----------")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            if symbol == "AAPL":
                portfolio.buy_stock(apple, quantity)
                print("Bought {} shares of AAPL".format(quantity))
            elif symbol == "GOOGL":
                portfolio.buy_stock(google, quantity)
                print("Bought {} shares of GOOGL".format(quantity))

        elif choice == 2:
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            if symbol == "AAPL":
                if portfolio.sell_stock(apple, quantity):
                    print("Sold {} shares of AAPL".format(quantity))
                else:
                    print("Not enough shares of AAPL to sell")
            elif symbol == "GOOGL":
                if portfolio.sell_stock(google, quantity):
                    print("Sold {} shares of GOOGL".format(quantity))
                else:
                    print("Not enough shares of GOOGL to sell")

        elif choice == 3:
            print("Portfolio:")
            for symbol, quantity in portfolio.stocks.items():
                if symbol == "AAPL":
                    print("AAPL: {} shares".format(quantity))
                elif symbol == "GOOGL":
                    print("GOOGL: {} shares".format(quantity))

        elif choice == 4:
            break

if __name__ == "__main__":
    main()
