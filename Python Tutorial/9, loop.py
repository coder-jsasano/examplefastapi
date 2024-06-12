#while

#while 1 == 1:
#    print('Help Im stuck in a loop!')

name = ""

#while len(name) == 0:
#    name = input('Enter your name: ')
#while not name:
#    name = input('Enter your name: ')

#print('Hello '+name)
#-----------------------------------------------------------------------------------------------------
#for

#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print(i)

#for i in "Jquan Lee":
#    print(i)

#import time

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print('Happy New Year!!!')
#-----------------------------------------------------------------------------------------------------
#nested loops
#rows = int(input('How many rows?: '))
#columns = int(input('How many columns?: '))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end='')
#    print()
#-----------------------------------------------------------------------------------------------------
#loop control statement = break, continue, pass

#while True:
#    name = input('Enter your name: ')
#    if name != "":
#        break

phone_number = "123-456-7890"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)
