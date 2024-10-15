# String Format 
Optional method that gives users more control when displaying output.

```py
animal = "Elephant"
item = "Jupiter"
print("The " + animal + " jumped over the " + item)

print("The {} jumped over the {}".format("Doraemon", "Rat"))
print("The {} jumped over the {}".format(animal, item))

# positional argument
print("The {0} jumped over the {1}".format(animal, item))

# keyword argument
print("The {animal} jumped over the {item}".format(animal = "Doraemon", item = "Rat"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

###########################################################

name = "Vayishu"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you". format(name))
print("Hello, my name is {:<10}. Nice to meet you". format(name))
print("Hello, my name is {:>10}. Nice to meet you". format(name))
print("Hello, my name is {:^10}. Nice to meet you". format(name))

###########################################################

number = 3.14159
print("The number PI is: {}". format(number))
print("The number PI is: {:.3f}". format(number))

###########################################################

number1 = 1000
print("The number is: {:,}".format(number1))
print("The number is: {:b}".format(number1))
print("The number is: {:x}".format(number1))
print("The number is: {:o}".format(number1))

"""
Output:
The Elephant jumped over the Jupiter
The Doraemon jumped over the Rat
The Elephant jumped over the Jupiter
The Elephant jumped over the Jupiter
The Doraemon jumped over the Rat
The Elephant jumped over the Jupiter
Hello, my name is Vayishu
Hello, my name is Vayishu   . Nice to meet you
Hello, my name is Vayishu   . Nice to meet you
Hello, my name is    Vayishu. Nice to meet you
Hello, my name is  Vayishu  . Nice to meet you
The number PI is: 3.14159
The number PI is: 3.142
The number is: 1,000
The number is: 1111101000
The number is: 3e8
The number is: 1750
"""
```