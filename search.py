# usage: python3 search.py search maxTime inSet maxSize numTrials replicates swaps
from sys import argv
from dynamicarray import DynamicArray
from scanner import Scanner
import pylab
import time
import random
import subprocess

# either binary or linear
search = argv[1].lower()
# the maximum time to put on the y axis
maxTime = float(argv[2])
# either in or out, specifies whether to search for a value in or out of the array
inSet = argv[3].lower()
# the maximum array size to test
maxSize = int(argv[4])
# the maximum x value to plot
maxXVal = int(maxSize * 1.1)
# how many data points to plot
numTrials = int(argv[5])
# the minimum array size to test
minSize = maxSize // numTrials
# the number of repeat tests
numReps = int(argv[6])
# the number of times to shuffle the data
swaps = int(argv[7])
if search != "binary" and search != "linear":
    raise ValueError("first arg must be either 'binary' or 'linear'")
if inSet != "in" and inSet != "out":
    raise ValueError("third arg must be either 'in' or 'out'")
if swaps != 0 and search == "binary":
    raise ValueError("a binary search cannot contain swaps")

def main():
    trialVals = []
    # the x values will be each of the size increments
    xVals = [i for i in range(minSize, maxSize+1, minSize)]

    trialNum = 1
    # loop through each array size to be graphed
    for size in range(minSize, maxSize+1, minSize):
        print("running trial", trialNum, "...")
        searchData = createSearchArray(size)

        repVals = []
        for n in range(numReps):
            repVals.append(timeSearch(searchData))

        trialVals.append(repVals)
        trialNum += 1

    # create a scatterplot
    for i in range(numReps):
        yVals = []
        for rep in trialVals:
            yVals.append(rep[i])
        pylab.scatter(xVals, yVals, marker='x')

    # set the attributes of the plot
    pylab.ylim(0, maxTime)
    pylab.xlim(0, maxXVal)
    pylab.title("Size of array vs average time taken to locate value")
    pylab.xlabel("size of array (slots)")
    pylab.ylabel("average time taken (seconds)")
    pylab.savefig(search + "_search_" + inSet + ".eps", format="eps", dpm=3000)

def timeSearch(searchData):
    if inSet == "in":
        searchVal = random.randint(0, searchData.getSize())
    else:
        # -1 will always be out of the range of the search data
        searchVal = -1

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
    # create a file called data.out with the randomized array
    subprocess.call(command, shell=True)
    numFile = Scanner("data.out")
    searchArray = DynamicArray(size)

    # create a DynamicArray with the randomized search data
    while True:
        token = numFile.readint()
        if token == "":
            break
        else:
            searchArray.addToBack(token)

    return searchArray

if __name__ == "__main__":
    main()

