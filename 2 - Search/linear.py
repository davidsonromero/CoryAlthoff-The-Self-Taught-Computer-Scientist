import time
import random

class LinearSearch:
    def __init__(self, collection):
        self.collection = collection
    
    def search(self, target):
        for i in range(len(self.collection)):
            if(self.collection[i] == target):
                return i

print("Creating array...\n")
collection = list(range(100000000))

target = random.randint(0, len(collection) - 1)
linearSearch = LinearSearch(collection)

start = time.time()

print("Searching value in the array...\n")
print("Position: " + str(linearSearch.search(target)))

print("Time: " + str(time.time() - start))