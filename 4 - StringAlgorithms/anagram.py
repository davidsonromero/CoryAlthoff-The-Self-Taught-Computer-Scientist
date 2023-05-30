def isAnagram(s1, s2) -> bool:
    s1.replace(' ', '').lower()
    s2.replace(' ', '').lower()
    if(sorted(s1) == sorted(s2)):
        return True
    return False

s1 = input("Type something\n")
s2 = input("Type something else\n")

if(isAnagram(s1, s2)):
    print("{} and {} are anagrams.".format(s1, s2))
else:
    print("{} and {} are NOT anagrams.".format(s1, s2))