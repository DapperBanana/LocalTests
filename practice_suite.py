
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create
data = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(data)

# Read
result = collection.find_one({"name": "John"})
print(result)

# Update
new_data = {"$set": {"age": 35}}
collection.update_one({"name": "John"}, new_data)

# Read updated data
result = collection.find_one({"name": "John"})
print(result)

# Delete
collection.delete_one({"name": "John"})

# Check if the data is deleted
result = collection.find_one({"name": "John"})
print(result)  # Output will be `None`
