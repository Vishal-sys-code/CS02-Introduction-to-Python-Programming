# **Working in Read Mode**

**File Handling: Read Mode...**

There is a file called `file.txt` that have the contents of:
`file.txt`
```bash
Hi,
My name is: file.txt
I am created before the creation of the py file.
```

**Example 1:**

The open command will open the py file in the read mode and the for loop will print each line present in the file

```py
import os
# The file "file.txt", will be opened with the reading mode
file = open('file.txt', 'r')

# Printing each line one by one in the file
for each in file:
    print(each)
```

<hr>

**Example 2:**

We will extract a string that contains all characters in the python file then we can use **`file.read()`**

```py
file = open("file.txt", "r")
print(file.read())
```

<hr>

**Example 3:**
We can read a file using the `with` statement

```py
with open("file.txt") as file:
    data = file.read()

print(data)
```

<hr>

**Example 4:**
We can call the certain number of characters from the file

```py
file = open("geeks.txt", "r")
print (file.read(5))
```

**Output of all the examples:**

```bash
------ File opening in Reading mode ------
--- Example 1 ---
Hi,

My name is: file.txt

I am created before the creation of the py file.

--- Example 2 ---
Hi,
My name is: file.txt
I am created before the creation of the py file.

--- Example 3 ---
Hi,
My name is: file.txt
I am created before the creation of the py file.

--- Example 4 ---
Hi,
M
```