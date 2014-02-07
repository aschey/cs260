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
minSize, step = maxSize // 10
numTrials = int(argv[5])
numReps = int(argv[6])

if search != "binary" and search != "linear" and search != "both":
    raise ValueError("first arg must be either 'binary', 'linear', or 'both'")
if inSet != "in" and inSet != "out":
    raise ValueError("third arg must be either 'in' or 'out'")

def main():
    for t in range(numTrials):
        for size in range(minSize, maxSize+1, step)
            bSearchTime = 0
            lSearchTime = 0
            for n in range(numReps):
                if search == "binary" or search == "both":
                    bSearchTime += timeBSearch()
                if search == "linear" or search == "both":
                    lSearchTime += timeLSearch()
            bSearchTime /= numReps
            lSearchTime /= numReps
            pylab.plot([i for i in range(maxXval)])

def timeSearch():
    if search == "binary" or search == "both":
        swaps = 0
    else:
        swaps = random.randint(0, maxSize)

    if inSet == "out":
        searchVal = -1
    else:
        searchVal == random.randint(0, maxSize)

    searchData = DynamicArray.fromRandomArray(size, swaps)

    times = []
    if search == "binary" or search == "both":
        start = time.time()
        searchData.binarySearch(searchData.get(searchVal))
        times.append(time.time() - start)
    if search == "linear" or search == "both":
        start = time.time()
        searchData.linearSearch(searchData.get(searchVal))
        times.append(time.time() - start)
    return times

def timeLSearch():
    searchData = DynamicArray.fromRandomArray(search, size, 0, 1, 0)
    start = time.time()
    DynamicArray.linearSearch(searchData.get(3))
    finish = time.time() - start
    return finish


    
if __name__ == "__main__":
    print(getDataSizes())

