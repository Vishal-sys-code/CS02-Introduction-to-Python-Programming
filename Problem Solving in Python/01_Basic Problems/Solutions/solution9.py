number = int(input("Enter the number: "))
strNumber = str(number)
sum_of_digits = 0
for i in strNumber:
    sum_of_digits += int(i)
print("Sum of the digits: ", sum_of_digits)