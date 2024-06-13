
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
                print(f"Not enough {item} in inventory")
        else:
            print(f"{item} not found in inventory")

    def check_inventory(self):
        if len(self.items) == 0:
            print("Inventory is empty")
        else:
            print("Current Inventory:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")

inventory = Inventory()

while True:
    print("\nOptions:")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Check inventory")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.add_item(item, quantity)
        print(f"{quantity} {item} added to inventory")

    elif choice == "2":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory.remove_item(item, quantity)

    elif choice == "3":
        inventory.check_inventory()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please select a valid option.")
