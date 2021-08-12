# calcmain1.py with a main function
import mycalculator
import myrandom

def my_main( ):
    """ This is a main function which generates two random numbers      and then apply calculator functions on them """
    x = myrandom.random_2d( )
    y = myrandom.random_1d( )
    sum = mycalculator.add(x, y)
    diff = mycalculator.subtract(x, y)

    print("x = {}, y = {}".format(x, y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))

""" This is executed only if the special variable '__name__' is set as main"""
if __name__ == "__main__":
    my_main()
