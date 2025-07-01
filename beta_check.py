
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
def create_customer(name, email):
    customer = {"name": name, "email": email}
    collection.insert_one(customer)
    print("Customer created successfully")

# Read
def get_customers():
    customers = collection.find()
    for customer in customers:
        print(customer)

# Update
def update_customer(name, new_email):
    query = {"name": name}
    new_values = {"$set": {"email": new_email}}
    collection.update_one(query, new_values)
    print("Customer updated successfully")

# Delete
def delete_customer(name):
    query = {"name": name}
    collection.delete_one(query)
    print("Customer deleted successfully")

# Test the CRUD operations
create_customer("Alice", "alice@example.com")
create_customer("Bob", "bob@example.com")
get_customers()
update_customer("Alice", "newalice@example.com")
delete_customer("Bob")
get_customers()

# Close MongoDB connection
client.close()
