import json

#person = {"name": "John", "age": 30, "city": "NYC", "hasChildren": False, "titles": ["assasin", "murderer"]}

#personJSON = json.dumps(person, indent=4, sort_keys= True ) #separators=['; ', '= '] #Encode Json
#print(personJSON)

#with open('person.json', 'w') as file:    #Create JSON files 
#    json.dump(person, file, indent=4)

#person = json.loads(personJSON)  #Decode JSON
#print(person)

#with open('person.json', 'r') as file:
#    person = json.load(file)  #Decode JSON
#    print(person)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Jquan', 21)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)



#userJSON = json.dumps(user, cls=UserEncoder) #default=encode_user
userJSON =UserEncoder().encode(user)
print(userJSON)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
