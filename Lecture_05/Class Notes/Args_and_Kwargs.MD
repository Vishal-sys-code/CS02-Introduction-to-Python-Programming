# ***args [Non-Keyword Arguments]**
The special syntax `*args` in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyword, variable length argument list.

* Parameter that will pack all the argument into a tuple. It is useful so that a function can accept a varing amount of arguments.

**NOTE :** The syntax is to use the symbol `*` to take in a variable number of arguments, by convention it is often used with the word args.

**Example:**
```py
def add(num1, num2):
    sum = num1+num2
    return sum
print(add(1,2)) #3
print(add(1,2,3)) #Error
```

The above code-snippet will give an error of: `TypeError: add() takes 2 positional arguments but 3 were given.` So, to avoid these errors we fix it by using the `*args`.

```py
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(add(1,2,3,4,5,6,7,8,9,10))
```

**NOTE :** Here in the above code we can change the name of the argument which is *args to anything like your name too: *annie or *jack too... 

<hr>

