def euclides(n1, n2) -> int:
    if(n2 == 0):
        n1, n2 = n2, n1
    while(n2 != 0):
        n1, n2 = n2, n1 % n2
    return n1

n1 = int(input("Type an integer number:\n"))

n2 = int(input("Type another integer number:\n"))

print(euclides(n1, n2))