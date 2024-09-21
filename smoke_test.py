
class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            print(f"Error: Not enough {item} in inventory")

    def check_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

# create an instance of the Inventory class
inventory = Inventory()

# add items to the inventory
inventory.add_item("apple", 10)
inventory.add_item("banana", 5)
inventory.add_item("orange", 8)

# check the current inventory
inventory.check_inventory()

# remove items from the inventory
inventory.remove_item("apple", 3)
inventory.remove_item("banana", 2)
inventory.remove_item("grapes", 5)

# check the current inventory again
inventory.check_inventory()
