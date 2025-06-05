
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
            else:
                print("Not enough quantity in stock.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

# Create an instance of Inventory
inventory = Inventory()

# Add items to inventory
inventory.add_item("apple", 10)
inventory.add_item("banana", 5)
inventory.add_item("orange", 15)

# Display current inventory
inventory.display_inventory()

# Remove items from inventory
inventory.remove_item("apple", 3)
inventory.remove_item("banana", 7)
inventory.remove_item("grapes", 2)

# Display updated inventory
inventory.display_inventory()
