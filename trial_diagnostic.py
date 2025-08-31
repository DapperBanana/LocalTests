
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["students"]

# Create
student1 = { "name": "Alice", "age": 20, "grade": "A" }
student2 = { "name": "Bob", "age": 22, "grade": "B" }

result = collection.insert_many([student1, student2])
print(result.inserted_ids)

# Read
for student in collection.find():
    print(student)

# Update
query = { "name": "Alice" }
new_values = { "$set": { "age": 21 } }

collection.update_one(query, new_values)

print("After updating:")
for student in collection.find():
    print(student)

# Delete
query = { "name": "Bob" }
collection.delete_one(query)

print("After deleting:")
for student in collection.find():
    print(student)
