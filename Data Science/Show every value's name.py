#How to show every value's name and type 

# Display information about all variables in the current session
def whos():
    for name, value in globals().items():
        print(f"{name}: {type(value)} = {value}")

# Define some variables
x = 3
y = 5.3
z = 'Suck my dick'
b = True
c = 3 + 5j         # complex is only valid with j         

# Call the function to display variable information
whos()

#print(int((3**(1/2))))


