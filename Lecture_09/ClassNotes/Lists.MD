# **Lists**
Lists are just dynamically sized arrays, declared in other languages (vector in C++, ArrayList in java)

List are the collection of things, which are enclosed by `[]` and seperated by the commas.

List is a sequential datatype which is used to store the collection of data. Lists are mutable.

**Example:**
```py
var = ["Geeks", "for", "Geeks"]
print(var)
```

List are simple containers that are an intefral part of the python. A single list may contain datatypes like: Integers, Strings, as well as objects. List are mutable and hence they can be altered even after their creation.

**Example 1 : Creating a basic list**
```py
list = []
print("Blank List: ")
print(list)

list = [10, 11, 12]
print("List Containing Numbers: ")
print(list)

print("Stanford", "University")
print("List Containing Strings: ")
print(list)
```

The complexities of the above code are: 
* Time Complexity: `O(1)`
* Space Complexity: `O(N)`


**Example 2: Creating a List with distinct or duplicate elements**
A list can contain duplicate values with their distinct positions and hence multiple distinct or duplicate values can be passes as a sequence at the time of list creation.

```py
list = [1,2,2,3,3,3,4,5,6,6,7,8,9,9,10,10]
print("List containing duplicate value: ")
print(list)

list = [3,4,"Stanford",2,0,1,"University"]
print("List containing mixed values: ")
print(list)

# To get the access of the list
print("\nAccessing the Lists: ")
print(list[0])
print(list[1])

# Negative Indexing
print("\nDisplaying the Negative Indexing: ")
print(list[-1])
print(list[-3])

# Getting size of list
print("\nDisplaying the Length of the List: ")
print(len(list))
```

**Example 3: Taking an input from the user in list**
```py
# Example - 1 
string = input("Enter Elements: ")
list = string.split()
print("List is: ", list)

# Example - 2
n = int(input("Enter the size of the list: "))
lst = list(map(int,input("Enter the integer elements: ").strip().split()))[:n]
print("List is: ", lst)

# Example - 3
lst = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    element = int(input())
    lst.append(element)
print(lst)

# Example - 4
lst = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    element = [input(), int(input())]
    lst.append(element)
print(lst)
```

## **Adding Elements to a Python List**

There are two in-built functions through which we can insert the elements at the end of the list, the functions are:- `append()` and `extend()`

* **Using the built-in function append()**
```py
list = []
list.append(1)
list.append(2)
list.append(3)
for i in range(1,4):
    list.append(i)

list2 = ["Fydor", "Dostoevsky"]
list.append(list2) # Adding list in a list
```
* **Using the built-in function insert()**
```py
# Using the built-in function insert()
list = [1,2,3,4]
print(list)
list.insert(3,12)
list.insert(0,"State")
print(list)
```

The `append()` method addes up the element in the end of the list, where as the `insert()` method adds up the element at the any position of the list or adds the element at the desired position of the list.


Now we have another method which is: `extend()` it is the same as the `append()` method.

```py
list = []
list1 = [1,2,3,4]
list1.extend("Genie")
print(list1)
```

* **Output:** `[1,2,3,4,"Genie"]`
* **Time Complexity**: `O(N)`
* **Space Complexity**: `O(1)`

## **Reversing the List**

**Example 1: Using reverse() method**

```py
mylist = [1,2,3,4,5,'Meta', 'Microsoft']
mylist.reverse()
print(mylist)
```

**Example 2: Using reversed() functions**
The `reversed()` function returns a reverse iterator, which can be converted to a lost using the `list()` function.
```py

```