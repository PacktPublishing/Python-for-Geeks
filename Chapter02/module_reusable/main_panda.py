
import mypanda

def my_main():

    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98]}

    mypanda.print_dataframe (dict)

""" This is executed only if the special variable '__name__' is set as main"""
if __name__ == "__main__":
    my_main()