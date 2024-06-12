#map(function, iterable) - applies a function to each item in an iterable(list, tuple, etc)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_JPY = lambda data: (data[0],data[1]*153)
to_USD = lambda data: (data[0],data[1]/153)


store_jpy = list(map(to_JPY, store))
store_usd = list(map(to_USD, store))

for i in store_jpy:
    print(i)

for i in store_usd:
    print(i)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#filter(function, iterable) = create a collection of elements from an iterable for which a function returns True

dudes = [("Kai", 22),
         ("Speed", 19),
         ("Ray", 18),
         ("Duke", 31),
         ("Ryley", 20),
         ("Eragon", 20)]

age = lambda data:data[1]>=20

dringking_dudes = list(filter(age, dudes))

for i in dringking_dudes:
    print(i)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#reduce(function, iterable) = apply a function to an iterable and reduce it to a single cumulative value
#                             performs function on first two elements and repeats process until 1 value remains

import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y, letters)

print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x*y, factorial)
print(result)


