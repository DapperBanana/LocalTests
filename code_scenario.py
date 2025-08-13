
class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, price, quantity):
        item = InventoryItem(name, price, quantity)
        self.inventory.append(item)

    def remove_item(self, name):
        for item in self.inventory:
            if item.name == name:
                self.inventory.remove(item)

    def update_quantity(self, name, new_quantity):
        for item in self.inventory:
            if item.name == name:
                item.quantity = new_quantity

    def display_inventory(self):
        print("Current Inventory:")
        for item in self.inventory:
            print(f"{item.name} - Price: {item.price}, Quantity: {item.quantity}")

# Sample usage
inventory_manager = InventoryManager()

inventory_manager.add_item("Apple", 0.5, 100)
inventory_manager.add_item("Banana", 0.3, 50)

inventory_manager.display_inventory()

inventory_manager.update_quantity("Apple", 80)
inventory_manager.remove_item("Banana")

inventory_manager.display_inventory()
