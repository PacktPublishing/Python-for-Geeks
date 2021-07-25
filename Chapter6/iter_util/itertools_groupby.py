#itertools_groupby.py
import itertools

mylist = [("A", 100), ("A", 200), ("B", 30), ("B", 10)]
def get_key(group):
    return group[0]

for key, grp in itertools.groupby(mylist, get_key):
    print(key + "-->", list(grp))