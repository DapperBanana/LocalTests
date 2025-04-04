
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.shares = 0

stocks = {
    'AAPL': Stock('AAPL', 150),
    'GOOGL': Stock('GOOGL', 2000),
    'MSFT': Stock('MSFT', 300)
}

def buy_stock(symbol, shares):
    stock = stocks.get(symbol)
    if stock:
        cost = stock.price * shares
        stock.shares += shares
        print(f'Bought {shares} shares of {symbol} for ${cost}')
    else:
        print('Stock not found')

def sell_stock(symbol, shares):
    stock = stocks.get(symbol)
    if stock:
        if stock.shares >= shares:
            revenue = stock.price * shares
            stock.shares -= shares
            print(f'Sold {shares} shares of {symbol} for ${revenue}')
        else:
            print('Not enough shares to sell')
    else:
        print('Stock not found')

def display_portfolio():
    total_value = 0
    for symbol, stock in stocks.items():
        value = stock.price * stock.shares
        print(f'{symbol}: {stock.shares} shares, Total Value: ${value}')
        total_value += value
    print(f'Total Portfolio Value: ${total_value}')

while True:
    print('\n1. Buy Stock')
    print('2. Sell Stock')
    print('3. Display Portfolio')
    print('4. Exit')

    choice = input('\nEnter your choice: ')

    if choice == '1':
        symbol = input('Enter stock symbol: ')
        shares = int(input('Enter number of shares to buy: '))
        buy_stock(symbol, shares)
    elif choice == '2':
        symbol = input('Enter stock symbol: ')
        shares = int(input('Enter number of shares to sell: '))
        sell_stock(symbol, shares)
    elif choice == '3':
        display_portfolio()
    elif choice == '4':
        break
    else:
        print('Invalid choice')
