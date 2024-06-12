#def mygenerator():
#    yield 1
#    yield 2
#    yield 3

#g = mygenerator()

#print(sum(g))

#print(sorted(g)) #create list

#for i in g:
#    print(i)

#value = next(g)
#print(value)

#value = next(g)
#print(value)

#value = next(g)
#print(value)


#import time

#def countDown(num):
#    print("Starting")
#    while num > 0:
#        yield num
#        num -= 1
#        time.sleep(1)

#cd = countDown(4)

#value = next(cd)
#print(value)

#print(next(cd))
#print(next(cd))
#print(next(cd))


#import sys

#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums

#def firstn_generator(n):
#    num = 0
#    while num < n:
#        yield num
#        num += 1

#mylist = firstn(10000)
#mygeneratorlist = firstn_generator(10000)
#print(mylist)
#print(sum(mylist))
#print(sum(mygeneratorlist))
#print(sys.getsizeof(mylist))
#print(sys.getsizeof(mygeneratorlist))


#def fibonacci(limit):
#    # 0 1 1 2 2 3 4 5 13...
#    a, b = 0, 1
#    while a < limit:
#        yield a
#        a, b = b, a + b

#fib = fibonacci(30)
#for i in fib:
#    print(i)

import sys
mygenerator = (i for i in range(10000) if i %2 == 0)
#for i in mygenerator:
#    print(i)
#print(list(mygenerator))
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10000) if i %2 == 0]
#print(mylist)
print(sys.getsizeof(mylist))
