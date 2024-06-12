#collections: Counter, namedtuple, OrderedDict, defaultdict,  deque

#Counter

#from collections import Counter
#a = "aaabbbccc"
#my_counter = Counter(a) #Count every different stuff
#print(my_counter)
#print(my_counter.items())
#print(my_counter.keys())
#print(my_counter.values())
#print(my_counter.most_common(1)[0][0]) #() = number of value, [] = index num for tuple, [] = index num for only element
#print(list(my_counter.elements()))

#nametuple
#from collections import namedtuple
#Point = namedtuple("Point", "x,y")
#pt = Point(1, -4)
#print(pt)
#print(pt.x, pt.y) #show only values

#OrderedDict
#from collections import OrderedDict 
#ordered_dict = OrderedDict() #you can change the order by putting codes in your desired order
#ordered_dict["a"] = 1
#ordered_dict["b"] = 2
#ordered_dict["c"] = 3
#ordered_dict["d"] = 4
#print(ordered_dict)

#defaultdict
#from collections import defaultdict
#d = #defaultdict(list)#defaultdict(float) #defaultdict(float)#defaultdict(int)
#d["a"] = 1
#d["b"] = 2
#print(d["a"])

#deque
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3) #add element on the top left of deque

print(d)

#d.pop()
#d.popleft()
#rint(d)

#d.extend([4,5,6])
#print(d)

#d.extendleft([4,5,6])
#print(d)

d.rotate(1) #Rotate right, if negative, left
print(d)








