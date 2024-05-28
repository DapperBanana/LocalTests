
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
                print(f"Error: Not enough {item} in inventory")
        else:
            print(f"Error: {item} not found in inventory")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

# Create an instance of the Inventory class
inventory = Inventory()

# Add items to the inventory
inventory.add_item("Apple", 10)
inventory.add_item("Orange", 5)
inventory.add_item("Banana", 8)

# Display the inventory
inventory.display_inventory()

# Remove items from the inventory
inventory.remove_item("Apple", 3)
inventory.remove_item("Grape", 2)

# Display the updated inventory
inventory.display_inventory()
