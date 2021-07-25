#itertools_chain.py
import itertools

list1 = ['A','B','C']
list2 = ['W','X','Y','Z']

chained_iter = itertools.chain(list1, list2)
for x in chained_iter:
    print(x)