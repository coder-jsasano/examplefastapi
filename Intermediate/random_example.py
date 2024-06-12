import random


#a = random.random() #give 10 digit random float
#a = random.uniform(1, 10) #give 10 digit random float in a specified range
#a = random.randint(1, 10)  #Convert float into int
#a = random.randrange(1, 10) #Do the same as above
#a = random.normalvariate(0, 1) #Pick a random number from a specified normal distributinon
#print(a)

#mylist = list("ABCDEFGH")
#a = random.choice(mylist) #Pick up a random element
#a = random.choices(mylist, k=3) #Pick up random numbers in a specified range with duplications
#a = random.sample(mylist, 3) #Pick up random numbers in a specified range without duplications

#a = random.shuffle(mylist)
#print(mylist)


#random.seed(1)   #Reproduce random data but its weak in terms of security
#print(random.random())
#print(random.randint(1, 10))

#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))

#random.seed(1)
#print(random.random())
#print(random.randint(1, 10))

#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))

import secrets

#a = secrets.randbelow(10) #pick up a number from 0 to 9 
#a = secrets.randbits(4) #Pick up a number regarding a specified bytes
#1111

#mylist = list("ABCDEFGH") 
#a = secrets.choice(mylist) #Unreproducable
#print(a)


import numpy as np

#a = np.random.rand(3,3) #float
#a = np.random.randint(0,10,(3,4)) #int
#print(a)

#arr = np.array([[1,2,3], [4,5,6], [7,8,9]]) #Double buckets
#print(arr)
#np.random.shuffle(arr)
#print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

