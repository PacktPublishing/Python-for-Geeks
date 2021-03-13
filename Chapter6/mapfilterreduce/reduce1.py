# reduce1.py to get sum of numbers from a list
from functools import reduce

def seq_sum(num1, num2):
    return num1+num2

mylist = [1, 2, 3, 4, 5]
result = reduce(seq_sum, mylist, 10)
print(result)
