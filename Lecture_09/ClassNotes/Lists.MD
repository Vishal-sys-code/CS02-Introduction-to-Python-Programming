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
mylist = [1,2,3,4,5]
reversed_list = list(reversed(mylist))
print(reversed_list)
```

## **Removing elements from the List**

**Method 1: Using remove() method**
Elements can be removed from the list by using the built-in function `remove()` function but an Error arises if the element doesn't exist in the list.

Remove() method only removes one element at a time, to remove a range of elements, the iterator is used. The `remove()` method removes the specified item.

**NOTE :** Remove method in List will only remove the first occurence of the searched element.

```py
print("------- Method 1: Using remove() method -------")
list = [1,2,3,4,5,6,7,8,9,10]
print("Initial List: ")
print(list)
list.remove(5)
list.remove(3)
print("\nList after removing two elements: ")
print(list)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Initial List: ")
print(list1)
for i in range(1,5):
    list1.remove(i)
print("\nList after removing two elements: ")
print(list1)
```
The complexities for deleting elements in a list using `remove()` method.
* **Time Complexity :** `O(N)`
* **Space Complexity :** `O(1)`

**Method 2: Using pop() method**
The `pop()` function can also be used to remove and return an element from the lost, but by defaults ***it removes the last element of the list***, to remove an element from a specific position of the list. 
The index is passed as an argument to the pop() method.

```py
print("------- Method 2: Using pop() method -------")
list2 = [1,2,3,4,5,6,7,8,9,10]
print("List before popping: ")
print(list2)
list2.pop()
print("\nList after popping: ")
print(list2)
```
The complexities for deleting elements in a list using `pop()` method.
* **Time Complexitiy :** `O(1)/O(N)` [`O(1)` for removing the last element, `O(N)` for removing the first and middle elements]
* **Space Complexity :** `O(1)`

## **Slicing of the List**
We can get the substrings and sublists using slice. There are multiple ways to print the whole list with all the elements, but a specific range of elements from the list we use the slice operation.

* To print elements from beginning to a range, use: `[:index]`
* To print elements from beginning to negative range, use: `[:-index]`
* To print elements from a specific index till the end, use: `[index: ]`
* To print elements from a specific negative index till the end, use: `[-index: ]`
* To print the whole list in reverse order, use: `[::-1]`

```py
list = ['M','A', 'C', 'H', 'I', 'N', 'E', 'L', 'E', 'A', 'R', 'N', 'I', 'N', 'G', 'A', 'T', 'C', 'O', 'L', 'L', 'E', 'G', 'E']
print("Initial List: ")
print(list)

sliced_list = list[3:8]
print("\nElements sliced from the range of the 3 to 8: ")
print(sliced_list)

sliced_list_1 = list[5:]
print("\nElements sliced from 5th element till the end: ")
print(sliced_list_1)

sliced_list_2 = list[:]
print("\nPrinting all the elements using slice operations: ")
print(sliced_list_2)

# NEGATIVE INDEXING
sliced_list_3 = list[:-6]
print("\nElements sliced from the beginning till the 6th element from the end: ")
print(sliced_list_3)

sliced_list_4 = list[-6 : -1]
print("\nElements sliced from the 6th element from the end till the 2nd last element: ")
print(sliced_list_4)

sliced_list_5 = list[::-1]
print("\nElements sliced in reverse order: ")
print(sliced_list_5)
```

## **List Methods**

| Function                  | Description                                                                                                        |
| -------                   | -------                                                                                                            |
| **append()**              | Add an element to the end of the list                                                                              |
| **extend()**              | Add all elements of a list to another list                                                                         |
| **insert()**              | Insert an item at the defined index                                                                                |
| **remove()**              | Removes an item from the list                                                                                      |
| **clear()**               | Removes all items from the list                                                                                    |
| **index()**               | Returns the index of the first matched item                                                                        |
| **count()**               | Returns the count of the number of items passed as an argument                                                     |
| **sort()**                | Sort items in a list in ascending order                                                                            |
| **reverse()**             | Reverse the order of items in the list                                                                             |
| **copy()**                | Returns a copy of the list                                                                                         |
| **pop()**                 | Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.|

## **FAQs**

Lists are used in Python to store collections of items, such as numbers, strings, or other objects. They are commonly used for:
* Storing and manipulating sequences of data.
* Aggregating items to iterate over them.
* Collecting multiple items as a single variable.
* Data manipulation and analysis.