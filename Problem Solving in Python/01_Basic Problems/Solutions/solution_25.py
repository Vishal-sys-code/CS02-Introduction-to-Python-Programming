# Approach 1
number = int(input("Enter the number: "))
numString = str(number)
print(f"The number {number} has", len(numString), "digits")

# Approach 2
number = int(input("Enter the number: "))
countNum = 0
temp = number
while temp > 0:
    countNum += 1 # counting the digits
    temp //= 10 # taking the quotient till 0
# Here we dont need remainder to take care of
print(f"The number {number} has {countNum} digits")

"""
NOTES: In counting the digits of a number we don't need to take care of the remainder.
"""