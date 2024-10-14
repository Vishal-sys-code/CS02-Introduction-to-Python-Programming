try:
    raise NameError("Hi there!!!")
except NameError:
    print("An error occurred!!!")
    raise

"""
Output: 
py", line 2, in <module>
    raise NameError("Hi there!!!")
NameError: Hi there!!!
"""