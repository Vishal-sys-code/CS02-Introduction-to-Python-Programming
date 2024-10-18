# **`filter()`**

Creates a collection of element from an iterable for which a function return true.

**Syntax:** `filter(function, iterable)`

```py
friends = [("Rachel", 20), ("Monica", 42), ("Richard", 19), ("Phoebe", 22), ("Ross", 23), ("Joey", 24)]
age = lambda data : data [1] >= 18
drinkingBuddies = list(filter(age, friends))
for i in drinkingBuddies:
	print(i)
```