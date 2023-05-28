import random

def insertionSort(collection):
    for i in range(1, len(collection)):
        value = collection[i]
        while(i > 0 and collection[i - 1] > value):
            collection[i] = collection[i - 1]
            i -= 1
        collection[i] = value
        print(collection)
    return collection

collection = list(range(1000))

random.shuffle(collection)

print(insertionSort(collection))