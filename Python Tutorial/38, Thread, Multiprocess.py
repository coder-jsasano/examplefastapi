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

def eat_breakfast():
    time.sleep(3)
    print('You ate breakfast')

def drink_coffee():
    time.sleep(4)
    print('You drank coffee')

def study():
    time.sleep(5)
    print('You finish studing')

#Run program concurrently!
x = threading.Thread(target=eat_breakfast, args=())
#x.start()

y = threading.Thread(target=drink_coffee, args=())
#y.start()

z = threading.Thread(target=study, args=())
#z.start()

#Skip every threads and run first
#x.join()
#y.join()
#z.join()

#eat_breakfast()
#drink_coffee()
#study()

#print(threading.active_count())#Count how many threads 
#print(threading.enumerate())#print a list of all the threads running
#print(time.perf_counter())#how long it takes calling threads to finish its set of instructions
#-------------------------------------------------------------------------------------------------------------------------------------------
#daemon thread = a thread that runs in the background, not important for program to run 
#                your program will not wait for daemon threads to complete before exiting
#                non-daemon threads cannot normally be killed, stay alive until task is complete

#                ex. background tasks, garbage collection, waiting for input, long running process

def timer():
    print()
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        if count == 1:
            print('Logged in for: ',count,'second')
        else:
            print('Logged in for: ',count,'seconds')

a = threading.Thread(target=timer, daemon=True)
#a.start()
#a.setDaemon(True)
#print(a.isDaemon)#check if daemon or not

#answer = input("Do you wish to exit?")

#Python multiprocessing
#-------------------------------------------------------------------------------------------------------------------------------------------
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

    a = Process(target=counter, args=(2500,))
    b = Process(target=counter, args=(2500,))
    c = Process(target=counter, args=(2500,))
    d = Process(target=counter, args=(2500,))
    
    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print('Finished in: ',time.perf_counter(),' seconds')


if __name__ == '__main__':
    main()

