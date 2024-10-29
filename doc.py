# Test the connection
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["first_project"]
collection = db["dev_02"]

#  insert document
document = {
    "name":"max",
    "email":"max45@max.comb",
    "mobile": "01993494",
    "work" : "nojob",
    "address":{
        "street":"3434 jafna",
        "city"  : "jafna",
        "state" : "easten",
        "zip"   : "188938"
    }
    }

result = collection.insert_one(document)
print(result.inserted_id)
