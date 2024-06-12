# * 
#result = 5 * 7 # Multiplication
#print(result)

#result = 2 ** 4 #power
#print(result)

#zeros = [0] * 10 #tuple() string"" is valid as well
#print(zeros)
#----------------------------------------------------------------------------------------------------
#def foo(a, b, *args, **kwargs):
#    print(a, b)
#    for arg in args:
#        print(arg)
#    for key in kwargs:
#        print(key, kwargs[key])

#foo(1, 2, 3, 4, 5, six=6, seven=7)
#--------------------------------------------------------------------------------------------------------------------------------------
#def foo(a, b, c):
#    print(a, b, c)

#my_list = [0, 1, 2]
#my_dict = {'a':1, 'b':2, 'c':3} #keys and numbers of argument must be equal parameters
#foo(*my_list)
#foo(**my_dict)
#--------------------------------------------------------------------------------------------------------------------------------------

#numbers = [1, 2, 3, 4, 5, 6]

#*beginning, last = numbers #Unpack the last item and only works for list
#beginning, *last = numbers #Unpack the first item and only works for list
#beginning, *middle, last = numbers #Unpack the first and last item and only works for list
#beginning, *middle, secondlast, last = numbers
#print(beginning)
#print(middle)
#print(secondlast)
#print(last)
#--------------------------------------------------------------------------------------------------------------------------------------
#my_tuple = (1, 2, 3)
#my_list = [4, 5, 6]
#my_set = [4, 5, 6]

#new_list = [*my_tuple, *my_list]
#new_list = [*my_tuple, *my_set]

#print(new_list)
#---------------------------------------------------------------------------------------------------------------------------------------
dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}

my_dict = {**dict_a, **dict_b}
print(my_dict)



