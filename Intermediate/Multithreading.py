from threading import Thread, Lock, current_thread
from queue import Queue
import time
#def square_numbers():
#    for i in range(100):
#        i * i
#        time.sleep(0.1)


#if __name__ as "__main__":
#    threads = []
#    num_threads = 10

#create threads
#for i in range(num_threads):
#    t = Thread(target=square_numbers)
#    threads.append(t)

#start
#for t in threads:
#    t.start()

#join threads: wait for them to complete
#for t in threads:
#    t.join()

#print('end main')


#database_value = 0


#def increase(lock):
#    global database_value

    #lock.acquire()
    #local_copy = database_value
    #processing
    #local_copy += 1
    #time.sleep(0.1)
    #database_value = local_copy
    #lock.release()

#         or            #

#    with lock:
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
    


#if __name__ == "__main__":

#    lock = Lock()

#    print('start value', database_value)

#    thread1 = Thread(target=increase, args=(lock,))
#    thread2 = Thread(target=increase, args=(lock,))

#    thread1.start()
#    thread2.start()

#    thread1.join()
#    thread2.join()

#    print('end value', database_value)

#    print('end main')




#if __name__ == "__main__":

#        q = Queue()

#        q.put(1)
#        q.put(2)
#        q.put(3)

        #3 2 1 ->
#        first = q.get()
#        print(first)

#        q.task_done()
#        q.join()



#print('end main')


def worker(q, lock):
        while True:
               value = q.get()

               #processing
               with lock:
                      print(f'in {current_thread().name} got {value}')
               q.task_done()



if __name__ == "__main__":

        q = Queue()
        lock = Lock()
        num_threads = 10

        for i in range(num_threads):
                thread = Thread(target=worker, args=(q, lock))
                thread.daemon=True
                thread.start()
        
        for i in range(1, 21):
                q.put(i)

        q.join()




print('end main')



