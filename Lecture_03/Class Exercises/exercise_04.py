# C/5 = (F-32)/9
# F = (9*C/5)+32

celcius = input("Enter the Celcius: ")
celcius = int(celcius)
fahrenheit = float((9*celcius/5)+32)
print("Fahrenheit: " + str(fahrenheit) + " °F")