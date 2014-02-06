from sys import argv
from dynamicarray import DynamicArray

def main():
    search = argv[1]
    time = argv[2]
    inSet = argv[3] # either in or out
    maxSize = argv[4]
    numTrials = argv[5]
    replicates = argv[6]
    
    if search == "binary":
        searchData = DynamicArray.fromRandomArray(maxSize, 0, 1, 0)
    elif search == "linear":
        searchData = DynamicArray.fromRandomArray(maxSize, 0, 1, maxSize)
    
    
    
main()

