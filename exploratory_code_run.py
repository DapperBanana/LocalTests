
class Stock:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True
        else:
            return False

stocks = {
    'AAPL': Stock('AAPL', 150, 10),
    'GOOGL': Stock('GOOGL', 2000, 5),
    'AMZN': Stock('AMZN', 3500, 8)
}

def display_stocks():
    print("Available stocks:")
    for stock in stocks.values():
        print(f"{stock.name}: Price - ${stock.price}, Quantity - {stock.quantity}")

def trade():
    display_stocks()
    
    choice = input("Enter the stock symbol you want to trade: ").upper()
    action = input("Do you want to buy or sell? ").lower()
    
    if choice in stocks:
        stock = stocks[choice]
        if action == 'buy':
            quantity = int(input("Enter the quantity you want to buy: "))
            stock.buy(quantity)
        elif action == 'sell':
            quantity = int(input("Enter the quantity you want to sell: "))
            if stock.sell(quantity):
                print("Sold successfully")
            else:
                print("Insufficient quantity")
        else:
            print("Invalid action")
    else:
        print("Invalid stock symbol")

while True:
    trade()
    continue_trading = input("Do you want to continue trading? (y/n) ")
    if continue_trading.lower() != 'y':
        break
