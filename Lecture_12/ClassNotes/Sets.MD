# **Set in Python**
It is an unordered collection datatype that is iterable, mutable and has no duplicate elements.
Set is represented by : `{}` [values are enclosed in this curly braces].
Set is mutable, which means it can be changed after it is created.
The major advantage of using a set, as opossed to a list is that it has a highly optimized method for checking whether a specific element is contained in the set.
This is based on a data structure known as Hash Tables. [We will know deeply in our Algorithms Lecture].
Since, sets are unordered, we cannot access items using indexes as we do in lists.

```py
var = {"Geeks", "know", "nerds"}
print(var)
print(type(var))

"""
Output:
{'Geeks', 'know', 'nerds'}
<class 'set'>
"""
```

## **Type Casting with Python Set Method**
* `set()` method is used for the type casting.

```py
# typecasting list to set
myList = ["a", "b", "c"]
print("Before typecasting from List to Set: ")
print(myList)
mySet = set(myList)
print("After typecasting from List to Set: ")
print(mySet)
# Adding element to the set
mySet.add("d")
print("After Adding an element to the Set: ")
print(mySet)

"""
Output:
Before typecasting from List to Set: 
['a', 'b', 'c']
After typecasting from List to Set:
{'b', 'c', 'a'}
After Adding an element to the Set:
{'d', 'b', 'c', 'a'}
"""
```
Python set is an unordered datatype, which means we cannot know in which order the elements of the set are sorted.
* Time Complexity: `O(N)`
* Space Complexity: `O(N)` 

## Check Unique and Immutable with in Set
Python set cannot have a duplicate value and once it is created we cannot change its value.

```py
# A set cannot have duplicate values
# and we cannot change its value
mySet = {"William", "Henry", "Gates", "Phoebe", "Gates"}
print("Set Created and looks like: ")
print(mySet)
# Values of a set cannot be changed
mySet[1] = "Helwett"
print(mySet)

"""
Output:
Set Created and looks like: 
{'Henry', 'William', 'Gates', 'Phoebe'}
Traceback (most recent call last):
  File "\Lectures\CS02-Introduction-to-Python-Programming\main.py", line 7, in <module>
    mySet[1] = "Helwett"
TypeError: 'set' object does not support item assignment
"""
```

* The first code explains that the set cannot have a duplicate value. Every item in it is a unique value.
* The second part of the code generates an error because we cannot assign or change a value once the set is created. We can only add or delete items in the set.

## Heterogenous Element with Python Set
Python sets can store heterogenous element in it, i.e. a set can store a mixture of string, integer, boolean etc. datatypes.

```py
mySet = {"Cambridge", "University", 10, 9.54, True}
print(mySet)

"""
Output:
{True, 'Cambridge', 'University', 9.54, 10}
"""
```
A set can store the heterogenous element, which we saw above.
* Time Complexity: `O(N)`
* Space Complexity: `O(N)`

## **Python Frozen Sets**
Frozen Sets in python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. It can be done by `frozenset()` method while elements of the set can be modified at any time, elements of the drozen set remain the same after creation.
If no paramter passes then it will return as the empty frozen set.

```py
myFirstList = ["a", "b", "c"]
mySecondList = ["e", "f", "g"]
print("Normal Set: ")
normalSet = set(myFirstList)
print(normalSet)
frozen_set = frozenset(mySecondList)
print("Frozen Set: ")
print(frozen_set)

"""
Output:
Normal Set: 
{'b', 'a', 'c'}
Frozen Set:
frozenset({'g', 'e', 'f'})
"""
```
**Summary of Output :**
* **Normal Set:** Displays the elements of `myFirstList` as a set. The order is not guaranteed and can be different every time you run the code.
* **Frozen Set:** Similar to a normal set but immutable. The output shows the elements of `mySecondList` as a `frozenset`, also unordered.

## **Internal working of the set**
This is based on a data structure known as a hash table. If multiple values are present at the same index, then the value is appended to that index position, to form a linked list.
Sets are implemented using a dictionary with dummy variables, where key brings the members set with greater optimizations to the time complexity.

<!-- Add the diagram form the figma -->

## **Method of Sets**

### **Adding elements to the Python Sets**
Insertion in the set is done through the `set.add()` function. Where an appropriate record value is created to store in the hash tables. Same as checking for an item i.e. `O(1)` on average.
In worst case => `O(N)`

```py
# creating a set
people = {"Vishal", "Taylor", "Fredichie"}
print("People: ", end = "")
print(people)
people.add("Ananya")
for i in range(1,6):
    people.add(i)
print("\n Set after adding element: ", end = "")
print(people)

"""
Output:
People: {'Fredichie', 'Taylor', 'Vishal'}
Set after adding element: {1, 2, 3, 4, 5, 'Ananya', 'Vishal', 'Fredichie', 'Taylor'}
"""
```
**Complexities :**
* Time Complexity: `O(N)`
* Space Complexity: `O(N)`

### Union Operations
Two sets can be merged using `union()` function or `|` operator. Both Hash Table values are accessed and traversal with merge operation perform on them to combine the elements, at the same time duplicates are removed.
Time Complexity: `O(len(s1) + len(s2))`, where S1 and S2 are the two sets.

```py
people = {"Vishal", "Roger", "Richard"}
vampires = {"Sherine", "Madeline"}
dracula = {"Stephen", "Wood"}

# using union function
population = people.union(vampires)
print("Union using union() function: ")
print(population)

# using | operators
population = people | dracula
print("Union using | function: ")
print(population)

"""
Output:
Union using union() function: 
{'Vishal', 'Madeline', 'Richard', 'Roger', 'Sherine'}

Union using | function: 
{'Vishal', 'Richard', 'Roger', 'Stephen', 'Wood'}
"""
```

### Intersection of sets
This can be fone through the `intersection()` or `&` operator. Common elements are selected. They are similar to iteration over the Hash Lists and combining the same values on both the table.

Time Complexity: `O(min(len(s1), len(s2)))`, where s1 and s2 are two sets

```py
set1 = set()
set2 = set()
for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)
set3 = set1.intersection(set2)
print("Intersection using intersection() function: ")
print(set3)
set3 = set1 & set2
print("Intersection using & operator: ")
print(set3)

"""
Output:
Intersection using intersection() function: 
{3, 4}
Intersection using & operator:
{3, 4}
"""
```

**Complexities :**
* Time Complexity: `O(N)`
* Space Complexity: `O(N)`

### Finding differences of the sets
To find the differences between the sets is simlar to find the differences between the linked lists. This is done through the `difference()` function or the `-` operator.

Time Complexity: (s1 - s2) => `O(len(s1))` or `O(len(s2))` {depends on s2-s1 or s1-s2}

```py
set1 = set()
set2 = set()
for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)
set3 = set1.difference(set2)
print("Difference of two sets using the difference() method: ")
print(set3)
set3 = set1 - set2
print("Difference of two sets using '-' operator: ")
print(set3)

"""
Output:
Difference of two sets using the difference() method: 
{0, 1, 2}
Difference of two sets using '-' operator:
{0, 1, 2}
"""
```

**Complexities :**
* Time Complexity: `O(N)`
* Space Complexity: `O(N)`

### Clearing Python Sets

```py
set1 = {1,2,3,4,5,6,7,8}
print("Initial Set: ")
print(set1)
set1.clear()
print("Set after using clear() function")
print(set1)

"""
Output:
Initial Set: 
{1, 2, 3, 4, 5, 6, 7, 8}
Set after using clear() function
set()
"""
```
**Complexities :**
* Time Complexity: `O(N)` {where N is the number of elements in the set}
* Space Complexity: `O(1)` {constant space complexity as it doesn't depend on the}

However there are multiple two major pit falls in python sets:
* The set doesn't maintain elements in any particular order
* Only instances of immutable types can be added to a python set

## Operator for set
* `key in s`: containment check
* `key not in s`: non containment check
* `s1 == s2`: s1 is equivalent to s2
* `s1 != s2`: s1 is not equivalent to s2
* `s1 <= s2`: s1 is subset of s2
* `s1 < s2`: s1 is proper subset of s2
* `s1 >= s2`: s1 is super set of s2
* `s1 > s2`: s1 is proper subset of s2
* `s1 | s2`: The union of s1 and s2
* `s1 ^ s2`: The set of elements in precisely one of s1 or s2

| Operation                                    | Average Case                              | Worst Case                                    | Notes                                               |
| -------------------------------------------- | ----------------------------------------- | --------------------------------------------- | --------------------------------------------------- |
| **x in S**                                   | `O(1)`                                    | `O(N)`                                        |                                                     |
| **Union** `st`                              | `O(len(s) + len(t))`                     |                                               |                                                     |
| **Intersection** `s&t`                       | `O(min(len(s), len(t)))`                 | `O(len(s) * len(t))`                         | Replace `min` with `max` if `t` is not a set      |
| **Difference** `s-t`                         | `O(len(s))`                               |                                               |                                                     |
| **Multiple Intersection** `s1 & s2 & ... & sn` |                                           | `(n - 1) * O(l), where l is the max(len(s1), ..., len(sn))` |                                                     |
