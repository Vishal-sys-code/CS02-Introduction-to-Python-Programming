import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The LCM of", a, "and", b, "is:", (a/math.gcd(a,b))*b)