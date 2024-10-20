import math
def isPrime(number):
    if number<=1:
        return False
    for i in range(2, int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

def primeinRanges(start, end):
    primes = []
    for i in range(start, end+1):
        if isPrime(i):
            primes.append(i)
    return primes

number = int(input("Enter the number: "))
start = 2 # as the prime will always start from here only
end = number
print(primeinRanges(start, end))