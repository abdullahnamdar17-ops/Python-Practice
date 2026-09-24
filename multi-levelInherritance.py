class Car:
    def __init__(self, colour):
        self.colour = colour

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
    def __init__(self, type, model,):
        self.type = type
        self.model = model
        super().start()

s1 = Fortuner("SUV", "Fortuner Sigma 4x4")
s2 = Toyota("Honda") 
print(s2.make)
print(s1.type, s1.model)
s1.stop()
