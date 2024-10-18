# **Zip Functions**

**Syntax:**`zip(*iterables)`

Here, `*iterables` = aggregate elements from two or more iterables(list, sets, tuples, etc.) creates a zip object with paired elements stored in tuples for each elements.

```py
username = ["zuck", "elon", "thisisbillgates"]
password = ["meta@666", "spacex#28", "microsoft#404"]
users = zip(username, password)
print(type(users))
for i in users:
	print(i)
for key,value in user.items():
	print(key + "" + values)
```