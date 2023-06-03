def isPowerOfTwo(n) -> bool:
    return n & (n - 1) == 0

n = int(input("Type an integer number:\n"))

print(isPowerOfTwo(n))