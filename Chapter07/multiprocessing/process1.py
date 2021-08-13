# process1.py to create simple processes with function
import os
from multiprocessing import Process, current_process as cp
from time import sleep

def print_hello():
    sleep(2)
    print("{}-{}: Hello".format(os.getpid(), cp().name))


def print_message(msg):
    sleep(1)
    print("{}-{}: {}".format(os.getpid(), cp().name, msg))

processes = []

# creating process
processes.append(Process(target=print_hello, name="Process 1"))
processes.append(Process(target=print_hello, name="Process 2"))
processes.append(Process(target=print_message,
                         args=["Good morning"], name="Process 3"))

# start the process
for p in processes:
    p.start()

# wait till all are done
for p in processes:
    p.join()

print("Exiting the main process")
