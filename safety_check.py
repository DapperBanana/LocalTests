
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

    def buy(self, num_shares):
        self.shares += num_shares
        
    def sell(self, num_shares):
        if num_shares <= self.shares:
            self.shares -= num_shares
            return True
        else:
            return False

    def get_value(self):
        return self.price * self.shares

def main():
    stock = Stock("AAPL", 150.00)
    
    while True:
        print("\nStock Trading System")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. Check Portfolio")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num_shares = int(input("Enter the number of shares to buy: "))
            stock.buy(num_shares)
            print(f"Bought {num_shares} shares of {stock.symbol} at ${stock.price} each.")
            
        elif choice == "2":
            num_shares = int(input("Enter the number of shares to sell: "))
            if stock.sell(num_shares):
                print(f"Sold {num_shares} shares of {stock.symbol} at ${stock.price} each.")
            else:
                print("Not enough shares to sell.")
                
        elif choice == "3":
            print(f"Portfolio Value: ${stock.get_value()}")
            
        elif choice == "4":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
