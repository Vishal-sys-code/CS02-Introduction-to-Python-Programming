def isOdd(number):
    if number % 2 == 0:
        return False
    return True

def suminRange(start,end):
    sumofOddNumbers = 0
    for i in range(start, end+1):
        if(isOdd(i)):
            sumofOddNumbers += i
    return sumofOddNumbers

lowerBound = int(input("Enter lower bound of the range: "))
upperBound = int(input("Enter upper bound of the range: "))
print(suminRange(lowerBound,upperBound))