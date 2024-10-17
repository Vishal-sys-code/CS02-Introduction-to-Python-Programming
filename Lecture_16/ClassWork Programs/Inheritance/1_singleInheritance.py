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