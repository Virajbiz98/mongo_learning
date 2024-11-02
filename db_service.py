# how to insert many documents
from connection import collection

query_01 = {"id":"001","name":"test one","field":"art"}

query_02 = {"id":"002","name":"test_two","feild":"food"}

query_03 = {"name":"john","job":"eat"}

result = collection.insert_many([query_01,query_02,query_03])
print(result.inserted_ids)
