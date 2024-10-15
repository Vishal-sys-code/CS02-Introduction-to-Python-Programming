from car import Car
car_1 = Car("Lamborghini", "L-1", 2023, "Black")
car_2 = Car("Ferrari", "L-2", 2023, "Red")
car_1.wheels = 2
print(car_1.wheels) # 2
print(car_2.wheels) # 4
print(Car.wheels) # 4
Car.wheels = 2
print(car_1.wheels) # 2 
print(car_2.wheels) # 2