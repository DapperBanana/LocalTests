
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER)''')

# Function to insert data into the database
def create_employee(name, age):
    cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Employee created successfully")

# Function to read data from the database
def get_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to update data in the database
def update_employee(id, name, age):
    cursor.execute("UPDATE employees SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    print("Employee updated successfully")

# Function to delete data from the database
def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()
    print("Employee deleted successfully")

# Example usage of the CRUD functions
create_employee('Alice', 30)
create_employee('Bob', 25)
get_employees()
update_employee(1, 'Alice Smith', 32)
delete_employee(2)
get_employees()

# Close the database connection
conn.close()
