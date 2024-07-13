
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create
data = {"name": "John", "age": 30, "city": "New York"}
new_record = collection.insert_one(data)
print("Created new record with ID:", new_record.inserted_id)

# Read
record = collection.find_one({"name": "John"})
print("Read record:", record)

# Update
update_query = {"name": "John"}
new_values = {"$set": {"age": 35}}
collection.update_one(update_query, new_values)
print("Record updated")

# Read all records
all_records = collection.find()
print("All records:")
for record in all_records:
    print(record)

# Delete
delete_query = {"name": "John"}
collection.delete_one(delete_query)
print("Record deleted")

# Read all records after deletion
all_records_after_deletion = collection.find()
print("All records after deletion:")
for record in all_records_after_deletion:
    print(record)
