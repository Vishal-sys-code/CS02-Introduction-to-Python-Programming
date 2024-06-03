# **Variables**
Variables are the containers that stores the values. Python is not "statically-typed". It is the basic unit of storage in a program.

## **Variable Name Rules**
* Must start with a letter or underscore
* Case Sensitive
* Must consist of letters, numbers or underscores

**Good:** spam, eggs, spam23, _speed
**Bad:** 23spam, #sign, var.12
**Different:** spam, Spam, SPAM

Example:
```py
name = "tmleyncodes"
print(name)
```

### Sentences or Lines
```py 
x = 2 # Assign Statement
x = x + 2 # Assign with expession
print(x) # Print Statement
```

**NOTES:**
* The value stored in a variable can be changed during program execution.
* A Variables in Python is only a name given to a memory location, all the operations done on the variable effects that memory location.

**Valid Variable Name:**
```py
geeks = 1
print(geeks)

Geeks = 2
print(Geeks)

Ge_e_ks = 5
print(Ge_e_ks)

_geeks = 6
print(_geeks)

geeks_ = 7
print(geeks_)

_GEEKS_ = 8
print(_GEEKS_)
```

## Assigning the Variables

```py
# A Integer Variable
age = 45
# A Floating Variable
salary = 10000.79
# A String Variable
name = "John"

# Declaring a Variable
num = 100

# Re-declaring a variable
num = 101

# Multi-Assignments
a = b = c = 10

age, salary, name = 45, 10000.79, "John"
```