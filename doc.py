# Insert a document
data = {"name": "shadow", "email": "shadow90@example.com"}
collection.insert_one(data)

# Find a document
result = collection.find_one({"name": "shadow"})
print(result)
