#itertools_cycle.py
import itertools

letters = ['A','B','C']
for letter in itertools.cycle(letters):
    print(letter)
letters = ['A','B','C']
iter1, iter2 = itertools.tee(letters)

for x in iter1:
    print(x)

for x in iter2:
    print(x)