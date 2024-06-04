hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
ans = 0
hours = float(hours)
rate = float(rate)
if hours > 40:
    pass
    diff = hours - 40
    ans = (40*rate) + diff*1.5*rate
else:
    ans = 0

print("Pay: " + str(ans))