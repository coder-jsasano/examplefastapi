def printSuccess():
    print('I am done')
    print('Send me another task')

#printSuccess()
#-------------------------------------------------------------------------------------------------------------
def printSuccess2():
    """
    This function is doing nothing except printing a message.
    That message is "hello" 
    """
    print("hello")

#help(printSuccess2) #shows documents written in functions
#-------------------------------------------------------------------------------------------------------------
def printMsg(msg):
    """
    The function prints the message supplied by the user
    or prints that msg is not in the form of str
    """
    if isinstance(msg, str):
        print(msg)
    else:
        print('Your input argument is not a string')
        print('Here is what you have supplied', msg,':',type(msg))


#help(printMsg)
#printMsg("STFU")
#printMsg(23)

#y = "hello there!"
#printMsg(y)
#-------------------------------------------------------------------------------------------------------------
def my_power(a,b):
    """This function computes power just like pow()"""
    c = a**b
    print(c)

#my_power(2,3)
#-------------------------------------------------------------------------------------------------------------
def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("Error: The input arguments are not the expected types")

#checkArgs(3,4,5)
#-------------------------------------------------------------------------------------------------------------
def f(a,b,c):
    print("A is :",a)
    print("B is :",b)
    print("C is :",c)

#f(2,3,'game')
#f(a = 3, b = 'game', c = 2)
#f(c = 2, a = 3, b = 'game')
#-------------------------------------------------------------------------------------------------------------
def myadd(a,b):
    sumValue = a + b
    return sumValue    #if you wanna use it in global, you gotta put return

#d = myadd(2,3)
#print(d)

variableOutsideTheFunction = 3
def g():
    variableOutsideTheFunction = 5
    print(variableOutsideTheFunction)

#g() #local only works in local
#print(variableOutsideTheFunction)
#-------------------------------------------------------------------------------------------------------------
def h():
    print('A')
    a = 3
    b = 5
    c = a + b
    print('something')
    return c

#print(h())
#-------------------------------------------------------------------------------------------------------------
def r():
    a = 5
    b = 7
    d = 'something'
    return a,b,d

x,y,z = r()
#print(x,y,z)
#-------------------------------------------------------------------------------------------------------------
def myAddUniversal(*args):
    s = 0
    for i in range(len(args)):
        s += args[i] #s = s+args[i]
    return s
    
#print(myAddUniversal(2,4,5,6,56))
#-------------------------------------------------------------------------------------------------------------
def printAllVariablesAndValues(**args):
    for x in args:
        print('Variable name is:',x,'And Value is:',args[x])

#printAllVariablesAndValues(a=3, b='B', c='CCC',y=6.7)
#-------------------------------------------------------------------------------------------------------------
def gg(s=4):
    print(s)

#gg(55)

#L = [1,2,3]
#L2= L
#L2[0] = -9
#print(L)

def ff(L=[1,2]):
    for i in L:
        print(i)

L2 = [12,3,4]
#ff(L2)
#ff()
#-------------------------------------------------------------------------------------------------------------
import sys
sys.path.append('C:\\Users\\junpe\\Python code\\Tutorials\\Data Science')
import my_universal_functions as myFs #inport all functions in a specified module
#from my_universal_functions import addAllNumerics #inport a function from a specified module

#c = myFs.addAllNumerics(2,3,4,5,4)
#c = addAllNumerics(2,3,4,5,4)
#print(c)

#n = myFs.myName
#print(n)
#-------------------------------------------------------------------------------------------------------------
def findMin(L):
    m = L[0]
    idx = 0
    i = 0
    for x in L:
        if x<m:
            m = x
            idx = i
        else:
            pass
        i += 1
    return m,idx

a,b = findMin([2,3,4,0,9])
#print(a,b) #(minimum, index)

def findMin2(L, startIdx):
    m = L[startIdx]
    idx = startIdx
    for i in range(startIdx, len(L)):
        x = L[i]
        if x<m:
            m = x
            idx = i
        else:
            pass
        i += 1
    return m,idx

#a,b = findMin2([2,3,4,0,9])
#print(a,b) #(minimum, index)
#-------------------------------------------------------------------------------------------------------------
def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L

#L = [2,3,6,7]
#L2 = swapValues(L,1,3)
#print(L2)
#-------------------------------------------------------------------------------------------------------------
def checkIfNotNumeric2(L):
    retValue = True
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True

def sortList(L,startIdx):
    if not checkIfNotNumeric2(L):
        print('Error: List does not contain numeric values')
        return
    else:
        c = 0
        for x in L:
            m, idx = findMin2(L, c)
            L = swapValues(L,c,idx)
            c += 1
    return L

L2 = sortList([2,1,5,3,-8,17],0)
print(L2)
#-------------------------------------------------------------------------------------------------------------



