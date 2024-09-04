
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.quantity = 0

    def buy(self, qty):
        self.quantity += qty

    def sell(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
            return True
        else:
            print("Not enough shares to sell")
            return False

    def get_value(self):
        return self.quantity * self.price

stocks = {
    'AAPL': Stock('AAPL', 150),
    'GOOGL': Stock('GOOGL', 2500),
    'MSFT': Stock('MSFT', 300)
}

cash = 10000

while True:
    print("\nAvailable cash: $", cash)
    print("Stocks:")
    for symbol, stock in stocks.items():
        print(f"{symbol}: {stock.quantity} shares, Price: ${stock.price}")

    action = input("\nEnter 'buy [symbol] [quantity]' or 'sell [symbol] [quantity]' or 'quit': ")
    if action == 'quit':
        break
    else:
        parts = action.split(' ')
        if len(parts) != 3:
            print("Invalid input")
            continue

        command, symbol, qty = parts
        try:
            qty = int(qty)
        except ValueError:
            print("Invalid quantity")
            continue

        if symbol not in stocks:
            print("Invalid symbol")
            continue

        if command == 'buy':
            stock = stocks[symbol]
            total_cost = stock.price * qty
            if total_cost > cash:
                print("Not enough cash to buy")
                continue
            stock.buy(qty)
            cash -= total_cost
            print(f"Bought {qty} shares of {symbol} for ${total_cost}")
        elif command == 'sell':
            stock = stocks[symbol]
            if not stock.sell(qty):
                continue
            total_sale = stock.price * qty
            cash += total_sale
            print(f"Sold {qty} shares of {symbol} for ${total_sale}")
        else:
            print("Invalid command")
