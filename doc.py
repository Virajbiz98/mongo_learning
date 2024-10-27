# update one matching document
collection.update_one(
    {"name":"shadow"}, # filter (what dofind)
    {"$set": {"email": "updateemail@example.com"}}
)
