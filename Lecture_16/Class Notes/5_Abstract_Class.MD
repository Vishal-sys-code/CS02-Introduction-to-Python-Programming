# **Abstract Class**
* Prevents a user from creating an object of that class.
* It compels the user to override abstract methods in a child class.
* Abstract Class: A class which contains one or more abstract methods
* Abstract method: A method that has a declaration but doesn't have an implementation.

```py
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
```