# process2.py to create processes using a pool
import os
from multiprocessing import Process, Pool, current_process as cp
from time import sleep

def print_message(msg):
    sleep(1)
    print("{}-{}: {}".format(os.getpid(), cp().name, msg))


def main():
    # creating process from a pool
    with Pool(3) as proc:
        proc.map(print_message, ["Orange", "Apple", "Banana",
                                 "Grapes","Pears"])

    print("Exiting the main process")

if __name__ == '__main__':
    main()