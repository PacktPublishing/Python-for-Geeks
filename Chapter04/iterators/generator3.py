#generator3.py
L = [1,2,3,4,5,6,7,8,9,0]
f1 = [x+1 for x in L]
g1 = (x+1 for x in L)

print(g1.__next__())
print(g1.__next__())
