#itertools: product, permutations, combinations, accumulate, groupby,  and infinite iterators

#product
#from itertools import product
#a = [1, 2]
#b = [3]
#prod = product(a,b) #Multiple each other 
#prod = product(a,b, repeat = 2) #repeat multiplications
#print(list(prod))  

#permutaions
#from itertools import permutations
#a = [1, 2, 3]
#perm = permutations(a) #show every pattern of items in list
#perm = permutations(a, 2) #Specified amount of stuff
#print(list(perm))

#combinations
#from itertools import combinations #No repeatition
#from itertools import combinations_with_replacement #Repeatition included
#a = [1, 2, 3, 4]
#comb = combinations(a, 2)
#print(list(comb))
#comb_wr = combinations_with_replacement(a, 2)
#print(list(comb_wr))

#accumulate
#from itertools import accumulate
#import operator
#a = [1, 2, 5, 3, 4]
#acc = accumulate(a) #sum
#acc = accumulate(a, func=operator.mul) #multiple *do not forget to import operator
#acc = accumulate(a, func=max)  #comparison from maximum number
#print(a)
#print(list(acc))

#from itertools import groupby

#def smaller_than_3(x):
#    return x <3

#persons = [{"name": "Jquan", "age": 21}, {"name": "Kai", "age": 21}, 
#           {"name": "Ray", "age": 18}, {"name": "Speed", "age": 19}]

#a = [1, 2, 3, 4]
#group_obj = groupby(a, key=smaller_than_3)
#group_obj = groupby(a, key=lambda x: x<3)
#group_obj = groupby(persons, key=lambda x: x["age"])
#for key, value in group_obj:
#    print(key, list(value))

#count, cycle, repeat
from itertools import count, cycle, repeat

#for i in count(10): #count from 10 
#    print(i)
#    if i == 15:
#        break

a = [1, 2, 3]
#for i in cycle(a): #cycle stuff in list
#    print(i)
#    if i == 3:
#        break

for i in repeat(1, 4): #repeat (something, howmany)
    print(i)







