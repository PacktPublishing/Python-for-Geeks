#gencomp1.py

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen1 =	(x for x in list1 if x % 2 ==0)
print(list(gen1))
