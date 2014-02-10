from sys import argv
from dynamicarray import DynamicArray
from scanner import Scanner
import pylab
import time
import timeit
import random
import subprocess

search = argv[1].lower()
maxTime = float(argv[2])
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

if search == "binary":
    swaps = 0
else:
    swaps = random.randint(0, maxSize)
if inSet == "out":
    searchVal = -1
else:
    searchVal = random.randint(0, maxSize-1)
def main():
    yVals = []
    xVals = [i for i in range(minSize, maxSize+1, minSize)]
    for t in range(1, numTrials+1):
        print("running trial", t, "...")
        for size in range(minSize, maxSize+1, minSize):
            searchData = createSearchArray(size)
            totalTime = 0
            for n in range(numReps):
                totalTime += timeSearch(searchData)
        avgTime = totalTime / numReps
        yVals.append(avgTime)
    m,b = pylab.polyfit(xVals, yVals, 1)
    bestFit = [m*x + b for x in yVals]
    pylab.scatter(xVals, yVals)
    pylab.plot(xVals, bestFit, label="line of best fit")
    pylab.ylim(0, maxTime)
    pylab.xlim(0, maxXVal)
    pylab.title("Size of array vs average time taken to locate value")
    pylab.xlabel("size of array (slots)")
    pylab.ylabel("average time taken (seconds)")
    pylab.legend()
    pylab.show()

def timeSearch(searchData):
    if search == "binary":
        start = time.time()
        searchData.binarySearch(searchVal)
        return time.time() - start
    else:
        start = time.time()
        searchData.linearSearch(searchVal)
        return time.time() - start

def createSearchArray(size):
    command = str.format("python3 makeintegers.py {0} 0 1 {1} > data.out", size, swaps)
    subprocess.call(command, shell=True)
    numFile = Scanner("data.out")
    searchArray = []
    while True:
        token = numFile.readint()
        if token == "":
            break
        else:
            searchArray.append(token)
    return DynamicArray.fromArray(searchArray)
   
if __name__ == "__main__":
    main()

