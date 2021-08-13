#iterator1.py
#example 1: iterating on a list
for x in [1,2,3]:
    print(x)

#example 2: iterating on a string
for x in "Python for Geeks":
    print(x, end="")
print('')

#example 3: iterating on a dictionary
week_days = {1:'Mon', 2:'Tue',
             3:'Wed', 4:'Thu',
             5:'Fri', 6:'Sat', 7:'Sun'}
for k in week_days:
	print(k, week_days[k])

#example 4: iterating on a file
for row in open('abc.txt'):
    print(row, end="")