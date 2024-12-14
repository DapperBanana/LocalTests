
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create
data = {"name": "John", "address": "Highway 37"}
insert_result = collection.insert_one(data)
print(insert_result.inserted_id)

# Read
for customer in collection.find():
    print(customer)

# Update
update_query = {"name": "John"}
new_values = {"$set": {"address": "Park Lane 38"}}
update_result = collection.update_one(update_query, new_values)
print(update_result.modified_count)

# Delete
delete_query = {"name": "John"}
delete_result = collection.delete_one(delete_query)
print(delete_result.deleted_count)

# Read after delete
for customer in collection.find():
    print(customer)
