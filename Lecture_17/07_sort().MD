# **`sort()`**

* sort() method = used with lists 
* sort() functions = used with iterables

```py
students = ['spongebob', 'sandy', 'patrick', 'squidward', 'mr.krab']
students.sort()
for i in students:
    print(i)
## to reverse
students.sort(reverse=True)
```

if we use: 
`students = ('spongebob', 'sandy', 'patrick', 'squidward', 'mr.krab')`
It will throw an error of AttributeError: 'tuple' object has no attribute 'sort'
To sort this we need the built in functions:

```py
sorted_students = sorted(students)
for i in sorted_students:
    print(i)
```

To reverse it we will use :- `sorted(students, reverse = True)`

Suppose we have list of tuples:
```py
students = [("Squidward", "F", 60), ("Sandy", "A", 33), ("Patrick", "D", 36),("Spongebob", "B", 20), ("Mr. Krab", "C", 78)]
grades = lambda grades:grades[1]
ages = lambda ages:ages[2]
students.sort(key = grades)
for i in students:
    print(i)

students.sort(key = grades, reverse = True)
```

Now, suppose we have the list of the list:-

```py
students = (("Squidward", "F", 60), ("Sandy", "A", 33), ("Patrick", "D", 36),("Spongebob", "B", 20), ("Mr. Krab", "C", 78))
ages = lambda ages:ages[2]
sorted_students = sorted(students, key=ages)
for i in sorted_students:
    print(i)
```