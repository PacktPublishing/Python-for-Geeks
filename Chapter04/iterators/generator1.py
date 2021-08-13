#generators1.py
def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'


if(__name__ == "__main__"):
    iter1 = my_gen()
    print(iter1.__next__())
    print(next(iter1))
    print(iter1.__next__())
