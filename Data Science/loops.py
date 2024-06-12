#while
#n = int(input()) + 1
#i = 1
#while i<n:
#    print(i**2)
#    print('This is iteration number:', i)
#    i += 1
#print('done')
#------------------------------------------------------------------------------------
n = 10
i = 1
#while True: #always run except for break
#    if i%9 == 0:
#        print('inside if')
#        break
#    else:
#        print('inside else')
#        i = i+1
#print('Done') 
#------------------------------------------------------------------------------------
#while True:
#    if i%9 != 0:
#        print('inside if')
#        i += 1
#        continue
#    print('something') # This works like else statement 
#    break

#print('Done')
#------------------------------------------------------------------------------------
#for
#L = []
#for i in range(0,10,2):
#    print(i)
#    L.append(i**2)
#print(L)
#------------------------------------------------------------------------------------
#S = {"Apple", 4.20, "Zaza"} #Set
#i = 1
#for x in S:
#    print(x)
#    i += 1
#    if i == 3:
#        break
#    else:
#        pass
#else:           #It works only in Python
#    print('Loop terminates with success')
#print('Outside the loop')
#-----------------------------------------------------------------------------------------
#D = {'A':10, 'B':-19, 'C':'abc'} #Dictionary
#for x in D:
#    print(x,":",D[x])
#-----------------------------------------------------------------------------------------
#Given a list of numbers i.e. [1, 2, 4, -5, 7, 9, 3, 2]
#that contains all the items in sorted order from min to max.
#Create sorted list with loop function

L = [1, 2, 4, -5, 7, 9, 3, 2]
for j in range(len(L)):
    m = L[j]
    idx = j
    for i in range(j, len(L)):
        if L[i] < m:
            m = L[i]
            idx = i
    # Swap elements to place the minimum at the correct position
    L[j], L[idx] = L[idx], L[j]

print(L)





