str = 'X-DSPAM-Confidence: 0.8475'
index = str.find(':')
print("The word ':' is at index :", index)

# Slicing the str for getting that desired number
length_of_string = len(str)
print("Length of String: ", length_of_string)
sliced_str = str[index+1 : length_of_string+1]
print("Sliced String: ", sliced_str)
print("The type of Sliced String is: " , type(sliced_str))

# Converting it to the Floating point number
floating_num = float(sliced_str)
print("Converted String to the Floating Number: ", floating_num)
print("The type of the Number which is extracted is: ", type(floating_num))