# usage: python3 search.py alg maxTime maxSize numTrials replicates swaps
from sys import argv
from dynamicarray import DynamicArray
from scanner import Scanner
import time
import random
import subprocess
if len(argv) < 7:
    print("usage: python3 search.py algorithm maxTime numTrials replicates swaps")
    exit()
# either insertion, selection, stooge, merge, or quick
alg = argv[1]
# the maximum time to put on the y axis
maxTime = float(argv[2])
# the maximum array size to test
maxSize = int(argv[3])
# the maximum x value to plot
maxXVal = int(maxSize * 1.1)
# how many data points to plot
numTrials = int(argv[4])
# the minimum array size to test
minSize = maxSize // numTrials
# the number of repeat tests
numReps = int(argv[5])
# the number of times to shuffle the data
swaps = int(argv[6])


def main():
    trialVals = []
    # the x values will be each of the size increments
    xVals = [i for i in range(minSize, maxSize+1, minSize)]

    trialNum = 1
    # loop through each array size to be graphed
    for size in range(minSize, maxSize+1, minSize):
        print("running trial", trialNum, "...")
        repVals = []
        #searchData = createSearchArray(size)
        for n in range(numReps):
            searchData = createSearchArray(size)
            repVals.append(timeSearch(searchData))

        f = open("sorted.dat", "w")
        f.write(str(searchData.toArray()))
        f.close()
        
        checkSorted(searchData)

        trialVals.append(repVals)
        trialNum += 1
    createPlot(xVals, trialVals)

def timeSearch(searchData):
    if alg == "insertion":
        start = time.time()
        searchData.insertionSort()
        finish = time.time()
        
    elif alg == "selection":
        start = time.time()
        searchData.selectionSort()
        finish = time.time()
    
    elif alg == "stooge":
        start = time.time()
        searchData.stoogeSort()
        finish = time.time()

    elif alg == "merge":
        start = time.time()
        searchData.mergeSort()
        finish = time.time()

    elif alg == "quick":
        start = time.time()
        searchData.quickSort()
        finish = time.time()

    return finish-start

def createSearchArray(size):
    command = str.format("python3 makeintegers.py {0} 0 1 {1} > ints.out", size, swaps)
    # create a file called data.out with the randomized array
    subprocess.call(command, shell=True)
    numFile = Scanner("ints.out")
    searchArray = DynamicArray(size)

    # create a DynamicArray with the randomized search data
    while True:
        token = numFile.readint()
        if token == "":
            break
        else:
            searchArray.addToBack(token)
    
    return searchArray

def createPlot(xVals, trialVals):
    filename = alg
    if swaps == 0:
        filename += "_sorted"
    else:
        filename += "_unsorted"

    t = open("graphs/" + filename + ".gplot", "w")
    t.write("#! /usr/bin/gnuplot\n")
    t.write("set term postscript enhanced eps monochrome\n")
    t.write("set output \"graphs/" + filename + ".eps\"\n")
    t.write("set xlabel \"Size of array (slots)\"\n")
    t.write("set ylabel \"Average time taken (seconds)\"\n")
    t.write("set title \"sdfsd\"\n")
    t.write("set pointsize 0.5\n")
    t.write("set key spacing 2\n")
    t.write("set nokey\n")
    t.write("set xrange [0:" + str(maxXVal) + "]\n")
    if maxTime == -1:
        t.write("set yrange [0:*]\n")
        t.write("set autoscale ymax\n")
    else:
        t.write("set yrange [0:" + str(maxTime) + "]\n")
    t.write("plot for [col=2:" + str(numReps+1)+ "] \"trials.txt\" using 1:col with points pointtype 5")
    t.close()
    
    d = open("trials.txt", "w")
    for x,trial in zip(xVals, trialVals):
        d.write(str(x))
        for rep in trial:
            d.write("\t" + str(rep))
        d.write("\n")
    d.close()

    subprocess.call("gnuplot graphs/" + filename + ".gplot", shell=True)
    subprocess.call("evince graphs/" + filename + ".eps", shell=True)

def checkSorted(sortedData):
    for i in range(sortedData.getSize()-1):
        # if any number is out of order, the array isn't sorted
        if sortedData.get(i) > sortedData.get(i+1):
            print("ERROR: Data not sorted correctly")
            subprocess.call("geany sorted.dat", shell=True)
            exit()

if __name__ == "__main__":
    main()

