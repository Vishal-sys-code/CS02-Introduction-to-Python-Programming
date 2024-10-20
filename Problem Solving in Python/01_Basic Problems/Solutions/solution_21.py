def isEven(number):
    if number % 2 == 0:
        return True
    return False

def suminRange(start,end):
    sumofEvenNumbers = 0
    for i in range(start, end+1):
        if(isEven(i)):
            sumofEvenNumbers += i
    return sumofEvenNumbers

lowerBound = int(input("Enter lower bound of the range: "))
upperBound = int(input("Enter upper bound of the range: "))
print(suminRange(lowerBound,upperBound))