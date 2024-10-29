# insert document
document = {
        "id"  : {"$oid":"sampathtile123"},  # this one:- {"$oid":".."} must need for insert id
        "name" : "sampath ",
        "email": "sampath94@taile.com",
        "age"  : 30,
        "address":{
            "street": "365 pliyandala ",
            "city"  : "werahara",
            "state" : "western",
            "zip"   : "94345"
        },
        "phone numbers":[
            {
                "type" : "home",
                "number": "0413497017"
            },
            {
                "type" : "work",
                "number": "0765534223"
            }
        ],

        "is active": True, #  isActive to True means the user is currently active, while False would indicate they are inactive.
        "createdAT": datetime.now(), #.  This field stores the date and time when the document (or entity) was created.
        "updateAT" : datetime.now()# This field records the date and time when the document was last updated.
            }
        

result = collection.insert_one(document)
print(result)
