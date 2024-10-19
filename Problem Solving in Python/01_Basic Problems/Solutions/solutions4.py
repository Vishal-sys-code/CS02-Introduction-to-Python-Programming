# Armstrong number: Approach 1
number = int(input("Enter the number: "))
original_number = number
sum_of_powers = 0
exponent = 0

# To find the digits in the number
temp = number
while(temp > 0):
    temp //= 10
    exponent += 1

# Lets perform the sum of the powers
temp = number
while(temp > 0):
    digit = temp % 10
    sum_of_powers += digit ** exponent
    temp //= 10

# Conditional Setup 
if(sum_of_powers == original_number):
    print("This number is Armstrong Number")
else:
    print("This number is not an Armstrong Number")


# Armstrong number: Approach 2
"""
number = int(input("Enter the number: "))
numStr = str(number)
exponent = len(numStr)
sum = 0
for i in numStr:
    sum = sum + pow(int(i), exponent)
if(sum == number):
    print("This number is Armstrong Number")
else:
    print("This number is not an Armstrong Number")
"""
# Time complexity for Second Approach
# Complexity: O(logn)
# Space Complexity: O(1)  # because we are using a constant amount of space. 