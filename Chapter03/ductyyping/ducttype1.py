#ducttype1.py
class Car:
    def start(self):
        print ("start engine by ignition /battery")

class Cycle:
    def start(self):
        print ("start by pushing paddles")

class Horse:
    def start(self):
        print ("start by pulling/releasing the reins")


if __name__ == "__main__":
    for obj in Car(), Cycle(), Horse():
        obj.start()