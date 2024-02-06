
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | ${self.price} | Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                return True
        return False

    def search_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for product in self.products:
                print(product)


def main():
    inventory = Inventory()

    while True:
        print("--------------------")
        print("1. Add product")
        print("2. Remove product")
        print("3. Search product")
        print("4. Display inventory")
        print("5. Exit")
        print("--------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            inventory.add_product(product)
            print("Product added successfully.")

        elif choice == "2":
            name = input("Enter product name to remove: ")
            if inventory.remove_product(name):
                print("Product removed successfully.")
            else:
                print("Product not found.")

        elif choice == "3":
            name = input("Enter product name to search: ")
            product = inventory.search_product(name)
            if product:
                print("Product found:")
                print(product)
            else:
                print("Product not found.")

        elif choice == "4":
            inventory.display_inventory()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
