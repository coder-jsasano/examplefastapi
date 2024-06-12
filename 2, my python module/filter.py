#filter() = creates a collection of elements from an iterable for witch a function returns

#filter(function,iterable)

friends = [("Agent",19),
           ("Kai",22),
           ("Ray",17),
           ("Duke",28),
           ("Chris",25),
           ("Davis",25),
           ("Fanum",25)]

age = lambda data : data[1] >= 20

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
