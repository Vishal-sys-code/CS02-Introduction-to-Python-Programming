# Duck Typing
It is the concept where the class of an object is less important than the methods/attributes class type is not checked in minimum methods/attributes are present.

"If it walks like a duck and it quacks like a duck then it must be a duck".

```py
class Duck:
    def walk(self):
        print("Duck is walking")
    def talk(self):
        print("Duck is quackng")
class Person:
    def catch(self, Duck):
        Duck.walk()
        Duck.talk()
        print("You catch me")
class Chicken:
    def walk(self):
        print("The chicken is walking")
    def talk(self):
        print("The chicken is talking")

duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
person.catch(chicken)

"""
Output:
Duck is walking
Duck is quackng
You catch me
The chicken is walking
The chicken is talking
You catch me
"""
```