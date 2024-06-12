#myset = {1,2,3,1,2} #No dupliates (Same one is not shown)

#myset = set([1,2,3]) 
#myset = set("Hello") 

#myset = set()
#myset.add(1)
#myset.add(2)
#myset.add(3)

#myset.remove()
#myset.discard()
#myset.clear()
#print(myset.pop()) #Remove the first one

#for i in myset:
#    print(i)

#if 4 in myset:
#    print("Yes")

#print(myset)

#odds = {1, 3, 5, 7, 9}
#evens = {0, 2, 4, 6, 8}
#primes = {2, 3, 5, 7}

#u = odds.union(evens) #convine elements without duplicates
#print(u)

#i = odds.intersection(primes) #detect the same elements
#print(i)

setA = {1, 2, 3, 4, 5, 6}
#setB = {1, 2, 3}
#setC = {7,8}

#diff = setA.difference(setB) #Show differences from a specified set
#diff = setA.symmetric_difference(setB) #Show differences that has both of sets
#setA.update(setB)
#setA.intersection_update(setB) #show only the same elements
#setA.difference_update(setB)
#setA.symmetric_difference_update(setB)
#print(setA)

#print(setA.issubset(setB)) #Say True if the elements of setA are in setB, otherwise false
#print(setA.issuperset(setB)) #Say True if the elements of setA are all contained in setB
#print(setA.isdisjoint(setC)) #Say True if the first set has completely different elements

#setB = setA.copy() #or set(setA)
#setB.add(7)
#print(setB)
#print(setA)

a = frozenset([1, 2, 3, 4]) #Immutable set except for union and intersection function

a.add(5)
a.remove(1)

print(a)
