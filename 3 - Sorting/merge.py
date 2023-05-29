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
        print(collection)
        return collection
    
collection = list(range(1000))

shuffle(collection)

print(mergeSort(collection))