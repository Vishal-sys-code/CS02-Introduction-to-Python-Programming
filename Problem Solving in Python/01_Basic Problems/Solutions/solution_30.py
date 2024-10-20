def findingMissingNumber(sequence):
    lowerBound = min(sequence)
    upperBound = max(sequence)
    fullset = set(range(lowerBound,upperBound+1))
    sequenceset = set(sequence)
    set_difference = (fullset - sequenceset)
    return set_difference

sequence = []
n = int(input("Enter the number of Elements: "))
for i in range(0,n):
    ele = int(input("Enter Element: "))
    sequence.append(ele)

print(f"Missing Value: ",findingMissingNumber(sequence))