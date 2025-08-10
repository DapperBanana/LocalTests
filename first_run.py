
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.quantity = 0
        
    def buy(self, qty):
        self.quantity += qty
        print(f"Bought {qty} shares of {self.symbol}")
        
    def sell(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
            print(f"Sold {qty} shares of {self.symbol}")
        else:
            print("Not enough shares to sell")
        
    def get_value(self):
        return self.quantity * self.price
        
apple = Stock("AAPL", 150.25)
google = Stock("GOOG", 2000.50)

while True:
    print("Available Stocks:")
    print("1. AAPL - Price: $150.25")
    print("2. GOOG - Price: $2000.50")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        qty = int(input("Enter quantity to buy/sell for AAPL: "))
        action = input("Buy or Sell? ").lower()
        if action == "buy":
            apple.buy(qty)
        elif action == "sell":
            apple.sell(qty)
    elif choice == "2":
        qty = int(input("Enter quantity to buy/sell for GOOG: "))
        action = input("Buy or Sell? ").lower()
        if action == "buy":
            google.buy(qty)
        elif action == "sell":
            google.sell(qty)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Try again.")

print(f"Final Portfolio Value:")
print(f"AAPL: ${apple.get_value()}")
print(f"GOOG: ${google.get_value()}")
