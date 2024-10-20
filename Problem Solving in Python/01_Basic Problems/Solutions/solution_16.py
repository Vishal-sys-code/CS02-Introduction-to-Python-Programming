arr = []
n = int(input("Enter the number of Elements: "))

for i in range(0,n):
    ele = int(input("Enter Element: "))
    arr.append(ele)

sumOfArray = 0
for i in range(0,n):
    sumOfArray += arr[i]

print("Sum of the Array: ", sumOfArray)