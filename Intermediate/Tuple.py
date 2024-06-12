#mytuple = ("Max", 28, "Boston") #Need , even if it's only one
#mytuple = tuple(["Max", 28, "Boston"]) #make list tuple
#print(mytuple)
#print(type(mytuple))

#item = mytuple[0]
#print(item)

#mytuple[0] = "Tom" #it ain't work cuz tuple is immutable

#for i in mytuple:
#    print(i)

#if "max" in mytuple:
#    print("Yes")

#else:
#    print("No")
#---------------------------------------------------------------------------
#mytuple = ["a","p","p","l","e"]
#print(len(mytuple)) #Count the element of tuple
#print(mytuple.count("p")) #Count a specified element
#print(mytuple.index("a")) #Show the index of a specified element

#mylist = list(mytuple)
#print(mylist)

#mytuple2 = tuple(mylist)
#print(mytuple)
#---------------------------------------------------------------------------------
#a = [1,2,3,4,5,6,7,8,9,10]

#b = a[2:5]
#b = a[::-2]
#print(b)
#---------------------------------------------------------------------------------
#my_tuple = "Max", 28, "Boston" 

#name, age, city = my_tuple #Must put the same amount of element in tuple
#print(name)
#print(age)
#print(city)

#my_tuple = (0,1,2,3,4)

#i1, *i2, i3 = my_tuple  #create list in between first and last element
#print(i1)
#print(i3)
#print(i2) #List
#-------------------------------------------------------------------------------------
#import sys
#my_list = [0,1,2,"hello",True]
#my_tuple = (0,1,2,"hello",True)
#print(sys.getsizeof(my_list), "bytes")   
#print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000))

#Tuple is more efficient than list due to the low amount of bytes

#----------------------------------------------------------------------------------------


