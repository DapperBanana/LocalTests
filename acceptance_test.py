
# Import the pymongo library
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]

# Create a new document
new_customer = {"name": "Alice", "email": "alice@example.com"}
inserted_doc = collection.insert_one(new_customer)
print("Inserted new document with ID:", inserted_doc.inserted_id)

# Find a document
query = {"name": "Alice"}
result = collection.find_one(query)
print("Found document:", result)

# Update a document
update_query = {"name": "Alice"}
new_values = {"$set": {"email": "alice.new@example.com"}}
collection.update_one(update_query, new_values)
print("Document updated.")

# Delete a document
delete_query = {"name": "Alice"}
collection.delete_one(delete_query)
print("Document deleted.")

# Print all documents in the collection
print("All documents in the collection:")
for doc in collection.find():
    print(doc)
