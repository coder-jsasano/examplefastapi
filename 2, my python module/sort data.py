#sort() method = used with lists
#sort() function = used with iterables

#students = ["Squidward","Kai Cenat","Rayquan Lee","Peter Parker","Fanum"]

#students.sort(reverse=True)
#sorted_students = sorted(students,reverse=True)

#for i in sorted_students:
#    print(i)


#students = [("Squidward","F",60),
#            ("Kai Cenat","A",22),
#            ("Rayquan Lee","D",18),
#            ("Peter Parker","S",23),
#            ("Fanum","F",26)]

students = (("Squidward","F",60),
            ("Kai Cenat","A",22),
            ("Rayquan Lee","D",18),
            ("Peter Parker","S",23),
            ("Fanum","F",26))
#grade = lambda grades:grades[1]
age = lambda ages:ages[2]

#students.sort(key=age) >>>>for lists[]
#sorted_students = sorted(students,key=age) >>>>for double ()
#for i in students:
#    print(i)
#for i in sorted_students:
#    print(i)