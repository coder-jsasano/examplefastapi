import numpy as np

#a = np.array([1,2,3,5,7])
#b = np.array([2,3,5])
a = np.array([1,2,3,5,7], dtype='i') #dtype = datatype(int, float, str)
b = np.array([2,3,5], dtype='f')
#print(a)
#print(b)
#print(type(a))
#print(type(b))

#print(a.dtype) #show data type
#print(b.dtype)
#----------------------------------------------------------------------------------------------------------------
# Dimension = List of list, compiled stuff
c = np.array([[1,2,3],[4,5,6]])
#print(c.ndim) #shows number of dimension
#print(c[0,2]) #[Index of dimension, index of the dimension's list]

#d = np.array([[1,2,3],[2,4,5,9]]) #Error cuz the items inside each dimension are supposed to be the same
d = np.array([[1,2,3,-1],[2,4,5,9]])
#print(d[1,2])
#print(d.ndim)

e = np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])
#print(e)
#print(e.ndim)
#print(e[1,0,2])
#print(type(e))
#----------------------------------------------------------------------------------------------------------------
#shape[number of lists top outside, number of lists inside of outside list, number of elements in list] 
#     =show how many elements(lists) there are
#print(e.shape)
#print(e.shape[0])
#print(e.shape[1])
#print(e.shape[2])

f = np.array([2])
#print(f.ndim)

g = np.array(3)
#print(g.ndim)

#print(e.size) # shows how many elements there
#print(e.nbytes) # show bytes
#----------------------------------------------------------------------------------------------------------------
#np.arange() = create array with specified elements
#              similar to print(list(range()))
h = np.arange(100)
#print(h)
i = np.arange(20,100,3)
#print(i)
#----------------------------------------------------------------------------------------------------------------
#np.random.permutation() = shuffle elements inside array
j = np.random.permutation(np.arange(10))
#print(j)
#----------------------------------------------------------------------------------------------------------------
#np.random.randint(20,30) #show random int in a specified range
k = np.random.randint(20,30)
#print(k)
#print(type(k)) #int
#----------------------------------------------------------------------------------------------------------------
#np.random.rand(how many) = create random number between 0 and 1 
#print(l)
l = np.random.rand(1000) 
#----------------------------------------------------------------------------------------------------------------
#matplotlib 
import matplotlib.pyplot as plt
plt.hist(l, bins=100)
#plt.show() #show hist in window
#----------------------------------------------------------------------------------------------------------------
#np.random.randn() = create numbers in a specified range
o = np.random.randn(10000)
plt.hist(o,bins=200)
#plt.show()
#----------------------------------------------------------------------------------------------------------------
p = np.random.rand(2,3,4,2) #2x3: 2 arrays, 3 elements 
#print(p)
#print(p.ndim)
#----------------------------------------------------------------------------------------------------------------
#np.reshape = create shaped arrays and elements in a specified range
q = np.arange(100).reshape(4,5,5)
#print(q.shape)
#print(q)

#np.zeros()
#np.ones()
#----------------------------------------------------------------------------------------------------------------
#Slice
r = np.arange(100)
#s = r[3:10] #r is not copied
s = r[3:10].copy()
#print(s)
s[0] = -1200
#print(s)
#print(r)

#print(r[::5]) #take each number related 5
#print(r[::-5])
#----------------------------------------------------------------------------------------------------------------
#find out the index
r = np.arange(100)
s = r[3:10]
s[0] = -1200
#print(r) 

#find out the index of -1200
idx = np.argwhere(r == -1200)[0][0]
#print(idx)
r[idx] = 3
#print(r)
#----------------------------------------------------------------------------------------------------------------
t = np.round(10 * np.random.rand(5,4))
#print(t)
#print(t[1,2])
#print(t[1,:]) #access to a whole specified array
#print(t[:,1])  #access to a whole specified elements
#print(t[1:3,2:4]) #t[rows,colums]
#print(t.T) #Swap axis
#----------------------------------------------------------------------------------------------------------------
#numpy.linalg
import numpy.linalg as la
u = la.inv(np.random.rand(3,3))
#print(u)
#----------------------------------------------------------------------------------------------------------------
#sort every colum
t.sort(axis=0) #sort every colum vertically
#print(t) 
t.sort(axis=1) #sort every colum holizontally
#print(t)
#----------------------------------------------------------------------------------------------------------------
#masking 
v = np.arange(100)
w = v[[3,5,6]] #same as copy
#print(w)

#w[0] = -4
#w = v[v<40]
#w = v[(v<40) & (v>30)]

# &, /, ~= Used for array
# and, or, not = Used for everything except for array

#print(w)
#print(v)
#----------------------------------------------------------------------------------------------------------------
#Broadcasting
x = np.round(10*np.random.rand(2,3))
#print(x)
#print(x+3)
#print(x+(np.arange(2).reshape(2,1))) #create array[0,1] and reshape it as 2x1 (row:2 colum:1)
#----------------------------------------------------------------------------------------------------------------
#np.hstack = conbine each array holizontally
#            MAKE SURE TO PUT THE SAME "ROW" ON EACH ARRAY
#y = np.round(10*np.random.rand(2,2))
#print(x)
#print(y)
#z = np.hstack((x,y))
#print(z)
#----------------------------------------------------------------------------------------------------------------
#np.vstack = conbine each array holizontally
#            MAKE SURE TO PUT THE SAME "COLUM" ON EACH ARRAY
y = np.round(10*np.random.rand(1,3))
#print(x)
#print(y)
z = np.vstack((x,y))
#print(z)
#----------------------------------------------------------------------------------------------------------------
#np.sort
A = np.random.permutation(np.arange(10))
#print(np.sort(A))

B = np.array(["abc",'wassgood','420']) #make sure to set the same data type
#print(np.sort(B))
#----------------------------------------------------------------------------------------------------------------
#Numpy's Speed 
import timeit

C = np.random.rand(1000000)

start_time = timeit.default_timer()
sum_result = sum(C)
end_time = timeit.default_timer()
print("Time taken for Python's sum():", end_time - start_time)

start_time = timeit.default_timer()
np_sum_result = np.sum(C)
end_time = timeit.default_timer()
print("Time taken for NumPy's sum():", end_time - start_time)

def mySum(G):
    s = 0
    for x in G:
        s += x
    return s

start_time = timeit.default_timer()
sum_result = mySum(C)
end_time = timeit.default_timer()
print("Time taken for mySum():", end_time - start_time)



