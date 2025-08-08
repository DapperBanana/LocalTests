
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
new_customer = { "name": "John", "address": "Highway 37" }
inserted_customer = collection.insert_one(new_customer)

print("Customer inserted with id:", inserted_customer.inserted_id)

# Read
find_customer = collection.find_one({ "name": "John" })
print("Customer found:", find_customer)

# Update
update_customer = { "$set": { "address": "Main Street 123" } }
collection.update_one({ "name": "John" }, update_customer)

# Read updated customer
find_customer = collection.find_one({ "name": "John" })
print("Updated customer:", find_customer)

# Delete
collection.delete_one({ "name": "John" })

# Verify deletion
verify_customer = collection.find_one({ "name": "John" })
print("Customer after deletion:", verify_customer)
