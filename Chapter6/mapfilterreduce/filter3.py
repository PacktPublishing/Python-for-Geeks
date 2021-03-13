# filter1.py to get even numbers from a list

def is_even(num):
    return (num % 2 == 0)

def contains_e(name):
    return 'e' in name

mylist1 = [1, 2, 3, 4, 5,6,7,8,9]
mylist2 = ["Orange","Apple", "Banana", "Peach", "Banana"]
new_list1 = list(filter(is_even, mylist1))
new_list2 = list(filter(contains_e, mylist2))
print(new_list1)
print(new_list2)
