import random

def bubbleSort(collection):
    maxIndex = len(collection) - 1
    for i in range(maxIndex):
        hasSwaps = False
        for j in range(maxIndex - i):
            if(collection[j] > collection[j + 1]):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                hasSwaps = True
            print("{} - {}".format(i + 1, j + 1))
        if(not hasSwaps):
            return collection
    return collection

col = list(range(1000))

random.shuffle(col)

print(str(bubbleSort(col)))