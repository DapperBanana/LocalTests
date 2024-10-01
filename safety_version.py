
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

    def buy(self, num_shares):
        self.shares += num_shares

    def sell(self, num_shares):
        if num_shares > self.shares:
            print("Error: Not enough shares to sell")
        else:
            self.shares -= num_shares

    def calculate_value(self):
        return self.shares * self.price

def main():
    stock = Stock("AAPL", 150.0)

    while True:
        print("\nStock: {} - Price: ${:.2f} - Shares: {}".format(stock.symbol, stock.price, stock.shares))
        action = input("Do you want to (b)uy, (s)ell, or (q)uit? ").lower()

        if action == "b":
            num_shares = int(input("Enter the number of shares to buy: "))
            stock.buy(num_shares)
        elif action == "s":
            num_shares = int(input("Enter the number of shares to sell: "))
            stock.sell(num_shares)
        elif action == "q":
            break
        else:
            print("Invalid input. Please enter 'b' to buy, 's' to sell, or 'q' to quit.")

    print("\nFinal Stock Portfolio:")
    print("Stock: {} - Shares: {} - Total Value: ${:.2f}".format(stock.symbol, stock.shares, stock.calculate_value()))

if __name__ == "__main__":
    main()
