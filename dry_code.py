
import pymongo

# Create a MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["mydatabase"]

# Create a collection
collection = db["customers"]

# Insert a record
record = {"name": "John", "address": "Highway 37"}
inserted_record = collection.insert_one(record)
print("Record inserted with ID:", inserted_record.inserted_id)

# Find a record
result = collection.find_one({"name": "John"})
print(result)

# Update a record
update_query = {"name": "John"}
update_data = {"$set": {"address": "Highway 61"}}
collection.update_one(update_query, update_data)
updated_record = collection.find_one({"name": "John"})
print(updated_record)

# Delete a record
delete_query = {"name": "John"}
collection.delete_one(delete_query)
deleted_record = collection.find_one({"name": "John"})
print("Record deleted:", deleted_record)

# Drop the collection
collection.drop()
