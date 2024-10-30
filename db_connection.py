import pymongo 
from pymongo import MongoClient
import datetime
MONGO_URL = "mongodb+srv://admin:dev_testing@cluster0.g21xt.mongodb.net/"

client = MongoClient(MONGO_URL)
db = client['dev_mongo']
collection = db['mongo_dev']

