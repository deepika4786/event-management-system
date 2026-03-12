from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")

# Database
db = client["event_management_db"]

# Collections
users_collection = db["users"]
events_collection = db["events"]
registrations_collection = db["registrations"]