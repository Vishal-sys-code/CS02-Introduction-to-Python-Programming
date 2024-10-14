# **Exception Handling**
Events detected during execution that interrupt the flow of the program.

# **Different types of Exception in Python**
There are several built-in exceptions that can be raised when an error occurs during the execution of a program.
* **`SyntaxError` :** This exception is raised when the interpreter encounters a syntax error in the code, such as misspelled keyword, a missing colon, or an unbalanced paranthesis.
* **`TypeError` :** This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
* **`NameError` :** This exception is raised when a variable or function name is not found in the current scope.
* **`IndexError` :** This exception is raised when an index is out of range for a list, tuple or other sequence types.
* **`KeyError` :** This exception is raised when a key is not found in a dictionary.
* **`ValueError` :** This exception is raised when a function or method is called with in an invalid argument or valid.
* **`AttributeError` :** This exception is raised when an attribute or method is not found on an object, such as tring to access a non-existence attribute of a class instance.
* **`IOError` :** This exception is raised when an I/O operation such as: reading, writing fails due to an input/output error.
* **`ZeroDivisionError` :** This exception is raised when an attempt is made to divide a number by zero.
* **`ImportError` :** This exception is raised when an inport statement fails to find or loads a module.

# **Try-Except Statements**
Try-expect statements are used to catch and handle exceptions in python. Statements that can raise exceptions are kept inside the try clause and the statements that can handle the exceptions are written inside the except clause.

Error in python can be of two types i.e. syntax errors and exceptions. Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal event occurs which changes the normal flow of the programs.

**Some Common exception errors are:**
* I/O Error: If the file can't be opened
* Keyboard interrupt: When an unrequired key is pressed by the user.
* ValueError: When the builtin function receives a wrong argument
* EOF Error: If End-of-File is hit without reading any data
* ImportError: If it is unable to find the module.

```py

try: 
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result: ", result)

# except Exception:
#     print("Something went wrong!!!")

except ZeroDivisionError:
    print("You cannot divide by 0")

except ValueError:
    print("Enter only number please")

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by 0")

# we can also add the else statement
else:
    print(result)
finally:
    print("This statement will always being executed")

"""
Output: 
Enter the numerator: 10
Enter the denominator: a
Enter only number please
This statement will always being executed
"""
```

# **Try with else Statements**
The code defines a function AbyB(a,b) that calculates variable c as the ((a+b)/(a-b)) and handles a potential ZeroDivisionError. It prints the results if no division by zero error. Calling AbyB(2.0,3.0) calculates and prints -5.0, while calling AbyB(3.0,3.0) attempts to divide by zero, resulting in a ZeroDivisionError, which is caught and "a/b results in 0" is printed.

```py
def AbyB(a,b):
    try:
        c = ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b cannot be divided to each other")
    else:
        print(c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)

"""
Output:
-5.0
a/b cannot be divided to each other
"""
```

# Finally Keyword
Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after the normal termination of the try block or adter the try block terminated due to the exception.

Syntax:-

```bash
try:
    # some code
except:
    # optional block
    # handling the exception(if required)
else:
    # execute if no exception
finally:
    # Some code .... (always executed)
```

The previous code attempts to perform integer division by zero, resulting in a ZeroDivisionError. It catches the exception and prints. "Can't divide by zero". Regardless of the exception, the finally block is executed and prints "This is always executed".

```py
try:
    k = 5//10
    print(k)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
finally:
    print("This is walys executed")

"""
Output: 
0
This is always executed
"""
```

# Raising Exceptions
The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. This may be either exception class or exception instance.

```py
try:
    raise NameError("Hi there!!!")
except NameError:
    print("An error occurred!!!")
    raise

"""
Output: 
py", line 2, in <module>
    raise NameError("Hi there!!!")
NameError: Hi there!!!
"""
```

The output of this will simply printed as "An exception" but a Runtime error will also occur in the laste due to raise statement in the last line. So, the output on your command line will look like the above written in curly braces.

**Advantages of Exception Handling**
* Improve program reliability
* Simplified error handling
* Cleaner code
* Easier debugging

**Disdvantages of Exception Handling**
* Performance Overhead
* Increased Code Complexity
* Possible security risks