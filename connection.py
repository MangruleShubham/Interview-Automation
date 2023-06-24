import os

from pymongo import MongoClient

# # Get the MongoDB connection string from the environment
# MONGODB_CONNECTION_STRING = os.environ['mongodb://localhost:27017']

# Create a MongoClient object
client = MongoClient('mongodb://localhost:27017')

# Get the database
db = client.get_database("login")

# Get the collection
collection = db.get_collection("user")

