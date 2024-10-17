# **Walrus Operator**
it is new to pyhton 3.8. It is also known assignment expression aka walrus operator. It assign values to variables as part of a larger expressions.

Walrus Operator looks like:  :=

**Example 1:**

```py
happy = True
print(happy)
```
Applying walrus operator to Example 1: 

```py
print(happy := True)
```

**Example 2:**

```py
food = list()
while True:
    food = input("What food you like: ")
    if food == 'quit':
        break
    food.append(food)
```

Applying walrus operator at Example 2:

```py
food = list
while food := input("What food do you like?: ") != 'quit':
    food.append(food)
```