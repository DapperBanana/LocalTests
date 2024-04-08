
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, name):
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)
    
    def update_quantity(self, name, quantity):
        for item in self.inventory:
            if item.name == name:
                item.quantity = quantity
    
    def display_inventory(self):
        print("Current Inventory:")
        for item in self.inventory:
            print(f"{item.name}: {item.quantity}")

# Create an instance of the Inventory class
inventory = Inventory()

# Add some items to the inventory
inventory.add_item(InventoryItem("Apples", 10))
inventory.add_item(InventoryItem("Bananas", 15))
inventory.add_item(InventoryItem("Oranges", 20))

# Display the current inventory
inventory.display_inventory()

# Update the quantity of bananas
inventory.update_quantity("Bananas", 20)

# Display the updated inventory
inventory.display_inventory()

# Remove oranges from the inventory
inventory.remove_item("Oranges")

# Display the final inventory
inventory.display_inventory()
