from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

client = MongoClient(os.environ["MONGO_URI"])
db = client['eventhub']
collection = db['events']

def list_collection_names():
    return db.list_collection_names()