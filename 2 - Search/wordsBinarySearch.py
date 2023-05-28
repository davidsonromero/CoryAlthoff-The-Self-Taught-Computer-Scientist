class WordBinarySearch:
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

target = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fox', 'giraffe']

wordsBinarySearch = WordBinarySearch(target)

print(wordsBinarySearch.search("cat"))