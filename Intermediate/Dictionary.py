#mydict = {"name": "Max", "age": 28, "city": "NYC"}
#print(mydict)

#mydict2 = dict(name="Mary", age=27, city="Boston")
#print(mydict2)

#value = mydict["name"] #Enable to check a specific value in dictionary
#print(value)

#mydict["email"] = "jquan0416@gmail.com" #Dictionary is mutable so you can add some shit like this
#print(mydict)                           # if you do that again, the item in value is overwritten

#del mydict["name"] #delete a specified value
#print(mydict)

#mydict.pop("age")  #delete a specified value
#print(mydict)

#mydict.popitem() #delete the last value
#print(mydict)

#if "name" in mydict:         #show if there's specified value and items
#    print(mydict["name"])
#else:
#    print("Error")

#try:
#    print(mydict["name"])
#except:
#    print("Error")

#for key in mydict:
#    print(key)

#for value in mydict.values():
#    print(value)

#for key, value in mydict.items():
#    print(key, value)

#mydict_cpy = mydict.copy() #or dict(mydict)
#print(mydict_cpy)

#mydict_cpy["email"] = "jquan0416@gmail.com"
#print(mydict_cpy)
#print(mydict)

#my_dict = {"name": "Max", "age": 28, "email": "jquan0416@gmail.com"}
#my_dict_2 = dict(name="Mary", age=27, city="Boston")

#my_dict.update(my_dict_2) #update values and items
#print(my_dict)

#my_dict = {3: 9, 6: 36, 9: 81}
#print(my_dict)

#value = my_dict[3] #Put the actual key instead of index number
#print(value)

mytuple = (8, 7)        #Recap: tuple also mutable 
mydict = {mytuple: 15}
print(mydict)









