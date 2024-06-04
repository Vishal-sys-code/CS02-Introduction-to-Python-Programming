try:
    hours = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    hours = int(hours)
    rate = int(rate)
    ans = hours * rate
    print(ans)
except ValueError:
    print("Error, please enter numeric input")