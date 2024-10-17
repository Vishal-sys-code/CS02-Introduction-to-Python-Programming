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