class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def getDetails(self):
        pass
        print("Make of the car: ", self.make)
        print("Manufactured Year: ", self.year)
        print("Color of the car: ", self.color)
    def drive(self):
        print("This " + self.model + " is driving.")
    def stop(self):
        print("This " + self.model + " is stopping.")
        print("-------------------------------------------")