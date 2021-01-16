#carexampl4.py
class Car:
    c_mileage_units = "Mi"
    def __init__(self, color, miles):
        self.i_color = color
        self.i_mileage = miles

    def __str__(self):
        return f"car with color {self.i_color} and mileage {self.i_mileage}"

if __name__ == "__main__":
    car1 = Car ("blue", 1000)
    print (str(car1))
    print(repr(car1))
    print(dir(car1))
