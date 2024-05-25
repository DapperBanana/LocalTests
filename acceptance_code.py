
import random

# Initialize variables
balance = 1000
stock_price = 100
portfolio = 0

while True:
    print("\nBalance: ${}".format(balance))
    print("Stock Price: ${}".format(stock_price))
    print("Portfolio: {}".format(portfolio))

    action = input("\nBuy (b) / Sell (s) / Quit (q): ")

    if action == 'b':
        shares = int(input("Enter number of shares to buy: "))
        cost = shares * stock_price
        if cost > balance:
            print("Not enough balance to buy {} shares.".format(shares))
        else:
            balance -= cost
            portfolio += shares
            print("Bought {} shares for ${} each.".format(shares, stock_price))
    elif action == 's':
        shares = int(input("Enter number of shares to sell: "))
        if shares > portfolio:
            print("Not enough shares to sell {} shares.".format(shares))
        else:
            revenue = shares * stock_price
            balance += revenue
            portfolio -= shares
            print("Sold {} shares for ${} each.".format(shares, stock_price))
    elif action == 'q':
        print("\nFinal Balance: ${}".format(balance))
        print("Final Portfolio: {}".format(portfolio))
        break
    else:
        print("Invalid action. Please try again.")

    # Update stock price randomly
    stock_price += random.randint(-5, 5)

