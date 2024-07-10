
balance = 10000
stocks = {
    "AAPL": 150,
    "GOOG": 75,
    "AMZN": 100
}

def buy_stock(stock_symbol, quantity):
    global balance, stocks
    if stock_symbol in stocks:
        price = stocks[stock_symbol]
        total_cost = price * quantity
        if total_cost <= balance:
            balance -= total_cost
            print(f"Bought {quantity} shares of {stock_symbol} for ${total_cost}")
        else:
            print("Insufficient balance")
    else:
        print("Stock symbol not found")

def sell_stock(stock_symbol, quantity):
    global balance, stocks
    if stock_symbol in stocks:
        price = stocks[stock_symbol]
        total_sell = price * quantity
        if quantity <= stocks[stock_symbol]:
            balance += total_sell
            print(f"Sold {quantity} shares of {stock_symbol} for ${total_sell}")
        else:
            print("Not enough shares to sell")
    else:
        print("Stock symbol not found")

def display_balance():
    print(f"Current Balance: ${balance}")

def display_portfolio():
    print("Current Portfolio:")
    for stock, quantity in stocks.items():
        print(f"{stock}: {quantity} shares")

while True:
    print("\n1. Buy Stock\n2. Sell Stock\n3. Display Balance\n4. Display Portfolio\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        stock_symbol = input("Enter stock symbol: ")
        quantity = int(input("Enter number of shares to buy: "))
        buy_stock(stock_symbol, quantity)
    elif choice == '2':
        stock_symbol = input("Enter stock symbol: ")
        quantity = int(input("Enter number of shares to sell: "))
        sell_stock(stock_symbol, quantity)
    elif choice == '3':
        display_balance()
    elif choice == '4':
        display_portfolio()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
