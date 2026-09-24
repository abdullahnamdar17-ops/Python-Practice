class Car:
    @staticmethod
    def start():
        print("Car has starting")
    
    @staticmethod
    def stop():
        print("Car has stopped")

class Toyota(Car):
    def __init__(self, model, color):
        self.model = model
        self.colour = color

s1 = Toyota("Altis", "Black")
s1.start()
print(s1.model, s1.colour)
s1.stop()