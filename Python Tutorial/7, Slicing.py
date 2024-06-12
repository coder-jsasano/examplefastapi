#slicing = [start(exclusive):stop(inclusive):step] or slice(start,stop,step)

name = 'Jquan Lee'

first_name = name[:5]
last_name = name[6:10]
funcky_name = name[::3]
reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funcky_name)
#print(reversed_name)

website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website[slice])
print(website2[slice])


