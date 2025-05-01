
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

stocks = {
    'AAPL': Stock('AAPL', 150),
    'GOOGL': Stock('GOOGL', 2000),
    'AMZN': Stock('AMZN', 3000),
}

portfolio = {}

def buy_stock(symbol, num_shares):
    if symbol in stocks:
        stock = stocks[symbol]
        if stock.price * num_shares <= portfolio.get('cash', 0):
            portfolio['cash'] -= stock.price * num_shares
            stock.shares += num_shares
            print(f"Bought {num_shares} shares of {symbol}")
        else:
            print("Not enough cash to buy stock")
    else:
        print("Stock symbol not found")

def sell_stock(symbol, num_shares):
    if symbol in stocks:
        stock = stocks[symbol]
        if stock.shares >= num_shares:
            portfolio['cash'] += stock.price * num_shares
            stock.shares -= num_shares
            print(f"Sold {num_shares} shares of {symbol}")
        else:
            print("Not enough shares to sell")
    else:
        print("Stock symbol not found")

def show_portfolio():
    print("Portfolio")
    for symbol, stock in stocks.items():
        if stock.shares > 0:
            print(f"{symbol}: {stock.shares} shares")

def show_cash():
    print(f"Cash: {portfolio.get('cash', 0)}")

def main():
    while True:
        print("\nMenu:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. Show Portfolio")
        print("4. Show Cash")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            num_shares = int(input("Enter number of shares to buy: "))
            buy_stock(symbol, num_shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ")
            num_shares = int(input("Enter number of shares to sell: "))
            sell_stock(symbol, num_shares)
        elif choice == '3':
            show_portfolio()
        elif choice == '4':
            show_cash()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
