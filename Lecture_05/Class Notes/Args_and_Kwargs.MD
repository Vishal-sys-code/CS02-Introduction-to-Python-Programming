# **`*args [Non-Keyword Arguments]`**
The special syntax `*args` in function definitions in Python is used to pass a variable number of arguments to a function. It is used to pass a non-keyword, variable length argument list.

* Parameter that will pack all the argument into a **tuple**. It is useful so that a function can accept a varing amount of arguments.

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

# **`**kwargs [Keyword Arguments]`**

The special syntax `**kwargs` in function definitions in Python is used to pass a keyworded, variable-length argument list. The reason of double start allows us to pass through keyword arguments (and any number of them).

* Parameter that will pack all the arguments into a dictionary useful so that a function can accepts a varying amount of keyword argument.

**Example:**
```py
def hello(first, last):
    print("Hello" + first + " " + last)
print(hello(first = "Jack", last = "Williams"))
print(hello(first = "Opera", middle = "Henry", last = "Kushgoterava"))
```
Here in the above code snippet of the hello function, there will be an error of the function which contains the three parameters. The error will be: 
`TypeError: hello() get an expected keyword argument 'middle'`

To avoid these type of errors in the positional argument type we can fix it by using the `**kwargs`.

```py
def hello(**kwargs):
    #print("Hello" + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end="")
    for key.value in kwargs.items():
        print(value)

print(hello(first = "Opera", middle = "Henry", last = "Kushgoterava"))
```