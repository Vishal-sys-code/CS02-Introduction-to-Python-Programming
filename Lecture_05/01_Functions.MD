# **Functions**
Functions are the block of statements that return the specific task. 

## **Benefits of Using**
* Increase Code Readability
* Increase Code Reusability

**Snippet:**
```py
def function_name(parameters):
    return expression
```
## **Types of Functions**
* **Built-in library function :** These are standard deviation in python that are available to use.
* **User-defined function :** We can create our own functions based on our requirements.

## **Creating a functions**
```py
def func():
    print("Batman")
```

## **Calling a Function**
```py
def func():
    print("Batman")
func()
```

## **Python function with parameters**

**Snippet:**
```py
def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
```
**Example :**
```py
def add(num1: int, num2:int) -> int:
    """Adding the two integers"""
    num3 = num1+num2
    return num3

num1, num2 = 5,10
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
```

## **Python function Arguments**
```py
def evenOdd(x):
    if x%2 == 0:
        print("Even")
    else:
        print("Odd")

evenOdd(2)
evenOdd(3)
```

## **Types of Arguments**

* **Default Arguments :** A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
* **Keyword Arguments :** They are values that, when passed into a function are identified by specific parameter names.
* **Positional Arguments :** It is an argument that is passed to a function based on it's position in the argument list.
* **Arbitrary Keyword Arguments :** It can pass a variable number of arguments to a function using special symbols. There are two special symbols: `*args`, `**kwargs`.