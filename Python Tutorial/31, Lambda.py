#lambda = function written in 1 line using lambda keyword
#         accept any number of arguments, but only has one expression
#         (think of it as a shortcut)

#syntax: lambda parameters:expression

#def double(x):
#    return x*2

#print(double(6))

double = lambda x: x * 2
multiply = lambda x,y: x * y
add = lambda x,y,z : x + y + z
full_name = lambda first_name, last_name: first_name +" "+ last_name
minor_check = lambda age: True if age >= 18 else False
#print(double(9))
#print(multiply(5,3))
#print(add(1,2,3))
#print(full_name("Jquan","Lee"))
#print(minor_check(13))
#----------------------------------------------------------------------------------------------------------------------------
#.sort() method = used with lists
#sort() function = used with iterable

#students = ["Kai", "Speed", "Adin", "Ray", "Jquan"]
students = ("Kai", "Speed", "Adin", "Ray", "Jquan")

#students.sort()
#students.sort(reverse=True) #reverse alphabetical order
#sorted_stutents = sorted(students)
#sorted_stutents = sorted(students,reverse=True)

#for i in students:
#    print(i)

#for i in sorted_stutents:
#    print(i)
#----------------------------------------------------------------------------------------------------------------------------
menbers = [("Nicki", "A", 27),
           ("Ice", "C", 24),
           ("SZA", "S", 33),
           ("Sexy Red", "F", 26),
           ("Cardi", "D", 27)]

menbers2 = (("Nicki", "A", 27),
           ("Ice", "C", 24),
           ("SZA", "S", 33),
           ("Sexy Red", "F", 26),
           ("Cardi", "D", 27))

grade = lambda grades: grades[1]
age = lambda ages: ages[2]

#menbers.sort(key=grade)
menbers.sort(key=age,reverse=True)
sorted_members = sorted(menbers2,key=age)


for i in menbers:
    print(i)
print()
for i in sorted_members:
    print(i)



