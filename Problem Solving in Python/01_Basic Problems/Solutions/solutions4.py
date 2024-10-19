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

# Complexity: O(logn)
# Space Complexity: O(1)  # because we are using a constant amount of space. 
