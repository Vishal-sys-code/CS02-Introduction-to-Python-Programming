# **For Loops**
A statement that will execute its block of a code a limited amount of times.

* **While Loop:** `Unlimited`
* **For Loop:** `Limited`

For loop helps to iterate or traverse the data structures: `arrays`, `string`, `tuples`, etc.

**Snippets :**

```py
for iterator_var in sequence:
    statements(s)
```

**Examples :**

```py
print("------- A for loop that prints in the range of 10 -------")
for i in range(10):
    print(i+1)

print("------- A for loop that prints in the range of the 50 to 100 -------")
for i in range (50, 100):
    print(i)

print("------- A for loop that iterates the string and display the message on the given condition -------")
for i in "Gigi Hadid":
    print(i)

print("------- A for loop that iterates from 50 to 101 and the jump is 2 and display the desired results -------")
for i in range (50, 100+1, 2):
    print(i)

print("------- A for loop that display the message on the time delay by importing the desired time package -------")
import time
for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Konichiwa")
```