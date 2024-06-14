# **Working in Writing Mode**
It is same as the reading a file in the python. 

**Example 1:**
In this example, we will show how the write mode and the write() function is used to write a file and also the close() command terminates all the resources in use and frees the system of this particular program.

```py
print("Example - 1")
file = open('write_mode_file.txt', 'w')
file.write("Hi, This is the write command")
file.write("Nice to meet you")
file.write("It allows us to write in a particular file")
file.close()
```

