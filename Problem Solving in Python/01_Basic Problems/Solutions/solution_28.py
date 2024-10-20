def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)

number = int(input("Enter the number: "))
factorialNumber = factorial(number)
stringNumber = str(factorialNumber)
sum = 0
for i in stringNumber:
    sum = sum + int(i)
print("Sum of the digits of the Factorial is:", sum)