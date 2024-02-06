
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL, 
             age INTEGER NOT NULL, 
             address TEXT)''')

def create_employee(name, age, address):
    # Insert employee into database
    c.execute("INSERT INTO employees (name, age, address) VALUES (?, ?, ?)", (name, age, address))
    conn.commit()
    print("Employee created successfully")

def read_employees():
    # Fetch and print all employees
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Address:", row[3])
        print()

def update_employee(emp_id, name, age, address):
    # Update employee in database
    c.execute("UPDATE employees SET name = ?, age = ?, address = ? WHERE id = ?", (name, age, address, emp_id))
    conn.commit()
    print("Employee updated successfully")

def delete_employee(emp_id):
    # Delete employee from database
    c.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print("Employee deleted successfully")

# Perform CRUD operations
create_employee("John Doe", 30, "123 Main St")
create_employee("Jane Smith", 25, "456 Elm St")

read_employees()

update_employee(1, "John Doe", 35, "123 Updated St")

delete_employee(2)

read_employees()

# Close the connection
conn.close()
