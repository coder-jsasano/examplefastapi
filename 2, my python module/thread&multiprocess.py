#thread = a flow of excecution. Like a separate order of instruction.
#         However each thread take a turn running to achieve concurrency
#         GIL = Global Interpreter Lock
#         allows only one thread to hold the control of the Python interpreter

#cpu bound = program/task spends most of its time waiting for internal evants(CPU intensive)
#            use multiprocessing

#io bound = program/task spends most of its time waiting for external evants(user input, web scraping)
#           use multithreading 

import threading
import time

#def eat_breakfast():
#    time.sleep(3)
#    print("You eat breakfast")

#def drink_coffee():
#    time.sleep(4)
#    print("You drink coffee")

#def study():
#    time.sleep(5)
#    print("You finish studying")

#x = threading.Thread(target=eat_breakfast, args=())
#x.start()

#y = threading.Thread(target=drink_coffee, args=())
#y.start()

#z = threading.Thread(target=study, args=())
#z.start()

#x.join()
#y.join()
#z.join()

#eat_breakfast()
#drink_coffee()
#study()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())

#daemon thread = a thread that runs in the background, not important for program to run 
#                your program will not wait for daemon threads to complete before exiting
#                non-daemon threads cannot normally be killed, stay alive until task is complete
#                ex. background tasks, garbage collection, waiting for input, long running process

#import threading
#import time

#def timer():
#    print()
#    print()
#    count = 0
#    while True:
#        time.sleep(1)
#        count += 1
#        print("logged in for: ", count, "seconds")

#x = threading.Thread(target=timer, daemon=True)
#x.start()

#x.setDaemon(True)
#print(x.isDaemon())

#answer = input("Do you wish to exit?: ")

#------------------------------------------------------------------------------------------------------------------------------
#Python multiprocessing

#multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                  multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                  multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    
    print(cpu_count())
    a = Process(target = counter, args=(12000000,))
    b = Process(target = counter, args=(12000000,))
    c = Process(target = counter, args=(12000000,))
    d = Process(target = counter, args=(12000000,))
    e = Process(target = counter, args=(12000000,))
    f = Process(target = counter, args=(12000000,))
    g = Process(target = counter, args=(12000000,))
    h = Process(target = counter, args=(12000000,))
    
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    

    print("finished in:",time.perf_counter(),"seconds")



if __name__ == '__main__':
    main()


