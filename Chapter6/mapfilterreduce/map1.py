#map1.py to get sqauare of each item in a list

mylist = [1, 2, 3, 4, 5]
new_list = []

for item in mylist:
    square = item*item
    new_list.append(square)

print(new_list)