#str.format() = optional method that give users more control when displaying output

animal = 'cow'
item = 'moon'

#print('The '+animal+' jumped over the '+item)

#format method

#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) #positional argument
#print("The {animal} jumped over the {animal}".format(animal='cow',item='moon')) #keyword argument
#---------------------------------------------------------------------------------------------------------------------------
#text = 'The {} jumped over the {}'
#print(text.format(animal, item))
#---------------------------------------------------------------------------------------------------------------------------
name = 'Jquan'

#print('Hello! My name is {}'.format(name))
#print('Hello! My name is {:10}. Nice to meet ya'.format(name)) #{:} = you can add specified numbers of space and set an alingnment
#print('Hello! My name is {:<10}. Nice to meet ya'.format(name)) #left alined
#print('Hello! My name is {:>10}. Nice to meet ya'.format(name)) #right
#print('Hello! My name is {:^10}. Nice to meet ya'.format(name)) #center
#print('Hello! My name is {:10}. Nice to meet ya'.format(name)) #{:} = you can add specified numbers of space

#You can put a positional argument or keyward argument to a format field
#print('Hello! My name is {0:10}. Nice to meet ya'.format(name)) 
#print('Hello! My name is {name:10}. Nice to meet ya'.format(name)) 
#---------------------------------------------------------------------------------------------------------------------------
#number = 3.14159
number = 1000
print('The number pi is {:.2f}'.format(number)) #{:.numf} = show specified decimal numbers 
print('The number pi is {:,}'.format(number)) #{:,} = add comma to between 1000 digit and 100 digit and so on
print('The number pi is {:b}'.format(number)) #{:b} = show binary number
print('The number pi is {:o}'.format(number)) #{:o} = show octal number
print('The number pi is {:X}'.format(number)) #{:X} = show hexidecimal
print('The number pi is {:E}'.format(number)) #{:E} = show scientific numbers 




