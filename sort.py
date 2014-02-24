# usage: python3 search.py alg sort maxTime maxSize numTrials replicates swaps
from sys import argv
from dynamicarray import DynamicArray
from scanner import Scanner
import pylab
import time
import random
import subprocess

# either insertion, selection, stooge, merge, or quick
alg = argv[1]
# either sorted or unsorted
sort = argv[2].lower()
# the maximum time to put on the y axis
maxTime = float(argv[3])
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
if sort != "s" and sort != "u":
    raise ValueError("secont arg must be either 's' or 'u'")

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
        f = open("sorted.dat", "w")
        f.write(str(searchData.toArray()))

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
        searchData.insertionSort()
        finish = time.time()
    
    elif alg == "stooge":
        start = time.time()
        searchData.stoogeSort()
        finish = time.time()

    elif alg == "merge":
        start = time.time()
        searchData.stoogeSort()
        finish = time.time()

    elif alg == "quick":
        start = time.time()
        searchData.quickSort()
        finish = time.time()

    return finish-start

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

def createPlot(xVals, trialVals):
    t = open("timings.gplot", "w")
    t.write("#! /usr/bin/gnuplot\n")
    t.write("set term postscript enhanced eps monochrome\n")
    t.write("set output \"timings.eps\"\n")
    t.write("set xlabel \"Size of array (slots)\"\n")
    t.write("set ylabel \"Average time taken (seconds)\"\n")
    t.write("set pointsize 0.5\n")
    t.write("set key spacing 2\n")
    t.write("set nokey\n")
    t.write("set xrange [0:" + str(maxXVal) + "]\n")
    if maxTime == -1:
        t.write("set autoscale y\n")
    else:
        t.write("set yrange [0:" + str(maxTime) + "]\n")
    t.write("plot for [col=2:" + str(numReps) + "] \"data.txt\" using 1:col " + 
            "with points pointtype 5 title \"Size of array vs average time taken to sort\n")
    t.close()
    
    d = open("data.txt", "w")
    for x,trial in zip(xVals, trialVals):
        d.write(str(x))
        for rep in trial:
            d.write("\t" + str(rep))
        d.write("\n")
    d.close()

    subprocess.call("gnuplot timings.gplot", shell=True)
    subprocess.call("evince timings.eps", shell=True)

if __name__ == "__main__":
    main()

