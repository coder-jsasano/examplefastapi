s = 'Python is an amazing language'
t = "It's good for data science"
#print(type(s))
#print(s)
#print('hello',21,'hello2','who is you',50)

#v = s+' '+t
#print(v)
#-----------------------------------------------------------------------------------------------------------------
price = '$' + str(12) 
b = 'The price of this book'
v = b + ' is '+ str(price)
#print(v)
#print(b,'is',price)
#-----------------------------------------------------------------------------------------------------------------
a = """this is line 1
this is line 2
this is the last line and this line is 3"""
#print(a)
#print("""The following options are available:
#      -a       :does nothing
#      -b       :does nothing""")
#-----------------------------------------------------------------------------------------------------------------
#slicing
u = "How's it going?"
#u[start:end:step]
#print(u[4])
#print(type(u[4]))
#print(u[0:8])
#print(u[-1])
#print(u[-6:-1])
#print(u[0:12:2])
#print(u[:12])
#print(u[1:])
#print(u[::2])

#s[1] = 'e' #Error happens cuz str is inmutable

#-----------------------------------------------------------------------------------------------------------------
x = '                 abc def                     hgq    kaicenat'
y = x.strip() #cut off the first and last space no matter how long
#print(b)
#-----------------------------------------------------------------------------------------------------------------
g = 'aBCE deFg ;; sadfa UIO'
h = g.lower()
i = g.upper()
q = g.capitalize()
#print(h)
#print(i)
#print(q)
#-----------------------------------------------------------------------------------------------------------------
j = 'Rayquan Kai Rage Nicki'
k = j.replace('a','e')
l = j.replace('a', 'aaaaaaaaaaaaaaaa')
#print(k)
#print(l)
#-----------------------------------------------------------------------------------------------------------------
m = 'abc;def;hgydfa;yy23'
n = m.split(';')
#print(n)  #Become a list
#print(n[1])
#-----------------------------------------------------------------------------------------------------------------
o = 'June, you are still a begginer'
p = o.count('J') #count a specified str in str
#print(p)
#-----------------------------------------------------------------------------------------------------------------
#check if there's a specified str in str
#print('abc' in 'jajajkajkjfnhiorehfabcnnvanl') 
#-----------------------------------------------------------------------------------------------------------------
#check the superior one in terms of alphabetical order
#print("abc" == "abc")
#print("abc" < "def")
#print("abcdefghi" < 'def')
#-----------------------------------------------------------------------------------------------------------------
#How to "" something inside "" or ''
#print('we are learning 'string' here') #Error
#print('we are learning \'string\' here') 
#print('we are learning "string" here') 

#go to a new line
print('we are \n now on another line') 

#add tab
print('we are \t now on another line')

#ignore escape sequence \
print(r'c:\drive\name') #\n don't work







