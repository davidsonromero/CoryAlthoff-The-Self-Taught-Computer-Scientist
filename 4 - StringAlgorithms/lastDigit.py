def lastDigit(string) -> str:
    ld = [a for a in string if(a.isigit())][-1]
    return ld

string = input("Type something that includes digits.\n")
print(lastDigit(string))