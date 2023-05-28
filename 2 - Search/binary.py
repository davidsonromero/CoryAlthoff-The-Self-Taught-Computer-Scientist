import random
import time

class BinarySearch:
    def __init__(self, collection):
        self.collection = collection
    
    def search(self, target):
        first = 0
        last = len(self.collection) - 1
        while(last >= first):
            mid = (first + last) // 2
            if(self.collection[mid] == target):
                return mid
            else:
                if(target < self.collection[mid]):
                    last = mid - 1
                else:
                    first = mid + 1
    def __del__(self):
        print("\n\nEnd")

print("Creating array...\n")
collection = list(range(1000000))

target = random.randint(0, len(collection) - 1)
binarySearch = BinarySearch(collection)
start = time.time()

print("Searching value in the array...\n")
print("Position: " + str(binarySearch.search(target)))

print("Time: " + str(time.time() - start))