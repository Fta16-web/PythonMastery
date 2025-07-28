from pymongo import MongoClient

client = MongoClient("mongodb://admin:adminpassword@localhost:27017")
db = client.mydatabase  # selecting a database
collection_name = "users"
user_collection = db[collection_name]
