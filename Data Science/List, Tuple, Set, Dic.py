# List = Ordered, Mutable, Duplicates
# Tuple = Ordered, Inmutable, Duplicates
# Set = Unordered, Addable/Removable, No duplicates
# Dictionary = Unordered, Mutable, No duplicates

L = [1,2,4,8,'name',3]
T = (1,2,4,8,'name',3)
S = {1,2,4,8,'name',3}
D = {"TwoThree":23, "B":43,"C":'CCD'}

#print('The type of L is:', type(L))
#print('The type of T is:', type(T))
#print('The type of S is:', type(S))
#print('The type of D is:', type(D))

#print(L[1])
#print(T[1])
#print(3 in S) #True or False
#print(D['B'])

#print(L[1:3])
#print(L[::-1])
#print(T[:3])
#----------------------------------------------------------------------------------
#Add some in List
#L = L + ['How', 'are', 7, 'you']
#print(L)
#L.append(6.8)
##print(L)
#----------------------------------------------------------------------------------
# combine Tuples
T2 = ('a', 'b', 420)
T3 = T+T2
#print(T3)
#----------------------------------------------------------------------------------
#add some in Set
S.add(69)
#print(S)
S.update({23,'game',1})
#print(S)
#----------------------------------------------------------------------------------
#add new keys and values in Dictionary
D['newkey'] = 'newValue'
#print(D)
D2 = {'y':'YY', 'z':10}
D.update(D2)
#print(D)
#----------------------------------------------------------------------------------
#delete some in List
del L[3]
#print(L)
#----------------------------------------------------------------------------------
#delete some in Set
S.remove('game')
#print(S)
#----------------------------------------------------------------------------------
#delete some in Dictionary
del D['C']
#print(D)
#----------------------------------------------------------------------------------
#Copy *Tuple cannot be copied
L2 = L.copy()
L2[2] = 'four'
#print(L2)
#print(L)
#----------------------------------------------------------------------------------
#Slicing
L3 = L[1:4]
#print(L3)
L3[0] = 'two'
#print(L3) #Don't effect to original one
#----------------------------------------------------------------------------------
#reverse
L.reverse()
#print(L)
#----------------------------------------------------------------------------------
D3 = {'A':L, 'B':T, 'C':S, 'D':D}
#print(D3['A'][3])

K = D3['D']
#print(K)
#for x in K:
#    print(x,K[x])

L4 = [L,T,D,23,'game']
#print(type(L4[2]))

L5 = [x**2 for x in range(10)]
print(L5)

S2 = {x**2 for x in range(2,20,3)}
print(S2)
#----------------------------------------------------------------------------------









