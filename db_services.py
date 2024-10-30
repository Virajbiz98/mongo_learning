from db_connection import collection

# creating fuction 
def find_users_with_name(name):
    query = {"name": name}
    document = collection.find_one(query)
    return document

#calling functon 
user_data = find_users_with_name("isuru")

# printing results
if user_data:
    print(user_data)
    print(f'the branch of the isuru is in : {user_data['branch']}')