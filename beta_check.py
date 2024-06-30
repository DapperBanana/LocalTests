
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]

# Create operation
def create_customer(name, email):
    new_customer = {"name": name, "email": email}
    col.insert_one(new_customer)

# Read operation
def read_all_customers():
    for customer in col.find():
        print(customer)

# Update operation
def update_customer(name, new_email):
    query = {"name": name}
    new_values = {"$set": {"email": new_email}}
    col.update_one(query, new_values)

# Delete operation
def delete_customer(name):
    query = {"name": name}
    col.delete_one(query)

# Perform CRUD operations
create_customer("Alice", "alice@example.com")
create_customer("Bob", "bob@example.com")
read_all_customers()

update_customer("Alice", "alice@example.net")
read_all_customers()

delete_customer("Bob")
read_all_customers()

client.close()
