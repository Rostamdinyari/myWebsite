# Import the necessary modules
import urllib.parse
import pymongo
from pymongo import MongoClient
import database



# Perform operations on the collection
# For example, insert a document
data = {"name": "Shirin", "age": 30}
insert_result = database.collection.insert_one(data)

# Print the inserted document's ID
print("Inserted document ID:", insert_result.inserted_id)
