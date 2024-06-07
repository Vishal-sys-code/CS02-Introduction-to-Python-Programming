print("------- A for loop that prints in the range of 10 -------")
for i in range(10):
    print(i+1)

print("------- A for loop that prints in the range of the 50 to 100 -------")
for i in range (50, 100):
    print(i)

print("------- A for loop that iterates the string and display the message on the given condition -------")
for i in "Gigi Hadid":
    print(i)

print("------- A for loop that iterates from 50 to 101 and the jump is 2 and display the desired results -------")
for i in range (50, 100+1, 2):
    print(i)

print("------- A for loop that display the message on the time delay by importing the desired time package -------")
import time
for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Konichiwa")

print("------- Iteration of the Data Structures -------")

print("------- List Iteration -------")
list = ["Lana", "Del", "Ray"]
for i in list:
    print(i)

print("------- Tuple Iteration -------")
tuple = ("Lana", "Del", "Ray")
for i in tuple:
    print(i)

print("------- String Iteration -------")
str = "Lana Del Ray"
for i in str:
    print(i)

print("------- Dictionary Iteration -------")
d = dict()
d['abc'] = 123
d['xyz'] = 456
for i in d:
    print("%s %d" % (i, d[i]))

print("------- Set Iteration -------")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)