#generator4.py
def prime_gen(num):
    for cand in range(2, num+1):
        for i in range (2, cand):
            if (cand % i) == 0:
                break
        else:
            yield cand

def x2_gen(list2):
    for num in list2:
        yield num*num

print(sum(x2_gen(prime_gen(5))))
