from math import sqrt

def isPrime(n) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

n = int(input("Type an integer number:\n"))

print(isPrime(n))