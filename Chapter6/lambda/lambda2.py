# lambda2.py to get even numbers from a list

mylist = [1, 2, 3, 4, 5,6,7,8,9]
new_list = list(filter(lambda x: x % 2 == 0, mylist))
print(new_list)
