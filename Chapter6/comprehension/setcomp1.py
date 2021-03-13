#setcomp1.py


list1 = [1, 2, 6, 4, 5, 6, 7, 8, 9, 10, 8]
set1 =	{x for x in list1 if x % 2 ==0}
print(set1)

set2 = set()
for x in list1:
    if x % 2 == 0:
        set2.add(x)
print(set2)