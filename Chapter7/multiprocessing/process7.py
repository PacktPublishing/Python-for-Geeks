# process7.py to show synchronization and locking
from functools import partial
from multiprocessing import Pool, Manager

def printme (lock, msg):
    lock.acquire()
    try:
        print(msg)
    finally:
        lock.release()

with Pool(3) as proc:
    lock = Manager().Lock()
    func = partial(printme,lock)
    proc.map(func, ["Orange", "Apple", "Banana",
                             "Grapes","Pears"])

print("Exiting the main process")
