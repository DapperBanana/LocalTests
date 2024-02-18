
class StockTradingSystem:
    def __init__(self):
        self.balance = 10000
        self.stocks = {'AAPL': 10, 'GOOGL': 5, 'MSFT': 8}

    def buy_stock(self, stock, quantity):
        if stock in self.stocks.keys():
            stock_price = get_stock_price(stock)
            total_cost = stock_price * quantity
            if total_cost <= self.balance:
                self.stocks[stock] += quantity
                self.balance -= total_cost
                print(f"Bought {quantity} shares of {stock} at ${stock_price} per share")
            else:
                print("Insufficient balance to buy stock")
        else:
            print("Stock not found")

    def sell_stock(self, stock, quantity):
        if stock in self.stocks.keys():
            stock_price = get_stock_price(stock)
            if self.stocks[stock] >= quantity:
                total_sell_value = stock_price * quantity
                self.stocks[stock] -= quantity
                self.balance += total_sell_value
                print(f"Sold {quantity} shares of {stock} at ${stock_price} per share")
            else:
                print("Not enough shares to sell")
        else:
            print("Stock not found")

    def get_stock_price(stock):
        # Function to get stock price from API or database
        return 100

# Main program
system = StockTradingSystem()

while True:
    print("1. Buy stock")
    print("2. Sell stock")
    print("3. Check balance")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        stock = input("Enter stock symbol: ")
        quantity = int(input("Enter quantity: "))
        system.buy_stock(stock, quantity)
    elif choice == '2':
        stock = input("Enter stock symbol: ")
        quantity = int(input("Enter quantity: "))
        system.sell_stock(stock, quantity)
    elif choice == '3':
        print(f"Current balance: ${system.balance}")
        print(f"Stock holdings: {system.stocks}")
    elif choice == '4':
        break
    else:
        print("Invalid choice")
