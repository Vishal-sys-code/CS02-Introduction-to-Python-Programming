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