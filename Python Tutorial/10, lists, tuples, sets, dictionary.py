#lists = [], changeable

food = ["pizza", "Hamburgers", "Hotdog", "Ramen"]
#print(food[0])
 
food[0] = "Sushi"

#print(food[0])

#food.append("Ice Cream")
#food.remove("Hotdog")
#food.pop() #Remove the last item in the list
#food.insert(0, "Puddin")
#food.sort()
#food.clear()

#for x in food:
#    print(x)
#---------------------------------------------------------------------------------------------------
#2D lists

drinks = ['Coffee', 'Soda', 'Tea']
dinner = ['Pizza', 'Hamburger', 'Ramen']
dessert = ['Cake', 'Ice Cream']

eats = [drinks, dinner, dessert]

#print(eats)
#print(eats[0])
#print(eats[1][2])
#---------------------------------------------------------------------------------------------------
#tuples = (), unchangeable

student = ("Jquan",22, "male")
#print(student.count('Jquan'))
#print(student.index('male'))

#for x in student:
#    print(x)

#if "Jquan" in student:
#    print("Jquan is here!")
#---------------------------------------------------------------------------------------------------
#sets = {}, unordered, unindexed, no duplicate values
#       faster than list or tuples

utensils = {"fork", "spoon", "knife" }
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add('napkin') 
#utensils.remove('fork')
#utensils.clear()
#utensils.update(dishes) # add set in another set
#dinner_table = utensils.union(dishes) #fuse a set with another set

#print(utensils.difference(dishes))   #find different values
#print(utensils.intersection(dishes)) #find common values

#for x in dinner_table:
#    print(x)
#---------------------------------------------------------------------------------------------------
#dictionary = {}, changeable, unordered

capitals = {'USA':'Wasington DC', 
            'India':'New Deli',
            'China':'Beijin',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()


#print(capitals['Russia'])
#print(capitals.get('Germany')) #Check if theres a specified key
#print(capitals.keys()) #show every keys in dict
#print(capitals.values()) #show every values in dict
#print(capitals.items()) #show every values and keys in dict

for key, value in capitals.items():
    print(key, value)


