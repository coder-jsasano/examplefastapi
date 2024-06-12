#zip(*iterable) = aggregate elements from two or more iterables (list, tuples, sets, etc)
#                 creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "J", "Sasano"]
password = ['password', "abc123", 'Jsasano']
login_date =["1/1/2024","1/2/2024","1/3/2024"]

#users = zip(username,password)
#users = list(zip(username,password))
users = zip(username,password,login_date)

#print(type(users))

for i in users:
    print(i)


#users = dict(zip(username,password))

#for key,value in users.items():
#    print(key+' : '+value)
