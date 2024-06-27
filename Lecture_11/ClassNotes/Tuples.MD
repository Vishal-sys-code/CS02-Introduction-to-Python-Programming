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