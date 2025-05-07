
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
            else:
                print("Not enough quantity in inventory")
        else:
            print("Item not found in inventory")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

# Creating an instance of Inventory
inventory = Inventory()

# Adding items to the inventory
inventory.add_item("apple", 10)
inventory.add_item("banana", 20)
inventory.add_item("orange", 15)

# Displaying the inventory
inventory.display_inventory()

# Removing items from the inventory
inventory.remove_item("apple", 5)
inventory.remove_item("grape", 5)

# Displaying the updated inventory
inventory.display_inventory()
