
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name}: {self.quantity}"

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                break

    def update_quantity(self, item_name, amount):
        for item in self.inventory:
            if item.name == item_name:
                item.update_quantity(amount)
                break

    def display_inventory(self):
        for item in self.inventory:
            print(item)

# Create a new inventory management system
inventory_system = InventoryManagementSystem()

# Add items to inventory
inventory_system.add_item(InventoryItem("Apple", 10))
inventory_system.add_item(InventoryItem("Banana", 20))
inventory_system.add_item(InventoryItem("Orange", 15))

# Update quantities
inventory_system.update_quantity("Apple", 5)
inventory_system.update_quantity("Banana", -3)

# Remove an item
inventory_system.remove_item("Orange")

# Display inventory
inventory_system.display_inventory()
