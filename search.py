from sys import argv
from dynamicarray import DynamicArray
import pylab
import time
import random

search = argv[1].lower()
maxTime = int(argv[2])
inSet = argv[3].lower() # either in or out
maxSize = int(argv[4])
maxXVal = int(maxSize * 1.1)
minSize = maxSize // 10
numTrials = int(argv[5])
numReps = int(argv[6])

if search != "binary" and search != "linear" and search != "both":
    raise ValueError("first arg must be either 'binary', 'linear', or 'both'")
if inSet != "in" and inSet != "out":
    raise ValueError("third arg must be either 'in' or 'out'")

def main():
    yVals = []
    xVals = [i for i in range(minSize, maxSize+1, minSize)]
    for t in range(1, numTrials+1):
        print("running trial", t, "...")
        for size in range(minSize, maxSize+1, minSize):
            totalTime = 0
            for n in range(numReps):
                totalTime += timeSearch(size)
        avgTime = totalTime / numReps
        yVals.append(avgTime)
    print(len(xVals))
    print(len(yVals))
    pylab.scatter(xVals, yVals)
    pylab.show()

def timeSearch(size):
    if search == "binary":
        swaps = 0
    else:
        swaps = random.randint(0, maxSize)

    if inSet == "out":
        searchVal = -1
    else:
        searchVal = random.randint(0, maxSize)

    searchData = DynamicArray.fromRandomArray(size, swaps)

    times = []
    if search == "binary":
        start = time.time()
        searchData.binarySearch(searchVal)
        return time.time() - start
    else:
        start = time.time()
        searchData.linearSearch(searchVal)
        return time.time() - start



    
if __name__ == "__main__":
    main()

