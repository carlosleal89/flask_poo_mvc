from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")

client = MongoClient(mongo_uri)

db = client[db_name]
