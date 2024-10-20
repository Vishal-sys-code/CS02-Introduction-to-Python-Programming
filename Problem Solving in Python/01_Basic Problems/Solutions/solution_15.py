arr = []
n = int(input("Enter the number of Elements: "))

for i in range(0,n):
    ele = int(input("Enter Element: "))
    arr.append(ele)

print("Before Sorting: ")
print(arr)
print("After Sorting[increasing order]: ")
arr.sort()
print(arr)
print("After Sorting[decreasing order]: ")
arr.sort(reverse=True)
print(arr)