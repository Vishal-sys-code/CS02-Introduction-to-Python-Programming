arr = []
n = int(input("Enter the number of Elements: "))

for i in range(0,n):
    ele = int(input("Enter Element: "))
    arr.append(ele)

max = arr[0]
min = arr[0]

for i in range(0,n):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print("Largest Element in this Array is: ", max)
print("Smallest Element in this Array is: ", min)