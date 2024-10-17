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