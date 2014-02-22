def merge(A, startL, stopL, startR, stopR):
    #print(A)
    #print(startL) #0
    #print(stopL) #1
    #print(startR) #1
    #print(stopR) #2
    #2 5
    #4 6
    leftL = A[startL:stopL]
    rightL = A[startR:stopR]
    i = 0
    j = 0
    k = startL
    B = copy(A)
    while i < len(leftL) and j < len(rightL):
        #print(i)
        #print(j)
        #print(leftL)
        #print(rightL)
        #print(startL)
        #print(stopL)
        #print(startR)
        #print(stopR)
        print(A)
        if leftL[i] < rightL[j]:
            A[k] = leftL[i]
            i += 1
        else:
            A[k] = rightL[j]
            j += 1
        k += 1

def mergeSort(A, length):
    if length < 2:
        return
    step = 1
    while step < length:
        startL = 0
        startR = step
        while startR + step < length:
            merge(A, startL, startL+step, startR, startR+step)
            startL = startR + step
            startR = startL + step
        if startR < length:
            A = merge(A, startL, startL+step, startR, length)
        step *= 2
    return A

def copy(a):
    b = [None] * len(a)
    for i in range(len(a)):
        b[i] = a[i]
    return b

print(mergeSort([2,5,4,6,2,4,6,1], 8))
