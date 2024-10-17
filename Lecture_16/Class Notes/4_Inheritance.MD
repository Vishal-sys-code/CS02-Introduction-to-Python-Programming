# **Inheritance**
It is the mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.

## **Benefits of Inheritance**
* It represent real world relationship well
* It provides the reusability of a code. We don't have have to write the same code again and again. Also, it aloows us to add more features to a class without modifying it.
* Inheritance offers simple, understandable model structure.
* It is transitive in nature, which means that is class B inherits from another class A, then all the subclasses B would automatically inherit from class A.

## **Syntax**

```py
class BaseClass:
    {Body}
class DerivedClass(BaseClass):
    {Body}
```

**Example:**
```py
class Person(object):
    # Constructor
    def __init__(self, name, age):
        self.age = age
        self.name = name
    # To get name
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def isEmployeed(self):
        return False
        
class Employee(Person):
    def isEmployee(self):
        return True
# An object of a Person
emp = Person("Gorilla", 100)
print("Object of Person: ")
print(emp.getName())
print(emp.getAge())
print(emp.isEmployeed())
# An object of a Employee
emp = Employee("Dinosaur", 66502)
print("Object of Employee: ")
print(emp.getName())
print(emp.getAge())
print(emp.isEmployee())

"""
Output:
Object of Person: 
Gorilla
100
False
Object of Employee: 
Dinosaur
66502
True
"""
```

* `super()` function is a built-in function that returns the objects that represented the parent class. It allows to access the parent class methods and attributes in the child class.

## **Different types of Inheritance**
* **Single Inheritance :** When a child class inherits from ***only one parent class***, it is called Single Inheritance. [Example is above]
* **Multiple Inheritance :** When a child class inherits from ***multiple parent classes***, it is called Multiple Inheritance.
* **Multilevel Inheritance :** When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
* **Hierarchial Inheritance :** More than one derived class can be created from a single base.
* **Hybrid Inheritance :** This forms combines more than one form if inheritance. Basically, it is a blend of more than one type of inheritance.

## **Single Inheritance**

```py
# Base class
class Animal:
    def speak(self):
        return "The animal makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return "The dog barks."

# Create an instance of the Dog class
my_dog = Dog()

# Call the speak method
print(my_dog.speak())  # Output: The dog barks.
```

## **Multiple Inheritance**
```py
# When a child class inherits from multiple parent classes, it is called Multiple Inheritance.

class Base1(object):
    # constructors
    def __init__(self):
        self.str1 = "USA"
        print("Base1 Class")
class Base2(object):
    # constructors
    def __init__(self):
        self.str2 = "Germany"
        print("Base2 Class")
class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of base classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived Class")
    def printStr(self):
        print("Countries:", self.str1, "", self.str2)
obj = Derived()
obj.printStr()

"""
Output:
Base1 Class
Base2 Class
Derived Class
Countries: USA  Germany
"""
```
## **Multilevel Inheritance**
```py
# When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
class Base(object):
    # constructor
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age
    def getAge(self):
        self.age = age

class grandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self,name,age)
        self.address = address
    def getAddress(self):
        return self.address
objGrandChild = grandChild("Richard", 23, "Boston")
print("Name:", objGrandChild.name)
print("Age:", objGrandChild.age)
print("Address:", objGrandChild.address)

"""
Output:
Name: Richard
Age: 23
Address: Boston 
"""
```

## **Hierarchial Inheritance**

```py
# Base class
class Animal:
    def speak(self):
        return "The animal makes a sound."

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "The dog barks."

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "The cat meows."

# Derived class 3
class Cow(Animal):
    def speak(self):
        return "The cow moos."

# Create instances of the derived classes
my_dog = Dog()
my_cat = Cat()
my_cow = Cow()

# Call the speak method for each instance
print(my_dog.speak())  # Output: The dog barks.
print(my_cat.speak())  # Output: The cat meows.
print(my_cow.speak())  # Output: The cow moos.
```

## **Hybrid Inheritance**

```py
# Base class
class Animal:
    def speak(self):
        return "The animal makes a sound."

# Derived class 1
class Dog(Animal):
    def speak(self):
        return "The dog barks."

# Derived class 2
class Cat(Animal):
    def speak(self):
        return "The cat meows."

# Derived class 3 (inherits from Dog and Cat)
class HybridAnimal(Dog, Cat):
    def hybrid_speak(self):
        return f"{self.speak()} and {Cat.speak(self)}"

# Create an instance of the HybridAnimal class
my_hybrid = HybridAnimal()

# Call the methods
print(my_hybrid.hybrid_speak())  # Output: The dog barks. and The cat meows.
```


## **Method Chaining**
Calling multiple methods automatically each call performs an actions on the same object and returns self.
```py
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
```

## `super()` Functions
Function used to give access to the method of a parent class. Returns a temporary object of a parent class when used.

### **Code without the super function:**

```py
class Rectangle:
    pass
class Square(Rectangle):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Cube(Rectangle):
    def __init__(self,length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        return self.length * self.width * self.width
square_obj = Square(3,3)
cube_obj = Cube(3,3,3)
a = square_obj.area()
b = cube_obj.volume()
print(a)
print(b)

"""
Output:
9 
27
"""
```
### **Code with the super function:**

```py
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.width

square_obj = Square(3,3)
cube_obj = Cube(3,3,3)
a = square_obj.area()
b = cube_obj.volume()
print(a)
print(b)

"""
Output:
9 
27
"""
```