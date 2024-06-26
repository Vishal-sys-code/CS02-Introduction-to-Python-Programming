# **Tuples**
Tuples are the collections of objects that are seperated by commas.
Tuples are immutable.

**Tuple:** A collection which is ordered and unchangeable used to group together related data.

**Creating Tuples:**
* Using round brackets
* With One item
* Using Tuple Constructor

## Creating Tuple using Round Brackets

```py
# Creating Tuple using Round Brackets
var = ("Sachin", "Mahi", "Yuvraj")
print(var)
print(type(var))
```

## Creating Tuple with One Item
Python still provide us in the way to create a tuple.

**Syntax:**
```bash
values : tuple [int | str, ....] = (1,2,3,4,"Nerds",)
print(values)
```
In the above syntax, we are considering a variables called value which holds a tuple that consist of either int or str, the '....' means that the tuple will hold more than one int or str.

```py
# Creating a Tuple with one item
mytuple = ("Advertisement",)
print(type(mytuple)) #<class 'tuple'>
mytuple = ("Advertisement")
print(type(mytuple)) #<class 'str'>
```

## Creating Tuple using Tuple Constructor
To create a tuple with a tuple constructor, we will pass the elements as its parameter.

```py
tuple_constructor = tuple(("Data Structures", "Algorithms", "Development", "Machine Learning"))
print(tuple_constructor)
print(type(tuple_constructor))
```

**What is immutable type in Python tuples?**
Tuples are immutable and ordered and allow duplicate values. Some characteristics of tuples in python:
* Tuples cannot be appended or extended.
* We cannot remove items from a tuple once it is created.

```py
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[4])

my_tuple = (1,2,3,4,2,3)
print(my_tuple)
my_tuple[1] = 10000
print(my_tuple)
```

The output of the above syntax is:
```bash
(1, 2, 3, 4, 5)
2
5
(1, 2, 3, 4, 2, 3)
Traceback (most recent call last):
    line 8, in <module>
    my_tuple[1] = 10000
TypeError: 'tuple' object does not support item assignment
```

Hence, it is immutable or unchangeable.

**NOTE:** For accessing tuples, we have indexing

## Different types of Operations Related to Tuples
* Concatenation
* Nesting
* Repetition
* Slicing
* Deletion
* Finding the length
* Multiple datatypes with Tuples
* Conversion of list to tuples
* Tuples in a loop

```py
# CONCATENATION
tuple1 = (0,1,2,3)
tuple2 = ("Python", "Java")
print("------ Concatenation of Tuples: ------")
print(tuple1 + tuple2)

# ------------------------------------------------------------------------------------------------

# NESTING
# It means a tuple inside another tuple
tuple1 = (0,1,2,3)
tuple2 = ("Python", "Java")
tuple3 = (tuple1, tuple2)
print("\n------ Nesting of Tuples: ------")
print(tuple3)

# ------------------------------------------------------------------------------------------------

# REPETITION
# We can create a tuple of multiple same elements from a single element in that tuple
tuple1 = ("python",)*3
print("\n------ Repetition of Tuples: ------")
print(tuple1)

# ------------------------------------------------------------------------------------------------

# SLICING
# Dividing the tuples into small tuples using indexing methods
tuple1 = (0,1,2,3,4,5,6,7)
print("\n------ Slicing of Tuples: ------")
print(tuple1[0:3])
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# ------------------------------------------------------------------------------------------------

# DELETING
# Use 'del' keyword for deleting a tuple. The output will be in the form of error because after deleting the tuple it will give a NameError. 
tuple1 = (0,1,2,3,4,5,6,7)
del tuple1
print("\n------ Deleting of Tuples: ------")
# print(tuple1) # NameError: name 'tuple1' is not defined. Did you mean: 'tuple2'?

# ------------------------------------------------------------------------------------------------

# LENGTH OF THE TUPLE
tuple1 = (0,1,2,3,4,5,6,7)
print("\n------ Length of the Tuple: ------")
print(len(tuple1))
tuple2 = ('Java', 'C++')
print(len(tuple2))

# ------------------------------------------------------------------------------------------------

# CONVERTING LIST INTO TUPLES
# We can do this by using a tuple() constructor and passing the list as its parameter.
list1 = [0,1,2]
print("\n----- Converting List into the Tuples: ------")
print(tuple(list1))
print(tuple('python'))

# ------------------------------------------------------------------------------------------------

# MULTI-DATATYPES
tuple = ("immutable", True, 12)
print("\n----- Multi-Datatypes: ------")
print(tuple)

# ------------------------------------------------------------------------------------------------

# TUPLES IN A LOOP
# We can create a tuple with a single element in it using loops.

tuple = ("Python",)
n = 5
print("\n----- Tuples in a Loop -----")
for i in range(n):
    tup = (tuple,)
    print(tup)
```