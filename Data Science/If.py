
#a = int(input())
#b = int(input())

#if a>b:   # b will be printed if b == a
#    print(a)
#    print('if part')
#else:
#    print(b)
#    print('else part')

#if a>b:
#    print(a)
#    print("a is greater than b")
#elif a == b:
#    print("a and b are equal")
#else:
#    print(b)
#    print('b is greater than a')

#a = int(input('Enter marks: '))

#if a >= 85:
#    print('A grade')
#elif 80 <= a < 85:
#    print('A- grade')
#elif 75 <= a < 80:
#    print('B grade')
#elif 70 <= a < 75:
#    print('B- grade')
#else:
#    print('Expelled')

# elif not: = else

#nested if

a = int(input())
if a>10:
    print('It is larger than 10')
    print('if')
    if a>=20:
        print('It is larger than 20')
        print('nested if')
        if a>=30:
            print('It is larger than 30')
            print('inside nested if')
        else:
            print('It is smaller than 30')
    else:
        print('It is smaller than 20')
        print('nested else')
else:
    print('It is smaller than 10')
    print('else')





