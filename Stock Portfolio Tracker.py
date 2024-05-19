class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, price):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
            self.stocks[symbol]['price'] = price
        else:
            self.stocks[symbol] = {'quantity': quantity, 'price': price}

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol]['quantity'] > quantity:
                self.stocks[symbol]['quantity'] -= quantity
            elif self.stocks[symbol]['quantity'] == quantity:
                del self.stocks[symbol]
            else:
                print("Not enough stock to remove")
        else:
            print("Stock not in portfolio")

    def get_portfolio_value(self):
        total_value = 0.0
        for symbol, data in self.stocks.items():
            total_value += data['quantity'] * data['price']
        return total_value

    def show_portfolio(self):
        print("Portfolio:")
        for symbol, data in self.stocks.items():
            print(f"Stock: {symbol}, Quantity: {data['quantity']}, Price: {data['price']:.2f}")

if __name__ == "__main__":
    portfolio = Portfolio()

    while True:
        print("\nPortfolio Tracker Menu")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Get Portfolio Value")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol to add: ").upper()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per stock: "))
            portfolio.add_stock(symbol, quantity, price)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            value = portfolio.get_portfolio_value()
            print(f"Total Portfolio Value: ${value:.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
