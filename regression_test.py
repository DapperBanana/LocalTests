
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def buy_stock(self, stock_symbol, num_shares):
        if stock_symbol not in self.stocks:
            print("Stock not found.")
            return
        stock = self.stocks[stock_symbol]
        total_price = stock.price * num_shares
        if total_price > cash_balance:
            print("Insufficient funds.")
        else:
            stock.shares += num_shares
            cash_balance -= total_price
            print(f"Bought {num_shares} shares of {stock.symbol}.")

    def sell_stock(self, stock_symbol, num_shares):
        if stock_symbol not in self.stocks:
            print("Stock not found.")
            return
        stock = self.stocks[stock_symbol]
        if stock.shares < num_shares:
            print("Not enough shares to sell.")
        else:
            stock.shares -= num_shares
            cash_balance += stock.price * num_shares
            print(f"Sold {num_shares} shares of {stock.symbol}.")

cash_balance = 1000
stocks = {
    "AAPL": Stock("AAPL", 150),
    "GOOGL": Stock("GOOGL", 2500),
    "AMZN": Stock("AMZN", 3500)
}
portfolio = Portfolio()
portfolio.stocks = stocks

while True:
    print(f"Cash Balance: ${cash_balance}")
    print("Stocks in Portfolio:")
    for symbol, stock in stocks.items():
        print(f"{stock.symbol}: {stock.price} - {stock.shares} shares")

    action = input("Buy or sell a stock? (b/s): ").lower()
    if action == 'b':
        stock_symbol = input("Enter stock symbol: ").upper()
        num_shares = int(input("Enter number of shares to buy: "))
        portfolio.buy_stock(stock_symbol, num_shares)
    elif action == 's':
        stock_symbol = input("Enter stock symbol: ").upper()
        num_shares = int(input("Enter number of shares to sell: "))
        portfolio.sell_stock(stock_symbol, num_shares)
    else:
        print("Invalid action. Please try again.")
