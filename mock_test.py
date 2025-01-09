
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
            else:
                print("Not enough quantity available")
        else:
            print("Item not found in inventory")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

inventory = Inventory()
while True:
    print("\n1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Quit")

    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.add_item(item, quantity)
    elif choice == '2':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        inventory.remove_item(item, quantity)
    elif choice == '3':
        inventory.display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
