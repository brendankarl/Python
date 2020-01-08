import json
import os

#JSON data 
userJSON = """{
"name":"John",
"age":30,
"cars":[ "Ford", "BMW", "Fiat" ]
}"""

#Convert from JSON to Python dictionary
user = json.loads(userJSON)

#Print keys from Python dictionary
print(user["name"]) 
print(user["age"]) 
print(user["cars"]) #Print the list of cars
print(user["cars"][1]) #Print the second car in the list

#Update values in the dictionary
user["name"] = "Brendan"
user["cars"][2] = "Nissan"

#Add value to the dictionary (this is a list within the dictionary)
user["cars"].append("Lexus")

#Remove value from the dictionary
user["cars"].remove("Ford") 

#Loop through dictionary and print out key and values
for key,value in user.items():
    print(key,value)

#Slightly more complex JSON
usersJSON = """{
    "users":
    [
        {
            "name": "John",
            "age": 30,
            "cars":
            [
                "Ford",
                "BMW",
                "Fiat"
            ]
        },
        {
            "name": "Bert",
            "age": 29,
            "cars":
            [
                "Ford",
                "BMW",
                "Fiat"
            ]
        }
    ]
}"""

#Convert to Python dictionary and do stuff
users = json.loads(userJSON)
users["users"][1]

#Convert from Python (dict) to JSON (str) and print
user = json.dumps(user)
print(user)