
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
user = {"name": "John", "email": "john@example.com"}
collection.insert_one(user)

# Read
result = collection.find_one({"name": "John"})
print(result)

# Update
update_query = {"name": "John"}
new_values = {"$set": {"email": "john.doe@example.com"}}
collection.update_one(update_query, new_values)

# Read
result = collection.find_one({"name": "John"})
print(result)

# Delete
delete_query = {"name": "John"}
collection.delete_one(delete_query)

# Read
result = collection.find_one({"name": "John"})
print(result)
