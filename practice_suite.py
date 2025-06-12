
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                if self.inventory[item] == 0:
                    del self.inventory[item]
            else:
                print(f"Not enough {item} in inventory.")
        else:
            print(f"{item} not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

# Main program
inventory = Inventory()

while True:
    print("\nWelcome to the Inventory Management System")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.add_item(item, quantity)
    elif choice == '2':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.remove_item(item, quantity)
    elif choice == '3':
        inventory.display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
