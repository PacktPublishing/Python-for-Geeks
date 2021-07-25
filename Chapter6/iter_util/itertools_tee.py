#itertools_tee.py
import itertools

letters = ['A','B','C']
iter1, iter2 = itertools.tee(letters)

for x in iter1:
    print(x)

for x in iter2:
    print(x)