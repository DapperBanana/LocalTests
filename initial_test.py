
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create operation
data = {"name": "John", "age": 30}
inserted_data = collection.insert_one(data)
print("Data inserted with id:", inserted_data.inserted_id)

# Read operation
result = collection.find_one({"name": "John"})
print("Data retrieved:", result)

# Update operation
update_query = {"name": "John"}
new_values = {"$set": {"age": 35}}
collection.update_one(update_query, new_values)
updated_result = collection.find_one({"name": "John"})
print("Data updated:", updated_result)

# Delete operation
delete_query = {"name": "John"}
collection.delete_one(delete_query)
print("Data deleted")

# Close the database connection
client.close()
