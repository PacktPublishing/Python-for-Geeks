#itertools_accumulate.py
import itertools
import operator

data = [1, 3, 5]
res = itertools.accumulate(data)
print("default:")
for x in res:
    print(x)
res = itertools.accumulate(data, operator.mul)
print("Multiply:" )
for x in res:
    print(x)
