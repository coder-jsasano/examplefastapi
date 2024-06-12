#time module

import time

#print(time.ctime(0)) #convert a time expressed in seconds since epoch to a readable strings
                     #epoch = when you computer thinks time began 

#print(time.time()) #return current seconds since epoch

#print(time.ctime(time.time()))

#time_objects = time.localtime()
#time_objects = time.gmtime() #UTC = time at 0 degree longitude
#print(time_objects)
#local_time = time.strftime("%B %D %Y %H:%M %S",time_objects)
#time.strftime(format, time_objects)
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string,"%d %B, %Y")
#print(time_object)

#(year, month, day, hours, minutes, secs, day of week, day of the year, dst)
time_tuple = (2024, 3, 31, 4, 20, 0, 0, 0, 0)
#time_string = time.asctime(time_tuple)
time_string = time.mktime(time_tuple)
print(time_string)


