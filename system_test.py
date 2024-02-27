
class Stock:
    def __init__(self, symbol, name, price, qty):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.qty = qty

    def buy(self, quantity):
        self.qty += quantity

    def sell(self, quantity):
        if self.qty >= quantity:
            self.qty -= quantity
            return True
        else:
            return False

    def __str__(self):
        return f"{self.symbol}: {self.name} - Price: ${self.price} - Qty: {self.qty}"

def main():
    stock1 = Stock("AAPL", "Apple Inc", 150.23, 10)
    stock2 = Stock("GOOGL", "Alphabet Inc", 2000.45, 5)

    stocks = [stock1, stock2]

    while True:
        print("\nAvailable Stocks:")
        for stock in stocks:
            print(stock)

        choice = input("\nEnter 'b' to buy, 's' to sell or 'q' to quit: ")

        if choice == 'q':
            break
        elif choice == 'b':
            symbol = input("Enter stock symbol to buy: ")
            quantity = int(input("Enter quantity to buy: "))
            for stock in stocks:
                if stock.symbol == symbol:
                    stock.buy(quantity)
                    print(f"Bought {quantity} shares of {stock.name}")
                    break
            else:
                print("Invalid stock symbol")
        elif choice == 's':
            symbol = input("Enter stock symbol to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            for stock in stocks:
                if stock.symbol == symbol:
                    if stock.sell(quantity):
                        print(f"Sold {quantity} shares of {stock.name}")
                    else:
                        print("Not enough shares to sell")
                    break
            else:
                print("Invalid stock symbol")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

