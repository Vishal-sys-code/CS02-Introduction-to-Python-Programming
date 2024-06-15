# **Working of Append Mode**

Let's see how the append mode works:

**Example 1 :**
```py
print("Example - 1")
file = open('append_mode_file.txt','a')
file.write('Hi, I am the appended mode statement')
file.close()
```

**Output:**
```bash
Hi, I am the appended mode statement
```

There are also various other commands in Python file handling that are used to handle various tasks: 

* `rstrip()`: This function strips each line of a file off spaces from the right-hand side.
* `lstrip()`: This function strips each line of a file off spaces from the left-hand side.