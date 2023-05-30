#The book challanges the reader to create a function that returns words from an array that
#have a length greater than or equals to a given number using list comprehension
def filterSize(words, size):
    return [a for a in words if(len(a) >= size)]

words = ["cat", "elephant", "dog", "apple", "lion", "banana", "turtle", "orange", "bird", "watermelon", "fish", "grape", "snake", "mango", "fox", "pear", "monkey", "kiwi", "bear", "cherry"]

size = int(input("Type an integer size\n"))

print("Result:\n" + str(filterSize(words, size)))