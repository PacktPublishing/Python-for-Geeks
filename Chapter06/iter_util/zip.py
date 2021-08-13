#zip.py

num_list = [1, 2, 3, 4, 5, 6]
lett_list = ['alpha', 'bravo', 'charlie', 'delta']

zipped_iter = zip(num_list,lett_list)
print(next(zipped_iter))
print(next(zipped_iter))
print(list(zipped_iter))
