
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

stocks = [
    Stock("AAPL", 150.00),
    Stock("GOOGL", 750.00),
    Stock("MSFT", 80.00),
    Stock("AMZN", 1000.00)
]

def display_stocks():
    for stock in stocks:
        print(f"{stock.name}: ${stock.price}")

def buy_stock(stock_name, quantity):
    for stock in stocks:
        if stock.name == stock_name:
            total_price = stock.price * quantity
            print(f"Bought {quantity} shares of {stock.name} for ${total_price}")
            return
    print("Stock not found.")

def sell_stock(stock_name, quantity):
    for stock in stocks:
        if stock.name == stock_name:
            total_price = stock.price * quantity
            print(f"Sold {quantity} shares of {stock.name} for ${total_price}")
            return
    print("Stock not found.")

running = True
while running:
    print("\nWelcome to the Stock Trading System:")
    print("1. Display available stocks")
    print("2. Buy stock")
    print("3. Sell stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_stocks()
    elif choice == "2":
        stock_name = input("Enter the stock name: ")
        quantity = int(input("Enter the quantity: "))
        buy_stock(stock_name, quantity)
    elif choice == "3":
        stock_name = input("Enter the stock name: ")
        quantity = int(input("Enter the quantity: "))
        sell_stock(stock_name, quantity)
    elif choice == "4":
        running = False
    else:
        print("Invalid choice. Please try again.")
