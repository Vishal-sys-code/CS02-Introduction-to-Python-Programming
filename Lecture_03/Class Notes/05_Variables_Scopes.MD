# Variable Scope
In python the scope of a variable determines the portion of the program where the variable is accessible. Understanding variable scope is crucial for writing robust and error free code.
Python primariliy uses four scopes: **Local**, **Enclosing** , **Global** and **Built-in** [LEGB]

## **Local Scope**
A variable declared inside a function is in the local scope and can only be accessed within that function.

```py
def myFunction():
    x = 10 # local variable
    print(x) 
myFunction() # Output: 10
print(x) # NameError: name 'x' is not defined
```

## **Enclosing Scope**
It refers to the scope of any enclosing functions, such as when functions are nested.

```py
def outerFunction():
    x = 20 # enclosing variable
    def innerFunction():
        print(x) # Accessing enclosing variable
    innerFunction()
outerFunction() # Output: 20
```

## **Global Scope**
A variable declared at the top level of a module or script is in the global scope. It can be accessed from any function within the same module.
```py
x = 30 # Global Variable
def myFunction(): # Accessing Global Variable
    print(x)
myFunction() # Output: 30
```


## **Built-in Scope**
Built in scope contains names that are predefined in Python. These are accessible from any part of the code.

```py
print(len("Hello")) # len is a built-in function
```