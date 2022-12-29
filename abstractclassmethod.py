from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(seld):
        print("this motorcycle is stopped")
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

