# **Loop Control Statements**

It change the loop execution from it's normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. 

The Control Statemetns are:
* **Continue Statement :** returns the control to the beginning of the loop.
* **Break Statement :** brings control out of the loop.
* **Pass Statement :** to write empty loops. Pass is also used for empty control statements, functions and classes.

**Summary :**
* `break`: used to terminate the loop entirely.
* `continue`: skips to the next iteration of the loop.
* `pass`: does nothing, act like a placeholder.

**Examples :**

```py
while True:
    name = input("Enter the name :")
    if name != " ":
        break
```

```py
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end = " ")
```

```py
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end = " ")
```



