#carwithinnerexample1.py
class Car:
    """outer class"""
    c_mileage_units = "Mi"
    def __init__(self, color, miles, eng_size):
        self.i_color = color
        self.i_mileage = miles
        self.i_engine = self.Engine(eng_size)

    def __str__(self):
        return f"car with color {self.i_color}, mileage {self.i_mileage} and engine of {self.i_engine}"

    class Engine:
        """inner class"""
        def __init__(self, size):
            self.i_size = size

        def __str__(self):
            return self.i_size


if __name__ == "__main__":
    car = Car ("blue", 1000, "2.5L")
    print (car)
    print (car.i_engine.i_size)
