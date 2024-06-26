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