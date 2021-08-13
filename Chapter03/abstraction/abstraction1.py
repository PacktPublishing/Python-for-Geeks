#abstraction1.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def hello(self):
        print(f"Hello from abstract class")
    @abstractmethod
    def print_me(self):
       pass

class Car (Vehicle):
    def __init__(self, color, seats):
        self.i_color = color
        self.i_seats = seats

    """It is must to implemented this method"""
    def print_me(self):
        print( f"Car with color {self.i_color} and no of seats {self.i_seats}")

if __name__ == "__main__":
    #vehicle = Vehicle()
    #vehicle.hello()
    car = Car ("blue", 5)
    car.print_me()
    car.hello()