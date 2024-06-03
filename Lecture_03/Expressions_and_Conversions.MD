# **Expressions**
* An expression is the combination of the operator and operands that is interpreted to produce some output value. 

* `+`   : Addition
* `-`   : Substraction
* `*`   : Multiplication
* `/`   : Division
* `**`  : Power | Expectation
* `%`   : Remainder

## **Operator Precedence Rules**

Higher precedence rule to lowest precedence rule:
* Parentheses are always respected
* Exponentiation (raise to power)
* Multiplication, Division and Remainder
* Addition and Substraction
* Left to Right

### **Type of Variables**
```py
num = 123
print(num)
type(num)

num1 = 123.3
type(num1)

name = "John"
print(name)
type(name)
```

### **Type Conversions**
* When you put an integer and floating point in an expression, the interger is implicitly converted to a float

```py
print(float(99) + 100) #199.0
i = 42
type(i)

f = float(i)
print(f)
type(f)
```

### **Integer Division**
```py
print(10/2) #5.0
print(9/2) #4.5
print(99/100) #0.99
print(10.0/2.0) # 5.0
print(99.0/100.0) #0.99
```

### **String Conversions**
* We can only use `int()` and `float()` to convert between string and integers.

```py
str = "123"
type(str)

num = int(str)
type(num)
print(num)
```