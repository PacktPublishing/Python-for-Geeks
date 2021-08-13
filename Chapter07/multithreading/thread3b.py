# thread3b.py when  thread synchronization is used

from threading import Lock, Thread as Thread

def inc_with_lock (lock):
    global x
    for _ in range(1000000):
        lock.acquire()
        x+=1
        lock.release()

x = 0
mylock = Lock()
# creating threads
t1 = Thread(target=inc_with_lock , args=(mylock,), name="Th 1")
t2 = Thread(target=inc_with_lock , args=(mylock,), name="Th 2")

# start the threads
t1.start()
t2.start()

#wait for the threads
t1.join()
t2.join()
print("final value of x :", x)


