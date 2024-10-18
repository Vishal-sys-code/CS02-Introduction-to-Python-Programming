import math
number = int(input("Enter the number: "))
if number < 2:
    print(number, "is not a Prime Number.")
else:
    isPrime = True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            isPrime = False
            break
    if isPrime:
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")