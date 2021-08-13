#dictcomp1.py

dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 =	{x : int(y/2) for (x, y) in dict1.items() if y <=200}
print(dict2)

dict3 = {}
for x,y in dict1.items():
    if y <= 200:
        dict3[x] = int(y/2)
print(dict3)