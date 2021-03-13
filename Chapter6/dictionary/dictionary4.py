# dictionary4.py

dict1 = {100:{'name':'John', 'age':24},
         101:{'name':'Mike', 'age':22},
         102:{'name':'Jim', 'age':21} }

del (dict1[101]['age'])
print(dict1)
dict1[102].pop('age')
print(dict1)