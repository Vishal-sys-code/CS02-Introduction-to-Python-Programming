# **While Loops**

It is used to execute a block of statements repeatedly until a given condition is satisfied.

A statement that will execute its block of code as long as its condition remains true.

**Snippet :**
```py
while expression:
    statement(s)
```

**Example 1:**
```py
while 1 == 1:
    print("I am stuck in a loop")
```
In the above code, the loop will run till the infinity.

**Example 2:**
```py
name = ""
while len(name) == 0:
    name = input()
print("Hello " + name)
# If we write the name then it will exit the loop 
```

**Example 3:**
```py
name_1 = None
while not name_1:
    name_1 = input()
print("Hello " + name)
```