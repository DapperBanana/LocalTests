
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print("Not enough quantity in stock.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

inventory = Inventory()

while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.add_item(item_name, quantity)
    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        inventory.remove_item(item_name, quantity)
    elif choice == '3':
        inventory.display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
