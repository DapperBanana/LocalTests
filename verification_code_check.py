
class Product:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
    
    def add_quantity(self, amount):
        self.quantity += amount
    
    def remove_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Error: Insufficient quantity")
    
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
    

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, id, name, quantity):
        product = Product(id, name, quantity)
        self.products.append(product)
    
    def remove_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return
        print("Error: Product not found")
    
    def find_product(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None
    
    def display_products(self):
        for product in self.products:
            product.display_info()


# Example usage of the inventory management system

# Create an inventory
inventory = Inventory()

# Add products
inventory.add_product(1, "Apple", 10)
inventory.add_product(2, "Orange", 5)
inventory.add_product(3, "Banana", 8)

# Display all products
inventory.display_products()

# Find a product by ID
product = inventory.find_product(2)
if product:
    product.display_info()

# Add quantity to a product
product = inventory.find_product(1)
if product:
    product.add_quantity(20)
    product.display_info()

# Remove quantity from a product
product = inventory.find_product(1)
if product:
    product.remove_quantity(5)
    product.display_info()

# Remove a product
inventory.remove_product(3)

# Display all products again
inventory.display_products()
