# **Higher Order Functions**

A function that either:
* Accepts a function as an argument OR
* Returns a function 

In python functions are treated as an object.

**Example 1:**

```py
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(text):
    text = func("Hello")
    print(text)
hello(loud)
hello(quiet)
```

**Example 2:**
```py
def divisor(x):
    def dividend(y):
        return y/x;
divide = divisor(2)
print(divide(10)) # 5.0


"""
10/2 = 5

10 = dividend
2 = divisor
5 = quotient
"""
```