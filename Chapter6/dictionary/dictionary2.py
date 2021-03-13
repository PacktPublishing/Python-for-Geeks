# dictionary2.py
#defining inner dictionary 1
student100 = {'name': 'John', 'age': 24}

#defining inner dictionary 2
student101 = {}
student101['name'] = 'Mike'
student101['age'] = '22'

#assiging inner dictionaries 1 and 2 to a root dictionary
dict1 = {}
dict1[100] = student100
dict1[101] = student101

#creating inner dictionary directly inside a root dictionary
dict1[102] = {}
dict1[102]['name'] = 'Jim'
dict1[102]['age'] = '21'

print(dict1)
print(dict1.get(102))
