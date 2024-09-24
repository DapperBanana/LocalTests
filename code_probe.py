
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
data = {"name": "John", "address": "Highway 37"}
new_doc = collection.insert_one(data)
print(new_doc.inserted_id)

# Read
customer = collection.find_one({"name": "John"})
print(customer)

# Update
query = {"name": "John"}
new_values = {"$set": {"address": "Highway 34"}}
collection.update_one(query, new_values)

updated_customer = collection.find_one({"name": "John"})
print(updated_customer)

# Delete
collection.delete_one({"name": "John"})

deleted_customer = collection.find_one({"name": "John"})
print(deleted_customer)
