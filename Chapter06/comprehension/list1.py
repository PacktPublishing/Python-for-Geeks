#list1.py

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 =	[x+1 for x in list1]
print(list2)

list3 = []
for x in list1:
    list3.append(x+1)
print(list3)