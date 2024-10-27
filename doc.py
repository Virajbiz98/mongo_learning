# Insert a document
data = {"name": "test user", "email": "testuser@example.com"}
collection.insert_one(data)

collection.delete_one({"name": "test user"})
