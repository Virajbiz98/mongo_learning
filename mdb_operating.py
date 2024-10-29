# how to insert one query 
query = {"name":"isuru"}
collection.insert_one(query)

# how to insert many query
query = {"name":"isuru"},{"name":"eranda"}
colection.insert_many(query)

# how to find query
result = collection.find_one({"name":"isuru"})
print(result)

results = collection.find()
for document in results:
    print(document)

# how to update query
collection.update_one({"name":"isuru"},{"$set":{"age":"26"}})

collection.delete_one({"name":"isuru'}

                      
