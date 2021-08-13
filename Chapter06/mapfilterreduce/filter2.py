# filter1.py to get even numbers from a list

def is_dublicate(item):
    return not(item in mylist)

mylist = ["Orange","Apple", "Banana", "Peach", "Banana"]
new_list = list(filter(is_dublicate, mylist))
print(new_list)
