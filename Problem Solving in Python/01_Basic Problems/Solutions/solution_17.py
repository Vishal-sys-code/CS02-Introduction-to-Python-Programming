lowerBound = int(input("Enter lower bound of the range: "))
upperBound = int(input("Enter upper bound of the range: "))
lstArmstrongNumbers = []
lstNonArmstrongNumbers = []
for number in range(lowerBound, upperBound+1):
    originalNumber = number
    numStr = str(number)
    exponent = len(numStr)
    sumofElements = 0
    for element in numStr:
        sumofElements = sumofElements + pow(int(element), exponent)
    if sumofElements == originalNumber and exponent > 1: # filtering the single-digit numbers
        lstArmstrongNumbers.append(number)
print(f"Armstrong Numbers in the range between {lowerBound} and {upperBound} is: ", lstArmstrongNumbers)