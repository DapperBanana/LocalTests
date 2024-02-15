
class InventoryItem:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def __str__(self):
        return f'{self.item_name}: {self.quantity}'


class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_item(self, item_name, quantity):
        item = self.find_item(item_name)
        if item:
            item.update_quantity(quantity)
        else:
            self.inventory.append(InventoryItem(item_name, quantity))

    def remove_item(self, item_name, quantity):
        item = self.find_item(item_name)
        if item:
            if item.quantity >= quantity:
                item.update_quantity(-quantity)
            else:
                print("Insufficient quantity.")
        else:
            print("Item not found.")

    def find_item(self, item_name):
        for item in self.inventory:
            if item.item_name == item_name:
                return item
        return None

    def print_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item in self.inventory:
                print(item)

# Example usage
inventory_manager = InventoryManager()
inventory_manager.add_item("Apple", 10)
inventory_manager.add_item("Banana", 5)
inventory_manager.print_inventory()

inventory_manager.add_item("Apple", 5)
inventory_manager.remove_item("Banana", 3)
inventory_manager.remove_item("Orange", 2)
inventory_manager.print_inventory()
