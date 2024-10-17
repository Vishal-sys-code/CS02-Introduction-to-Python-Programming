class Car:
    name = None
class motorCycle:
    name = None
def changeColor(Car, name):
    car.name = name
def changeColor(motorCycle, name):
    motorCycle.name = name

car_1 = Car()
car_2 = Car()
car_3 = Car()
changeColor(car_1, "Lamborghini")
changeColor(car_2, "Ferrari")
changeColor(car_3, "McLaren")

bike_1 = motorCycle()
bike_2 = motorCycle()
bike_3 = motorCycle()
changeColor(bike_1, "Duccati")
changeColor(bike_2, "Hayabusa")
changeColor(bike_3, "Himalayan Bullet")

print("Car Details: ")
print(car_1.name)
print(car_2.name)
print(car_3.name)
print("Bike Details: ")
print(bike_1.name)
print(bike_2.name)
print(bike_3.name)

"""
Output:

"""