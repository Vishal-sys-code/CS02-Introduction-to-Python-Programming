```py
def hello():
    print("Hello")

# Assign function address to the variable
print(hello) # <function hello at 0x01880850>
hi = hello
print(hi) # <function hello at 0x01880850>

hi = hello
hi() # Hello
say = print()
say("Waah! I can't believe this works!!!")
```