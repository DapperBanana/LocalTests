
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
            else:
                print("Error: Not enough quantity available.")
        else:
            print("Error: Item not found in inventory.")
    
    def display_inventory(self):
        print("Current Inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity}")

# Main program
inv = Inventory()

while True:
    print("\n1. Add Item to Inventory")
    print("2. Remove Item from Inventory")
    print("3. Display Inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inv.add_item(item_name, quantity)
    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inv.remove_item(item_name, quantity)
    elif choice == '3':
        inv.display_inventory()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
