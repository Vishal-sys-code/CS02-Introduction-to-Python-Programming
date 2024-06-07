print("-------- Using the break statement --------")
while True:
    name = input("Enter the name: ")
    if name != " ":
        break

print("-------- Using the continue statement --------")
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end = " ")
print()

print("-------- Using the pass statement --------")
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end = " ")