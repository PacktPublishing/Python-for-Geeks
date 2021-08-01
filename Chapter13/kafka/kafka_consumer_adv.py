#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import sys
from kafka import KafkaConsumer

"""Collect command-line options in a dictionary"""

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

class Consumer(multiprocessing.Process):
    host_id = ''
    topic_id = ''
    def __init__(self, host, topic):
        self.host_id = host + ''
        self.topic_id = topic
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()
        
    def stop(self):
        self.stop_event.set()
        
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.host_id,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000,
                                 api_version=(0, 8, 0))
        consumer.subscribe([self.topic_id])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                print("---------------------------------------")
                if self.stop_event.is_set():
                    break

        consumer.close()
        
        
def main():
    from sys import argv
    myargs = getopts(argv)
    HOST_IP=''
    TOPIC=''

    if '-host' in myargs:  # Example usage.
        HOST_IP = myargs['-host']
    else:
        print ('please use as follows python kafka_test_consumer.py -host HostIP -topic TOPIC')

    if '-topic' in myargs:  # Example usage.
        TOPIC = myargs['-topic']
    else:
        print ('please use as follows python kafka_test_consumer.py -host HostIP -topic TOPIC')
    print(myargs)

    tasks = [
        # Producer(),
        Consumer(HOST_IP,TOPIC)
    ]

    for t in tasks:
        t.start()

    # time.sleep(10)
    
    # for task in tasks:
    #     task.stop()

    for task in tasks:
        task.join()
        
        
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
