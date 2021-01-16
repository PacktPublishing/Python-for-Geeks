# calcmain2.py with  alias for modules
import mycalculator as calc
import myrandom as rand


def my_main():
    """ This is a main function which generates two random numbers and then apply calculator functions on them """
    x = rand.random_2d()
    y = rand.random_1d()

    sum = calc.add(x,y)
    diff = calc.subtract(x,y)

    print("x = {}, y = {}".format(x,y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))

    print (globals())

""" This is executed only if the special variable '__name__' is set as main"""
if __name__ == "__main__":
    my_main()