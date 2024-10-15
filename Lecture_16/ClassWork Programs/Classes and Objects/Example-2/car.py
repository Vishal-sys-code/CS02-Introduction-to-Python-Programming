class Car:
    wheels = 4 # class variable
    def __init__(self, make, model, year, color):
        self.make = make # instance variable 1
        self.model = model # instance variable 2
        self.year = year # instance variable 3
        self.color = color # instance variable 4

# Each object has their own unique values assigned to each of the variables