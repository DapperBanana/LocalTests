
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
data = {"name": "John", "email": "john@example.com"}
insert_result = collection.insert_one(data)
print("Document inserted with ID:", insert_result.inserted_id)

# Read
query = {"name": "John"}
result = collection.find_one(query)
print("Document retrieved:", result)

# Update
new_values = {"$set": {"email": "john.doe@example.com"}}
update_result = collection.update_one(query, new_values)
print("Document updated:", update_result.modified_count)

# Delete
delete_result = collection.delete_one(query)
print("Document deleted:", delete_result.deleted_count)
