# process3.py to use shared memory ctype objects

import multiprocessing
from multiprocessing import Process, Pool, current_process as cp

def inc_sum_list(list, inc_list, sum):
    sum.value = 0

    for index, num in enumerate(list):
        inc_list[index] = num + 1
        sum.value = sum.value + inc_list[index]

def main():

    mylist = [2, 5, 7]

    inc_list = multiprocessing.Array('i', 3)

    sum = multiprocessing.Value('i')

    p = Process(target=inc_sum_list,
                args=(mylist, inc_list, sum))

    p.start()
    p.join()
    print("incremented list: ", list(inc_list))
    print("sum of inc list: ", sum.value)

    print("Exiting the main process")

if __name__ == '__main__':
    main()