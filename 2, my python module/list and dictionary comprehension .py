#list comprehension = a way to create a new list with less syntax
#                     can mimic certain lambda functions, easier to read
#                     list = [expression (if/else) for item in iterable]


#squares = []              #create an empty list
#for i in range(1,11):     #create a for loop
#    squares.append(i * i) #define what each loop iteration should do
#print(squares)

#squares = [i * i for i in range(1,11)]
#print(squares)


students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x : x >=60, students))

#passed_students = [i for i in students if i >= 60]

#passed_students = [i if i >= 60 else "Failed" for i in students]

#print(passed_students)

#dictionary comprehension = create dictionaries using an expression
#                           can replace for loops and certain lambda functions

#dictionary = {key: expression for (key,value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
#dictionary = {key: (if,else) for (key,value) in iterable}
#dictionary = {key: function(value) for (key,value) in iterable}
#------------------------------------------------------------------------------------------------
#cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

#cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

#print(cities_in_C)
#-----------------------------------------------------------------------------------------------------------
#weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}

#sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}

#print(sunny_weather)
#-----------------------------------------------------------------------------------------------------------
#cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

#desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}

#print(desc_cities)
#-------------------------------------------------------------------------------------------------------------
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value > 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)




