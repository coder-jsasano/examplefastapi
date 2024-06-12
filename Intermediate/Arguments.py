#The difference between arguments and parameters
#Parameters: the variables that are defined or used inside parentheses where defining a function
#Arguments: the values passed for these parameters while calling a function

#def print_name(name): #(name) = parameter
#    print(name)

#print_name('Alex') #('Alex') = argument
#------------------------------------------------------------------------------------------------------------------
#Positional and Keyword arguments

#def food(a, b, c, d=4):
#    print(a, b, c, d)

#food(1, 2, 3) #Positional argument
#food(a=1, b=2, c=3) #Keyword argument
#food(1, 2, 3, 7)
#------------------------------------------------------------------------------------------------------------------
#variable length argument

#def foo(a, b, *args, **kwargs):
#    print(a, b)
#    for arg in args:
#        print(arg)
#    for key in kwargs:
#        print(key, kwargs[key])

#foo(1, 2, 3, 4, 5, six=6, seven=7)

#def foo(*args, last):
#    for arg in args:
#        print(arg)
#    print(last)

#foo(1, 2, 3, last=100)
#--------------------------------------------------------------------------------
#Unpacking arguments
#def foo(a, b, c):
#    print(a, b, c)

#my_list = [0, 1, 2]  #Unpack 
#my_dict = {'a':1, 'b':2, 'c':3}
#foo(*my_dict)
#------------------------------------------------------------------------------------
#Local vs Global arguments
#def foo():
#    global number
#    x = number
#    number = 3
#    print('Number inside function', x)

#number = 0
#foo()
#print(number)


#def foo(): 
#    global number   #global required to apply local arguments in function 
#    number = 3

#number = 0
#foo()
#print(number)
#------------------------------------------------------------------------------------
#Immutable
def foo(x):
    x = 5

var = 10
foo(var)
print(var)

#Mutable
def foo(a_list):
    a_list = [200, 300, 400] #If we rebind the alter reference won't be changed
    a_list.append(4)
    a_list[0] = -100
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)


def foo(a_list):
    #a_list += [200, 300, 400]  #Affect
    a_list = a_list + [200, 300, 400] #Not affect
    
my_list = [1, 2, 3]
foo(my_list)
print(my_list)









