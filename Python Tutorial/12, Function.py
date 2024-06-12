#function = a block of code which is executed only when it is called

def hello(first_name, last_name, age):
    print('Hello ' + first_name + ' ' + last_name)
    print("You are "+str(age)+" years old")
    print('Have a nice day!')

#my_name = 'Jquan'
#hello("Jquan")
#hello('Dude')
#hello(my_name)
#hello('Jquan', 'Lee')
#hello('Jquan', 'Lee',22)
#------------------------------------------------------------------------------------------------
#return 
def multipuly(number1, number2):
    result = number1 * number2
    return result

#x = multipuly(9,10)
#print(x)
#------------------------------------------------------------------------------------------------
#keyword arguments

def hello(first, middle, last):
    print('Hello '+first+' '+middle+' '+last)

#hello(middle='Lee', first='Jquan', last='Sasano')
#------------------------------------------------------------------------------------------------
#nested function calls

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("Enter a whole positive number: ")))))
#------------------------------------------------------------------------------------------------
#scope = variable

def display_name():
    name = 'Lee' #Local scope(Available only inside this function)
    print(name)

name = 'Jquan' #Global scope(Available inside and outside functions)
#display_name()
#print(name)

#Local => Enclosing => Global => Built-in
#------------------------------------------------------------------------------------------------
#*args = parameter that will pack all arguments
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

#print(add(1,2,3,4,5,6))
#print(add(1,2,3,4,5,6,7,7))
#------------------------------------------------------------------------------------------------
#**kwargs






