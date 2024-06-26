# **Dictionary**
A dictionary is a data structure that stores the value in `key:value` pairs.

**Snippet of the dictionary is:**
`dict_var = {key1:value1, key2:value2, key3:value3, ...}`

**Example:**
```py
dict{
    1: 'python',
    2: 'java',
    3: 'cpp'
}
```

Dictionaries in python is a data structure used to store values in `key:value` format. This makes it different from list, tuples, and arrays as in a dictionary each key has an associated value.

As of Python 3.7, dictionaries are ordered and cannot contain duplicate keys.

Values in a dictionary can be of any datatype and can be duplicated, where as keys can't be repeated and must be immutable.

**Example 1: Dictionary with use of integer keys**

```py
dict = {
    1: "Apple", 
    2: "Microsoft",
    3: "Google"
}
```

**Example 2: Dictionary with use of multiple keys**

```py
dict = {
    "Name": "Vishal",
    "Number": [1,2,3],
    1: [1,2,3,4,5,6]
}
```

A dictionary can also be created by the built-in function `dict()`. An empty dictionary can be created by just placing curly braces.

```py
dict_2 = {}
print("Empty Dictionary")
print(dict_2)
dict_3 = dict({1:'Geeks', 2:'Nerds', 3:'Introverts'})
print("\n Dictionary with the use of the dict(): ")
print(dict_3)
dict_4 = dict([(1,'Geeks'), (2, 'Nerds'), (3, 'Introverts')])
print("\nDictionary with each item as a pair: ")
print(dict_4)
```

The complexities are:
* **Time Complexity:** `O(len(dict))`
* **Space Complexity:** `O(N)`

## **Nested Dictionaries**

```py
dict_1 = {1:'Geeks', 2:'For', 3:{'A':'Welcome', 'B':'To', 'C':'Introvert Club'}}
dict_2 = {
    1:'Geeks', 
    2:'For', 
    3:{
        'A':'Welcome', 
        'B':'To', 
        'C':'Introvert Club'
    }
}
dict_3 = {
    1:'Geeks',
    2:'Nerds',
    3:{
        'A':'Good',
        'B':'Morning',
        'C':'Stanford'
    }
}
print(dict_1)
print(dict_2)
print(dict_3)
```

## **Adding elements to a Dictionary**
The addition of elements can be done in multiple ways. One value at a time can be added to a dictionary by defining value along with the key.
**eg:** dict[key] = 'value'

Updating an existing value in a dictionary can be done by using the built-in `update()` method.

```py
dict = {}
print("Empty Dictionary")
print(dict)

dict[0] = 'Geeks'
dict[1] = 'Nerds'
dict[3] = 100

print("\n After adding 3 elements")
print(dict)

dict['value_set'] = 2,3,4
print("\n After adding 3 elements")
print(dict)

dict[2] = "Welcome"
print("\nUpdate key Value")
print(dict)

dict[5] = {'Nested':{1:'Life', 2:'Introverts'}}
print("\n Adding a Nested Key")
print(dict)
```

The complexities are:
* **Time Complexity:** `O(1)/O(N)`
* **Space Complexity:** `O(1)`

## **Accessing Element in Dictionary**

```py
dict = {
    1:'Geeks',
    'name': 'GH',
    3:'Hardy'
}

print("\nAccessing element using key")
print(dict['name'])
print("\nAccessing a element using key")
print(dict[1])
```

There is also a method called `get()` that will also help in accessing the element from a dictionary. This method accepts key as arguments and returns the value.

The complexities are:
* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

The `get()` method retrieves they key.

```py
# Using get() method

dict = {
    1: 'Andrew',
    2:'Huberman',
    3:'Podcasts'
}
print("\nAccessing element using key")
print(dict.get(2))
```

## **Accessing a Nested Dictionary**

```py
# Accessing a Nested Dictionary
dict = {
    'dict1':{
        1: 'Vishal'
    },
    'dict2':{
        'Name':'Stanford'
    }
}
print("\n----- Accessing element in Nested Dictionary -----")
print(dict['dict1'])
print(dict['dict1'][1])
print(dict['dict2']['Name'])
print(dict['dict2'][2])
```

## **Deleting elments using 'del' keyword**

```py
# Deleting elments using 'del' keyword
dict = {1:'Andrew', 2:'Huberman', 3: 'Podcasts'}
print("Initial Dictionary: ")
print(dict)
del(dict[1])
print("Displaying dictionary after deletion: ")
print(dict)
```

## Dictionary Methods

* `dict.clear()`: Removes all the elements from the dictionary.
* `dict.copy()`: Returns a copy of the dictionary.
* `dict.get(key,default="None")`: Returns the value of a specified key.
* `dict.items()`: Returns a list containing a tuple for each key value pair.
* `dict.keys()`: Returns a list containing dictionary keys.
* `dict.update(dict2)`: Update dictionary with specified key value pair.
* `dict.values()`: Returns a list of all the values of dictionary.
* `dict.pop()`: Remove the element with specified key.
* `dict.popitem()`: Remove the last inserted key-value pair.
* `dict.setdefault(key, default="None")`: Set the key to the default value if the key is not specified in the dictionary.
* `dict.haskey(key)`: Returns true if the dictionary contains the specified key.

## Multiple Dictionary Operations
We will demonstrate the several dictionary operations: clearing, accessing, retrieving key-value pair and keys, removing, updating.

```py
dict1 = {1:'Python', 2:'Java', 3:'Ruby', 4:'Scala'}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3:'Scala'})
print(dict2)
print(dict2.values())
```