#threads_casestudy.py
from queue import Queue
from threading import Thread
import time

from getfilelistpy import getfilelist
import gdown
THREAD_POOL_SIZE = 5

#update the resource object as per your API key and the gdriver folder id
resource = {
    "api_key": "AIzaSyDYKmm85keq4bF1DpYa2bxddKrGns4z0",
    "id": "0B8TxHW2Ci6dbckVwtTlV3RUU",
    "fields": "files(name,id,webContentLink)",
}

class DownlaodWorker(Thread):

    def __init__(self, name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            # Get the file id and name from the queue
            item1 = self.queue.get()
            try:
                gdown.download( item1['webContentLink'],
                                './files/{}'.format(item1['name']),
                                quiet=False)
            finally:
                self.queue.task_done()

def main():
    def get_files(resource):
        #global files_list
        res = getfilelist.GetFileList(resource)
        files_list = res['fileList'][0]
        return files_list

    start_time = time.monotonic()

    files = get_files(resource)

    #add files info into the queue
    queue = Queue()
    for item in files['files']:
        queue.put(item)

    for i in range (THREAD_POOL_SIZE):
        worker = DownlaodWorker("Thread {}".format(i+1),queue)
        worker.daemon = True
        worker.start()

    queue.join()
    end_time = time.monotonic()
    print('Time taken to download: {} seconds'.
          format( end_time - start_time))
main()
