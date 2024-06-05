def add_without_NKargs(num1, num2):
    sum = num1 + num2
    return sum

print("-------- NOT Using *args --------")
print(add_without_NKargs(1,2))
print(add_without_NKargs(11,22))
print(add_without_NKargs(71,29))
#print(add_without_NKargs(1,2,3))

"""
The following above code has given the error of:
TypeError: add() takes 2 positional arguments but 3 were given.

So to fix this we need argument packing. Which can be done by the *args keyword.

Let's do it.
"""

#---------------------------------------------------------------------------------------------------#
def add_with_NKargs(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print("-------- Using *args --------")
print(add_with_NKargs(1,2))
print(add_with_NKargs(11,22))
print(add_with_NKargs(71,29))
print(add_with_NKargs(1,2,3))
print(add_with_NKargs(1,2,3,4,5,6,7,8,9,10))

#---------------------------------------------------------------------------------------------------#

"""
We can change the name of the *args to anything like your name too.
It can be *jack, *annie or anything.
"""

def args_function_name_change(*annie):
    mul = 1
    for i in annie:
        mul = mul * i
    return mul

print("-------- Changing the name of the *args to anyname --------")
print(args_function_name_change(1,2))
print(args_function_name_change(2,2))
print(args_function_name_change(3,0))
print(args_function_name_change(1,2,3,4,5,6,7,8,9,10))