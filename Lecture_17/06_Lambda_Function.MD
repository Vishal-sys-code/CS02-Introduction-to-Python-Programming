# **Lambda Functions**
The functions written in 1 line using lambda keywords accepts any number of arguments but only has one expression.

**Syntax:** `lambda parameters : expressions`

**Example 1:**
```py
def double(x):
    return x*2
double(10)
```

Applying Lambda function to the Example 1

```py
double = lambda x: x*2
print(double(10))
```

**Example 2:**
```py
product = lambda x,y: x*y
print(product(10,10))

add = lambda x,y,z: x+y+z
print(add(20,20,20))

fullName = lambda f_n,l_n: f_n+" "+l_n
print(fullName("Richard","Taylor"))

age_check = lambda age:True if age>=18 else false
print(age_check(38))

"""
Output:
100
60
Richard Taylor
True"""
```