# **Objects**
The object is an entity that has a state and behavior associated with it. It may be any real world entity like: mouse, keyboard, pen, table, chair, etc.

**Object consist of:**
- **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
- **Behavior:** It is represented by the methods of an object. It also reflect the response of an object to other objects.
- **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

To understand the state, behavior and identity let us take the example of the dog:-
* The identity can be considered as the name of the dog
* State or Attributes can be considered as the breed, age or color of the dog.
* The behavior can be considered as the whether the dog is eating or sleeping.

**Creating an object:**
`obj = Dog()`

## **Python Self**
- Class methods must have an extra parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
- If we have a method that takes no argument, then we will still have to have one argument.
- This is similar to this pointer in C++, and this reference in Java.

**Use of `self` :**
When working with the classes in python, the term `self` refers to the instance of the class that is currently being used. It is customary to use "self" as the first parameter in instance methods of a class. Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the `self` parameter. This enables you to modify the objects properties and executes takes unique to that particular instance.

Example:
```py
class myNumber:
    def __init__(self, value):
        self.value = value
    def printValue(self):
        print(self.value)

obj1 = myNumber(30)
obj1.printValue()

"""
Output:
30
"""
```
**Self Parameter**
When we call a method of this object as `myObject.method(arg1, arg2)`, this is automatically converted by python into `myClass.method(myObject, arg1, arg2)` - this is all the special self is about.
```py
class cambridgeCSLectures:
    def __init__(self, name, lecturer, course, year, semester):
        self.name = name
        self.lecturer = lecturer
        self.course = course
        self.year = year
        self.semester = semester
    def displayDetails(self):
        print("Hello, My name is " + self.name + " as a " + self.lecturer + " lecturer of " + self.course + " of " + self.year + " of " + self.semester + " semester ")

obj = cambridgeCSLectures("Vayishu", "Computer Science", "Introduction to Python Programming", "2024", "2nd")
obj.displayDetails()

"""
Output:
Hello, My name is Vayishu as a Computer Science lecturer of Introduction to Python Programming of 2024 of 2nd semester
"""
```
The self parameter doesn't call it to be self, you can use any other name instead of it.
* `__init__()` method: This method is called constructors. it is as similar as the C++ and Java constructors. Constructors are used to initializing the objects state. Like methods, a constructor also contains a collections of statements that are executed at the time of the object creation. It runs as soon as the object of a class is instantiated.
* self is not considered as a keyword in python. Self is just a parameter name used in instance methods to refer to the instance itself.

=> The `__init__` method is similar to constructor in CPP and Java. It is run as soon as the object os a class is instantiated. The method is useful to do any initialization you want to do with your object.

## **Class and instance variable or attribute**
* Instance variable are for data, unique to each instance and class variable are for attributes and methods shared by all instances of the class. 
* *Instance variable are variable whose value is assigned inside a constructor* or *method with self* where as *class variable are variable whose value is assigned in the class*.
* *instance variable = variable inside the constructor*

```py
class Dog:
    animal = 'dog' # class variable
    def __init__(self, name, breed): # init method or constructor
        self.name = name # instance variable 1
        self.breed = breed # instance variable 2
    def setColor(self, color):
        self.color = color # instance variable 3
    def getDetails(self):
        print("I have my pet and his name is " + self.name + " and he belongs to the breed of " + self.breed) # Retrieves an instance variable 1 and 2
    def getColor(self):
        return self.color # Retrieves an instance variable 3

petDog = Dog("Jimmy", "Pug")
petDog.setColor("White")
petDog.getDetails()
color = petDog.getColor()
print("Color: ", color)

"""
Output:
I have my pet and his name is Jimmy and he belongs to the breed of Pug
Color:  White
"""
```

**Define a class in Python?**
To define a class in python, use the class keyboard foloowed by the class name and a colon.

```py
class myClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def someMethod(self):
        # Method definitions
        pass
```