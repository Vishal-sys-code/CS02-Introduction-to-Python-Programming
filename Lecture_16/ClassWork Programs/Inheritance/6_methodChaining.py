class Car:
    def turn_on(self):
        print("You started the engine")
        return self
    def drive(self):
        print("You drove the car")
        return self
    def brake(self):
        print("You applied the brake on the Car")
        return self
    def turn_off(self):
        print("You turned off the engine")
        return self
car = Car()
print("Without Method Chaining: ")
car.turn_on()
car.drive()
car.brake()
car.turn_off()

# Method Chaining
print("\nWith Method Chaining: ")
car.turn_on().drive()
car.brake().turn_off()
car.turn_on().drive().brake().turn_off()

"""
Output:
Without Method Chaining: 
You started the engine
You drove the car
You applied the brake on the Car
You turned off the engine

With Method Chaining:
You started the engine
You drove the car
You applied the brake on the Car
You turned off the engine
You started the engine
You drove the car
You applied the brake on the Car
You turned off the engine
"""