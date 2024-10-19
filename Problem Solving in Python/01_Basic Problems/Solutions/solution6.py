string = str(input("Enter the string: "))
reversedString1 = ''.join(reversed(string))
reversedString2 = string[::-1]
print("Original String: ", string)

print("------------ Using join and reversed ------------")
if(string == reversedString1):
    print("The string is PALINDROME")
else:
    print("The string is not PALINDROME")

print("------------ Using slicing ------------")
if(string == reversedString2):
    print("The string is PALINDROME")
else:
    print("The string is not PALINDROME")