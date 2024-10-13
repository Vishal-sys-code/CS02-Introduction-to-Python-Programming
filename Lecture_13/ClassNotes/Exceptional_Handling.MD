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

Some Common 