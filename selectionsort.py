def selectionSort(array):
    n = len(array)
    for j in range(n)):
        iMin = j
        for i in range(j+1, n):
            if (array[i] < array[iMin]):
                iMin = i
        if iMin != j:
            array = swap(array[j], array[iMin])

def swap(a, b, array):
    array[temp] = array[a]
    array[a] = array[b]
    array[b] = array[temp]


print
