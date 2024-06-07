"""
while 1 == 1:
    print("I am stuck in a loop")
"""

name = ""
while len(name) == 0:
    name = input()
print("Hello " + name)

# If we write the name then it will exit the loop 

name_1 = None
while not name_1:
    name_1 = input()
print("Hello " + name)