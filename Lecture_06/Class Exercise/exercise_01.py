largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num.lower() == "done":
        continue

    try:
        num = int(num)
    except ValueError:
        print("Invalid input")
        break
    
    if largest == None or num > largest:
        largest = num
    if smallest == None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)