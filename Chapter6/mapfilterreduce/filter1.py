# filter1.py to get even numbers from a list

def is_even(num):
    return (num % 2 == 0)

mylist = [1, 2, 3, 4, 5,6,7,8,9]
new_list = list(filter(is_even, mylist))
print(new_list)
