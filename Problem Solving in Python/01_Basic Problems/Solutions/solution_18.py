number = int(input("Enter the number: "))
print(f"Multiplication Table of {number} is: ")
for i in range(1, 11):
    print(f"{number} X {i} =", number*i)