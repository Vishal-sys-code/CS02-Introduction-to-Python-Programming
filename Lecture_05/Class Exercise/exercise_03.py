def computepay(hours, rate):
    ans = 0
    if hours>40:
        diff = hours - 40
        ans = (40*rate) + diff*1.5*rate
        return ans
    else:
        return -1

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
hours = float(hours)
rate = float(rate)
ans = computepay(hours, rate)
print(ans)