#Problem solving
#Selection sort

L = [0,5,2,3,1,4]
n = len(L)

def searchMinFromList(L,n):
    minValue = L[0]
    idx = 0
    counter = 1
    while counter < n:
        v = L[counter]
        if v < minValue:
            minValue = v
            idx = counter
            counter += 1
        else:
            pass
        counter += 1
    return minValue, idx

def sortList(L,n):
    L2 = []
    counter = 0
    while counter < n:
        m, idx = searchMinFromList(L,n)
        L2.append(m)
        del L[idx]
        n = n-1
    return L2


#print(sortList(L,n))

#L.sort() # same as above
#print(L)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#User will enter a floating number. You gotta find out the code that makes that number without decimal number.
#Like 234.62 into 234 
#Also, you gotta tell if the number is even or odd.

#x = float(input('Enter a real number: '))
#y = round(x) 

#if x>0:
#    if y>x:
#        intPortion = y-1
#    else:
#        intPortion = y
#else:
#    if y<x:
#        intPortion = y+1
#    else:
#        intPortion = y

#if intPortion%2 == 0:
#    print('even')
#else:
#    print('odd')
 
#print(intPortion)   
#----------------------------------------------------------------------------------
"""Let's say you are a teacher and you have different student records containing id of a student. 
Also, the marks list in each subject where different students have taken different number of subjects.
All these records are in hard copy. 
You wanna enter all the data in computer and compute the average marks of each student"""

def getData():
    D = {}
    while True:
        studentId = input('Enter student ID: ')
        marksList = input('Enter the marks by comma separated values: ')
        moreStudents = input('Enter yes/no for adding more students: ')
        if studentId in D:
            print(studentId,'is already resistered')
        else:
            D[studentId] = marksList.split(',')
        if moreStudents.lower() == 'no':
            return D
        
studentData = getData()

print(studentData)

def getAverageMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks

avgM = getAverageMarks(studentData)

for x in avgM:
    print('Student :',x,'got avg Marks as:', avgM[x])

