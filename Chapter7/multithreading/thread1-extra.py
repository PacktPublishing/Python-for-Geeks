# thread1-extra.py to create simple threads with function (using threads list to simplly the code)

import threading
from threading import Thread as Thread
from time import sleep

def print_hello():
    sleep(2)
    print("{}: Hello".format(threading.current_thread().name))

def print_message(msg):
    sleep(1)
    print("{}: {}".format(threading.current_thread().name, msg))

threads = []
# creating threads
threads.append(Thread(target=print_hello, name="Th 1"))
threads.append(Thread(target=print_hello, name="Th 2"))
threads.append(Thread(target=print_message, args=["Good morning"], name="Th 3"))

# start the threads
for th in threads:
    th.start()

# wait till all are done
for th in threads:
    th.join()
