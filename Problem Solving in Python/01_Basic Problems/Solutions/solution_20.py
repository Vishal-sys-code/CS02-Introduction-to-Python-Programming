number = int(input("Enter the number: "))
perfectNumber = []
for i in range(1, number):
    if number % i == 0:
        # print(i)
        perfectNumber.append(i)
    else:
        continue
print(f"Perfect Numbers of {number} is:", perfectNumber)