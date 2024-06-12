#mylist = ["Banana","Cherry","Apple"]

#mylist2 = [5, True, "apple", "apple"]
#print(mylist2)


#for i in mylist:
#    print(i)

#item = mylist[0] #if I put minus, it reads from the last
#print(item)

#if "Banana" in mylist: #Enable to check if something is in list
#    print("Yes")
#else:
#    print("Nah")

#print(len(mylist)) #Show the number of items in list
#--------------------------------------------------------------------------
#mylist.append("lemon") #Add items in list
#print(mylist)

#mylist.insert(1, "blueberry") #Add items at a specific index in list
#print(mylist)
#--------------------------------------------------------------------------
#mylist.pop()  #Remove the last item
#print(mylist)

#mylist.remove("Cherry") #Remove a specified item
#print(mylist)

#mylist.clear() #Remove everything in list
#print(mylist)
#--------------------------------------------------------------------------
#mylist.reverse() #excecute reversely
#print(mylist)
#--------------------------------------------------------------------------
#mylist.sort() #sort out from abc, low to high
#print(mylist)

#new_list = sorted(mylist)
#print(new_list)
#--------------------------------------------------------------------------
#mylist = [0] * 5
#print(mylist)

#mylist2 = [1,2,3,4,5]

#new_list = mylist + mylist2
#print(new_list)
#------------------------------------------------------------------------------------
#mylist = [1,2,3,4,5,6,7,8,9]

#a = mylist[:5] #Excecute from 1 index till 4 one 
#a = mylist[::2] #Step
#a = mylist[::-1] #Execute reversely
#print(a)
#------------------------------------------------------------------------------------
#list_org = ["banana","cherry","apple"]

#list_cpy = list_org.copy() #Adding .copy() maintain the original
#list_cpy = list(list_org)   #maintain the original
#list_cpy = list_org[:]       #Slice = maintain the original 

#list_cpy.append("lemon") # if you append items in copy, the original one got affected the same as copy

#print(list_cpy)
#print(list_org)
#------------------------------------------------------------------------------------
a = [1,2,3,4,5]
b = [i*i for i in a] #make int items powered

print(a)
print(b)





