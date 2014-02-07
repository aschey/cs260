from sys import argv
from dynamicarray import DynamicArray
from matplotlib import pyplot
import time

search = argv[1].lower()
maxTime = int(argv[2])
inSet = argv[3].lower() # either in or out
maxSize = int(argv[4])
numTrials = int(argv[5])
replicates = int(argv[6])

if search != "binary" and search != "linear" and search != "both":
    raise ValueError("first arg must be either 'binary', 'linear', or 'both'")
if inSet != "in" and inSet != "out":
    raise ValueError("third arg must be either 'in' or 'out'")

def main():
    if search == "binary" or search == "both":
        searchData = DynamicArray.fromRandomArray(search, maxSize, 0, 1, 0)
        start = time.time()
        searchData.binarySearch(searchData.get(3))
        finish = time.time() - start
        print(finish)

    if search == "linear" or search == "both":
        start = time.time()
        DynamicArray.fromRandomArray(maxSize, 0, 1, maxSize)
        finish = time.time() - start
    
if __name__ == "__main__":
    main()

