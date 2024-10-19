# Approach 1: Fibonacci Series [in Limit]
def generateFibonacci(limit):
    fibonacci_numbers = []
    a,b = 0,1
    while a<=limit:
        fibonacci_numbers.append(a)
        a,b = b, b+a
    return fibonacci_numbers

limit1 = int(input("Enter the limit: "))
print(generateFibonacci(limit1))

# Approach 2: Fibonacci Series [in Range]
limit = int(input("Enter the limit: "))
a,b = 0,1
fibonacci_numbers = [a,b]
for i in range(2,limit):
    c = a+b
    fibonacci_numbers.append(c)
    a = b
    b = c
print(fibonacci_numbers)

# Approach 3: Fibinacci Numbers [in Range]
limit = int(input("Enter the limit: "))
a,b = 0,1
fibonacci_numbers = [a,b]
for i in range(2,limit):
    fibonacci_numbers.append(c)
    a,b = b, a+b
print(fibonacci_numbers)