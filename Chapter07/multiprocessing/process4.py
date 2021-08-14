# process4.py to use shared memory using the server process

import multiprocessing
from multiprocessing import Process

def insert_data (dict1, code, subject):
    dict1[code] =  subject

def output(dict1):
    print("Dictionary data: ", dict1)

def main():
    with multiprocessing.Manager() as mgr:
        # create a dictionary in the server process
        mydict = mgr.dict({100: "Maths", 200: "Science"})

        p1 = Process(target=insert_data, args=(mydict, 300, "English"))
        p2 = Process(target=insert_data, args=(mydict, 400, "French"))
        p3 = Process(target=output, args=(mydict,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        p3.start()
        p3.join()

    print("Exiting the main process")

if __name__ == '__main__':
    main()