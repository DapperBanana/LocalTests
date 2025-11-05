
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('crud_operations.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL)''')

# Create
def create_product(name, price):
    cursor.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
    conn.commit()
    print("Product created successfully")

# Read
def read_products():
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    for product in products:
        print(product)

# Update
def update_product(product_id, new_name, new_price):
    cursor.execute('''UPDATE products SET name = ?, price = ? WHERE id = ?''', (new_name, new_price, product_id))
    conn.commit()
    print("Product updated successfully")

# Delete
def delete_product(product_id):
    cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
    conn.commit()
    print("Product deleted successfully")

# Example usage
create_product("Laptop", 999.99)
create_product("Phone", 499.99)
read_products()

update_product(1, "New Laptop", 1099.99)
read_products()

delete_product(2)
read_products()

# Close connection
conn.close()
