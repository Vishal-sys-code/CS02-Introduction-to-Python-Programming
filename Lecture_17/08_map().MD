# **`map()`**
It applies a function to each item in an iterable (list, tuple, etc.)

**Syntax:** `map(function, iterable)`

```py
store = [("Shirts", 30.00),("Pants", 60.00), ("Jacket", 90.00), ("Socks", 120.00)]
to_euros = labmda data : (data[0], data[1] * 0.82)
to_dollars = labmda data : (data[0], data[1] / 0.82)
store_euros = list(map(to_euros, store))
for i in store_euros:
	print(i)
```
