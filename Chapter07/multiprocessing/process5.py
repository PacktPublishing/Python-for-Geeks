# process5.py to use queue to exchange data

from multiprocessing import Process
from multiprocessing import Queue

def copy_data (list, myqueue):
    for num in list:
        myqueue.put(num)

def output(myqueue):
    while not myqueue.empty():
        print(myqueue.get())

mylist = [2, 5, 7]
myqueue = Queue()

p1 = Process(target=copy_data, args=(mylist, myqueue))
p2 = Process(target=output, args=(myqueue,))

p1.start()
p1.join()
p2.start()
p2.join()

print("Queue is empty: ",myqueue.empty())
print("Exiting the main process")
