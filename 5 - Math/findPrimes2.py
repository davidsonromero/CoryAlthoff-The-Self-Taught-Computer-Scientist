#The book challanges the reader to implement a different algorithm to find prime numbers
#I decided to implement the Sieve of Atkin

def findPrimes2(num):
    if num > 2:
        print(2, end=" ")
    if num > 3:
        print(3, end=" ")
    
    sieve = [False] * (num + 1)
    for i in range(0, num + 1):
        sieve[i] = False
    
    x = 1
    while(x ** 2 <= num):
        y = 1
        while(y ** 2 <= num):
            n = (4 * x * x) + (y * y)
            if(n <= num and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if(n <= num and n % 12 == 7):
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= num and n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    r = 5
    while(r * r <= num):
        if(sieve[r]):
            for i in range(r * r, num+1, r * r):
                sieve[i] = False

        r += 1

    for a in range(5, num+1):
        if(sieve[a]):
            print(a, end=" ")
            

n = int(input("Type an integer number:\n"))

findPrimes2(n)