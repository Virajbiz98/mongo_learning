# how to insert one query 
query = {"name":"isuru"}
collection.insert_one(query)

# how to insert many query
import pymongo

# Your MongoDB connection string
client = pymongo.MongoClient("mongodb+srv://DEVMONGO:DEVMONGO@cluster0.wcbtj.mongodb.net/")

# Test the connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["first_project"]
collection = db["dev_02"]


query = [{"name":"free"},{"name":"learning"}]
collection.insert_many(query)


# how to find query
result = collection.find_one({"name":"isuru"})
print(result)

results = collection.find()
for document in results:
    print(document)

# how to update query
collection.update_one({"name":"isuru"},{"$set":{"age":"26"}})

collection.delete_one({"name":"isuru'}

                      
