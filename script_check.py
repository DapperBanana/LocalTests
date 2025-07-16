
class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def buy(self, quantity):
        self.quantity += quantity
    
    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return True
        else:
            return False

stocks = {
    'AAPL': Stock('Apple', 150.0, 10),
    'GOOGL': Stock('Google', 2000.0, 5),
    'AMZN': Stock('Amazon', 3000.0, 3)
}

def show_stock():
    for symbol, stock in stocks.items():
        print(f"{symbol}: {stock.name} - Price: ${stock.price} - Quantity: {stock.quantity}")

def main():
    while True:
        show_stock()
        print("\nOptions:")
        print("1. Buy")
        print("2. Sell")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol to buy: ")
            quantity = int(input("Enter quantity to buy: "))
            stocks[symbol].buy(quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            if not stocks[symbol].sell(quantity):
                print("Not enough stocks to sell!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
