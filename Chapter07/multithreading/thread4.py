# thread4.py with queue and custom Thread class

from queue import Queue
from threading import Thread as Thread
from time import sleep

class MyWorker (Thread):
   def __init__(self, name, q):
      Thread.__init__(self)
      self.name = name
      self.queue = q

   def run(self):
      while True:
          item = self.queue.get()
          sleep(1)
          try:
              print ("{}: {}".format(self.name, item))
          finally:
            self.queue.task_done()

#filling the queue
myqueue = Queue()
for i in range (10):
    myqueue.put("Task {}".format(i+1))

# creating threads
for i in range (5):
    worker = MyWorker("Th {}".format(i+1), myqueue)
    worker.daemon = True
    worker.start()

myqueue.join()

