
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["mycollection"]

# Create a new document
data = {"name": "Alice", "age": 30}
col.insert_one(data)

# Read all documents
for doc in col.find():
    print(doc)

# Update a document
query = {"name": "Alice"}
new_values = {"$set": {"age": 31}}
col.update_one(query, new_values)

# Read a single document
result = col.find_one({"name": "Alice"})
print(result)

# Delete a document
col.delete_one({"name": "Alice"})

# Verify deletion
for doc in col.find():
    print(doc)
