#The book challenges the reader to implement a sorting algorithm that is not described in chapter 4
#I decided to implement block sort, using merge sort as the block sorting algorithm

from random import shuffle

def mergeSort(collection):
    if(len(collection) > 1):
        mid = len(collection) // 2
        leftHalf = collection[:mid]
        rightHalf = collection[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        indexLeft = 0
        indexRight = 0
        indexCollection = 0

        while(indexLeft < len(leftHalf) and indexRight < len(rightHalf)):
            if(leftHalf[indexLeft] <= rightHalf[indexRight]):
                collection[indexCollection] = leftHalf[indexLeft]
                indexLeft += 1
            else:
                collection[indexCollection] = rightHalf[indexRight]
                indexRight += 1
            indexCollection += 1

        while(indexLeft < len(leftHalf)):
            collection[indexCollection] = leftHalf[indexLeft]
            indexLeft += 1
            indexCollection += 1
        
        while(indexRight < len(rightHalf)):
            collection[indexCollection] = rightHalf[indexRight]
            indexRight += 1
            indexCollection += 1
        print("Block: {}".format(collection))
        return collection

def blockSort(collection, blockSize):
    blocks = []

    for i in range(0, len(collection), blockSize):
        block = collection[i : i + blockSize]
        blocks.append(mergeSort(block))
    
    result = []

    while blocks:
        minIndex = 0
        for i in range(1, len(blocks)):
            if(blocks[i][0] < blocks[minIndex][0]):
                minIndex = i
        result.append(blocks[minIndex].pop(0))

        if(len(blocks[minIndex]) == 0):
            blocks.pop(minIndex)
    return result

collection = list(range(1000))

shuffle(collection)

print("Input: {}".format(collection))
print("\nOutput: {}".format(blockSort(collection, 50)))