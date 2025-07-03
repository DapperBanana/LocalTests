
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create operation
data1 = {"name": "Alice", "age": 25}
inserted_data = collection.insert_one(data1)
print("Data inserted with id:", inserted_data.inserted_id)

# Read operation
print("Data retrieved:")
for doc in collection.find():
    print(doc)

# Update operation
query = {"name": "Alice"}
update_values = {"$set": {"age": 30}}
collection.update_one(query, update_values)
print("Data updated.")

# Delete operation
query = {"name": "Alice"}
collection.delete_one(query)
print("Data deleted.")

# Display data after deletion
print("Data after deletion:")
for doc in collection.find():
    print(doc)
