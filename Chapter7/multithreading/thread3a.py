# thread3a.py when no thread synchronization used

from threading import Thread as Thread

def inc():
    global x
    for _ in range(1000000):
        x+=1

#global variable
x = 0

# creating threads
t1 = Thread(target=inc, name="Th 1")
t2 = Thread(target=inc, name="Th 2")

# start the threads
t1.start()
t2.start()

#wait for the threads
t1.join()
t2.join()

print("final value of x :", x)


