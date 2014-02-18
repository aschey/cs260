def selectionSort(array):
    n = len(array)
    for j in range(n-1):
        iMin = j
        #print(j)
        for i in range(j+1, n):
            if (array[i] < array[iMin]):
                iMin = i
        if iMin != j:
            array = swap(array, iMin, j)
    return array

def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp
    return array


print(selectionSort([2,4,7,3,6]))
