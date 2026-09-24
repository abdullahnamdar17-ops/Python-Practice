class Car:
    @staticmethod
    def start():
        print("Car has starting")
    
    @staticmethod
    def stop():
        print("Car has stopped")

class Toyota(Car):
    def __init__(self, make):
        self.make = make

class Fortuner(Toyota):
    def __init__(self, type, model):
        self.type = type
        self.model = model
        self.make = "Toyota"

s1 = Fortuner("SUV", "Fortuner Sigma 4x4")
print(s1.make, s1.type, s1.model)
s1.start()
s1.stop()
