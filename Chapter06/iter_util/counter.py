#Counter.py
from collections import Counter

#applying counter on a string object
print(Counter("people"))

#applying counter on a list object
my_counter = Counter([1,2,1,2,3,4,1,3])
print(my_counter.most_common(1))
print(list(my_counter.elements()))

#applying counter on a dict object
print(Counter({'A': 2, 'B': 2, 'C': 4, 'C': 4}))

