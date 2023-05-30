def isPalindrome(word) -> bool:
    if(word.lower() == word[::-1].lower()):
        return True
    return False

word = input("Type a word\n")

if(isPalindrome(word)):
    print("{} is a palindrome.".format(word))
else:
    print("{} is NOT a palindrome.".format(word))