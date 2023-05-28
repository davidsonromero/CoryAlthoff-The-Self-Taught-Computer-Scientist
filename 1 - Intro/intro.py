n = int(input("Type any integer amount: "))

#Algorythm O(1)
print("O(1)\n")
sum = 0

for i in range (100):
    print(i + 1)
    sum += i + 1

print(str(sum))
#======================================================
#Algorythm O(n)
print("\nO(n)\n")
sum = 0

for i in range (n):
    print(i + 1)
    sum += i + 1

print(str(sum))
#======================================================
#Algorythm O(n^2)
print("\nO(n^2)\n")
sum = 0

for i in range (n):
    print(i + 1)
    sum += i + 1
    for j in range (n):
        print(j + 1)
        sum += j + 1
    
print(str(sum))
#======================================================
#Algorythm O(n^3)
print("\nO(n^3)\n")
sum = 0

for i in range (n):
    print(i + 1)
    sum += i + 1
    for j in range (n):
        print(j + 1)
        sum += j + 1
        for x in range (n):
            print(x + 1)
            sum += x + 1
    
print(str(sum))
#======================================================
#Algorythm O(c^n)
print("\nO(n^3)\n")
sum = 0

for i in range (3 ** n):
    print(i + 1)
    sum += i + 1
    
print(str(sum))
#======================================================
#Space complexity - the greater is "num", the greater will be the occupied space in memory
print("Fatorial")
def factorial (num):
    if(num == 0):
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(n))
#======================================================