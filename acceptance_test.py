
import random

# Define starting stock prices
stock_prices = {
    "AAPL": 150.0,
    "GOOGL": 2000.0,
    "AMZN": 3000.0,
    "TSLA": 600.0
}

# Main trading function
def trade_stock(stock, action, quantity):
    price = stock_prices[stock]
    
    if action == "buy":
        cost = price * quantity
        print(f"Bought {quantity} shares of {stock} at ${price} each for a total cost of ${cost}")
    elif action == "sell":
        revenue = price * quantity
        print(f"Sold {quantity} shares of {stock} at ${price} each for a total revenue of ${revenue}")
    else:
        print("Invalid action. Please use 'buy' or 'sell'.")

# Main program loop
while True:
    print("\nCurrent stock prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    
    stock = input("\nEnter the stock symbol you would like to trade (or enter 'quit' to exit): ").upper()
    
    if stock == "QUIT":
        break
    
    action = input("Enter the action you would like to take (buy/sell): ")
    quantity = int(input("Enter the quantity of shares you would like to trade: "))
    
    if stock in stock_prices:
        trade_stock(stock, action, quantity)
    else:
        print("Invalid stock symbol. Please choose from the available options.")
