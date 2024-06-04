# **Nested Function Calls**
Function calls inside the function calls, innermost function calls are resolved first returned value is used as argument for the next outer function.

```py
num = input("Enter the number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
```
The above snippet can also be written as:

```py
print(round(abs(float(input("Enter the number: ")))))
```