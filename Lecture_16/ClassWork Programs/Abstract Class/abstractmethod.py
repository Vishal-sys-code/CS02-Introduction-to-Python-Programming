from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
class Car(Vehicle):
    def go(self):
        print("Car")
class motorCycle(Vehicle):
    def go(self):
        print("Bike")

car = Car()
motor = motorCycle()
car.go()
motor.go()
car.stop()
motor.stop()