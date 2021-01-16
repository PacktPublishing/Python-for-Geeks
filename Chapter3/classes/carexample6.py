#carexample6.py
class Car:
    __mileage_units = "Mi"
    def __init__(self, col, mil):
        self.__color = col
        self.__mileage = mil

    def __str__(self):
        return f"car with color {self.get_color()} and mileage {self.get_mileage()}"

    def get_color(self):
        return self.__color

    def get_mileage(self):
        return self.__mileage

    def set_mileage (self, new_mil):
            self.__mileage = new_mil


if __name__ == "__main__":
    car = Car ("blue", 1000)

    print (car)
    print (car.get_color())
    print(car.get_mileage())
    car.set_mileage(2000)
    print (car.get_color())
    print(car.get_mileage())

