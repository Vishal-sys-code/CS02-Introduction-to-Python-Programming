# **Object as an Argument**
You can pass objects as arguments to functions or methods. This allows you to manipulate and use the properties and methods of those objects within the function. Here's an explanation along with an example to illustrate how this works.

**Explanation :**
- **Object Creation**: You create an instance of a class (an object).
- **Function Definition**: You define a function that takes an object as a parameter.
- **Accessing Object Attributes and Methods**: Inside the function, you can access the object's attributes and call its methods.

**Example 1: Passing an Object to a Function**
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Function that takes a Person object as an argument
def introduce_person(person):
    print(f"Introducing a new person:")
    person.greet()

# Creating a Person object
john = Person("John", 30)

# Passing the Person object to the function
introduce_person(john)

"""
Output:
Introducing a new person:
Hello, my name is John and I am 30 years old.
"""
```

**Example 2: Modifying an Object Inside a Function**

```py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Function that modifies the Dog object
def change_dog_name(dog, new_name):
    dog.name = new_name

# Creating a Dog object
my_dog = Dog("Rex", "German Shepherd")

# Changing the dog's name by passing the object to the function
change_dog_name(my_dog, "Max")

# Checking the modified name
print(my_dog.name)  # Output: Max


"""
Output:
Max
"""
```
