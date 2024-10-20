limit = 100
a,b = 0,1
fibonacci_numbers = [a,b]
for i in range(2,limit):
    c = a+b
    fibonacci_numbers.append(c)
    a, b = b, c
position = int(input("Enter the position: "))
print(fibonacci_numbers[position])