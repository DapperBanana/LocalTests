
stocks = {
    'AAPL': 100,
    'GOOGL': 200,
    'MSFT': 150,
    'AMZN': 300
}

balance = 1000

while True:
    print("Available Stocks:")
    for stock, price in stocks.items():
        print(f"{stock} - ${price}")

    print(f"Your current balance is ${balance}")

    choice = input("Enter the stock symbol you want to buy/sell (or type 'quit' to exit): ")

    if choice == 'quit':
        print("Exiting program...")
        break

    if choice in stocks:
        action = input("Do you want to buy or sell? ")
        quantity = int(input("Enter the quantity: "))

        if action == 'buy':
            cost = stocks[choice] * quantity
            if cost <= balance:
                balance -= cost
                stocks[choice] += quantity
                print(f"You bought {quantity} shares of {choice}")
            else:
                print("Insufficient balance")
        elif action == 'sell':
            if stocks[choice] >= quantity:
                balance += stocks[choice] * quantity
                stocks[choice] -= quantity
                print(f"You sold {quantity} shares of {choice}")
            else:
                print("Insufficient shares")
        else:
            print("Invalid action")
    else:
        print("Invalid stock symbol")

