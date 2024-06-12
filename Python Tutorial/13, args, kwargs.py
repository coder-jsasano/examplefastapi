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
#**kwargs = parameter that will pack all arguments into dictionary

def hello(**names):
    #print('Hello '+ kwargs['first'] + ' '+ kwargs['last'])
    print('Hello', end=' ')
    for key, value in names.items():
        print(value, end=' ')


hello(title = 'Mr.', first='Jquan', middle='Sasano', last='Lee')








