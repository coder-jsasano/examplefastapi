a = True
b = True
c = False

print(a and b) 
print(a and c)
print(c and b)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(a or b) 
print(a or c)
print(c or c)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print(2<3)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

f = 2>1
print(type(f))
print(f)

print(3 == 3.0)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

x = 4
y = 9
z = 8.3
r = -3

xy = x<y
zy = z<y
rx = r == x

print(xy and zy or rx)
print(xy and rx or zy)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#isinstance(things or numbers, type) = returns True, if the first argument is an instance of that class. 
print(isinstance(1,int))
print(isinstance(3.4,int))
print(isinstance(3.4,(int, float)))
print(isinstance(3+4j,(int, float, str, complex)))


