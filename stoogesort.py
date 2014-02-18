def stoogeSort(array):
    return stoogeRec(array, 0, len(array)-1)

def stoogeRec(array, i, j):
    if array[j] < array[i]:
        array = swap(array, i, j)
    if j - i + 1 >= 3:
        t = (j - i + 1) // 3
        stoogeRec(array, i, j-t)
        stoogeRec(array, i+t, j)
        stoogeRec(array, i, j-t)
    return array

def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp
    return array

print(stoogeSort([3,64,64,23,22,7,433,6]))
