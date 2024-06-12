#Strings  = immutable
#my_string = """Hello
#World""" 
#'I\'m a programmer' #"Hello World"
#print(my_string)

#my_string = "Hello World"
#char = my_string[0] #Show the character of a specified index

#substring = my_string[:5:1]
#print(substring)

#greeting = "Hello"
#name = "Jquan"
#sentence = greeting + " " + name
#print(sentence)

#for i in greeting:
#    print(i)

#if "ell" in greeting:
#    print(True)
#else:
#    print(False)

#my_string = "Hello World"
#my_string = my_string.strip() #Remove space except for in between one
#print(my_string)
#print(my_string.upper()) #Capitalize every elements
#print(my_string.lower()) #Lowercase every elements
#print(my_string.startswith("H")) #Check the word that start with
#print(my_string.endswith("H")) #Check the word that start with from the last word

#print(my_string.find("H")) #Show the index number of a specified word, if not detected it will say "-1"
#print(my_string.count("H")) #Count the number of specified words

#print(my_string.replace("World", "Gang"))

#my_string = "How are ya doing?"
#my_list = my_string.split() #Split each elements
#new_string = " ".join(my_list) #Put on elements each other without spaces
#print(new_string)

#from timeit import default_timer as timer


#my_list = ["a"] * 1000
#print(my_list)

#my_string = ""
#start = timer()
#for i in my_list:
#    my_string += i
#stop = timer()
#print(stop-start) 

##start = timer()
#my_string = "".join(my_list)
#stop = timer()
#print(stop-start)

var =  3.12345 #3 #"Jquan"
var2 = 6
#my_string = "The variable is %s" % var #Insert a str word 
#my_string = "The variable is %i" % var #Insert a int word
#my_string = "The variable is %.3f" % var #Insert a floting word
#my_string = "The variable is {:.2f} and {}".format(var, var2)

#Easiest to insert floting and int 
my_string = f"The variable is {var*2} and {var2}"

print(my_string)



