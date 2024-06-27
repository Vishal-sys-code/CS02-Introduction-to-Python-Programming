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

```