from math import sqrt

def isPrime(n) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def findPrimes(n):
    return [i for i in range(2, n) if isPrime(i)]

n = int(input("Type an integer number:\n"))

print(findPrimes(n))