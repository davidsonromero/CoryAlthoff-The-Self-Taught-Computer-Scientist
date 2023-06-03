def greatestCommonFactor(n1, n2) -> int:
    gcf = None
    if(n1 > n2):
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if(n1 % i == 0 and n2 % i == 0):
            gcf = i
    return gcf

n1 = int(input("Type an integer number:\n"))

n2 = int(input("Type another integer number:\n"))

print(greatestCommonFactor(n1, n2))