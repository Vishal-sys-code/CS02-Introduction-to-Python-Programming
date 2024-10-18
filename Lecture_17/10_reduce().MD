# **`reduce()`**

Apply a function to an iterable and reduce it to a single cumulative value. Perform function on first 2 elements and repeat process until 1 value remains.

**Syntax:** `reduce(function, iterables)`

```py
import functools
letters = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x,y: x+y, letters)
print(word)
factorial = [5,4,3,2,1]
result = functools.reduce(labmda x,y: x*y, factorial)
print(factorial)
```