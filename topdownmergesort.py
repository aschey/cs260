def sort(values):
    number = len(values)
    mergeSort(0, number-1)

def mergeSort(low, high):
    if low < high:
        middle = low + (high-low) // 2
        mergeSort(low, middle)
        mergeSort(middle+1, high)
        merge(low, middle, high)

def merge(low, middle, high):

