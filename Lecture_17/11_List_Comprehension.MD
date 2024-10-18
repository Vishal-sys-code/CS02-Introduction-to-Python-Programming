# **List Comprehension**
A way to create a new list with less syntax can mimic certain lambda functions easier to read.

**Syntax :** 
* `list = [expression for item in iterable]`
* `list = [expression for item in iterable i conditional]`
* `list = [expression if/else condition for item in iterable]`

**Example 1:**
```py
squares = [] # creates an empty list
for i in range(1, 11): # creates a for loop
	squares.append(i*i) # defines what each loop iteration should do
print(squares)
```

Now lets use the list comprehension to see the less lines of code.

```py
squares = [i*i for i in range(1,11)]
print(squares)
```

**Example 2:**
```py
# Without List Comprehension
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
passed_students = list(filter(lambda x:x>=60, students))
print(passed_students)

# With List Comprehension
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
passed_students = [i for i in students if i >= 60]
passed_students1 = [i if i >=60 else "FAILED" for i in students]
print(passed_students)
```