
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - Quantity: {self.quantity}"

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, name):
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
                return True
        return False

    def update_quantity(self, name, quantity):
        for item in self.inventory:
            if item.name == name:
                item.quantity = quantity
                return True
        return False

    def print_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item in self.inventory:
            print(item)

def main():
    inventory_manager = InventoryManager()

    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. Print inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = Item(name, price, quantity)
            inventory_manager.add_item(item)
            print(f"{item.name} added to inventory.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            if inventory_manager.remove_item(name):
                print(f"{name} removed from inventory.")
            else:
                print(f"{name} not found in inventory.")

        elif choice == "3":
            name = input("Enter item name to update quantity: ")
            quantity = int(input("Enter new quantity: "))
            if inventory_manager.update_quantity(name, quantity):
                print(f"{name} quantity updated.")
            else:
                print(f"{name} not found in inventory.")

        elif choice == "4":
            inventory_manager.print_inventory()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
