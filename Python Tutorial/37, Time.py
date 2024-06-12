#epoch = when your computer thinks time began
import time

#print(time.ctime(0)) #convert a time expressed in seconds since epoch to a redable

#print(time.time()) #return current seconds since epoch

#print(time.ctime(time.time())) #current date and time
time_object = time.localtime() #more detail
#print(time_object)

#Python time directive
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)

#.gmtime() = show the time at 0 degree longitude
utc_time = time.gmtime()
#print(utc_time)

#.strptime(str, format) = show the detal time based on set time
time_string = "05 May, 2024"
time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)


#.asctime(tuple) = make the set time readable
#(year, month, day, hours, minutes, secs, #dayof the week, #day of the year, dst)
time_tuple = (2024, 5, 5, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
#print(time_string)

#.mktime(tuple) = show current sec from epoch to set time
#(year, month, day, hours, minutes, secs, #dayof the week, #day of the year, dst)
time_tuple = (2024, 5, 5, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) 
#print(time_string)
