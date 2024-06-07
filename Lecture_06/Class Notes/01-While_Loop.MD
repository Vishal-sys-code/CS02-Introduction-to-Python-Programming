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

Formally, here is the flow of execution for a while statement:
* Evaluate the condition, yielding `True` or `False`.
* If the condition is `false`, exit the while statement and continue execution at the next statement.
* If the condition is `true`, execute the body and then go back to step 1.

This type of flow is called a `loop` because the third step loops back around to the top. We call each time we execute the body of the loop an iteration.

The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates. We call the variable that changes each time the loop executes and controls when the loop finishes the iteration variable. If there is no iteration variable, the loop will repeat forever, resulting in an `infinite loop`.