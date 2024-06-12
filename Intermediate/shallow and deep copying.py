#shallow copy: one level deep, only references of nested child objects
#deep copy: full independent copy

import copy
#org = 5
#cpy = org
#cpy = 6      #original one don't change
#print(cpy)
#print(org)

#shallow copy
org = [0, 1, 2, 3, 4]
#cpy = org   #original one also change
#cpy = copy.copy(org) #original one don't change
#cpy = org.copy()
#cpy = list(org)
#cpy = org[:]
#cpy[0] = -10  
#print(cpy)
#print(org)

#deep copy
#org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
#cpy = copy.deepcopy(org) #original one don't change
#cpy[0][1] = -10  
#print(cpy)
#print(org)

#shallow copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Kai", 22)
#p2 = p1     #original one also change
p2 = copy.copy(p1)

p2.age = 23
print(p2.age)
print(p1.age)


#deep copy
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

    
p1 = Person("Kai", 22)
#p2 = p1     #original one also change
p2 = Person("Ray", 18)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


