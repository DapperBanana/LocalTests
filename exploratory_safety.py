
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
                print(f"Not enough {item_name} in inventory")
        else:
            print(f"{item_name} not found in inventory")

    def display_inventory(self):
        print("Inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity}")

# Create an instance of Inventory class
inventory = Inventory()

# Add items to inventory
inventory.add_item("Apple", 10)
inventory.add_item("Banana", 5)

# Display inventory
inventory.display_inventory()

# Remove items from inventory
inventory.remove_item("Apple", 3)
inventory.remove_item("Orange", 2)

# Display inventory again
inventory.display_inventory()
