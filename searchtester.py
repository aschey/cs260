from dynamicarray import DynamicArray

def main(n):
    dArray = DynamicArray(n)
    for i in range(n):
        dArray.addToBack(i)

    for i in range(n):
        if dArray.binarySearch(i) != i:
            raise ValueError("binarySeach fail on index" + i)
    print("all binarySearch values found correctly")

    for i in range(n):
        if dArray.linearSearch(i) != i:
            raise ValueError("linearSearch fail on index" + i)
    print("all linearSearch values found correctly")

    for i in range(n):
        if dArray.binarySearchRec(i, 0, n) != i:
            raise ValueError("binarySearchRec fail on index" + i)
    print("all binarySearchRec values found correctly")

    invalidValue = dArray.binarySearch(-1)
    if invalidValue != None:
        raise ValueError("binarySearch fail on value -1")
    print("binarySearch noninclusive value -1 correctly returns None")

    invalidValue = dArray.linearSearch(-1)
    if invalidValue != None:
        raise ValueError("linearSearch fail on value -1")
    print("linearSearch noninclusive value -1 correctly returns None")

    invalidValue = dArray.binarySearchRec(-1, 0, n)
    if invalidValue != None:
        raise ValueError("binarySearchRec fail on value -1")
    print("binarySearchRec noninclusive value -1 correctly returns None")

    dArray.removeFromIndex(45)
    invalidValue = dArray.binarySearch(45)
    if invalidValue != None:
        raise ValueError("binarySearch fail on value 45")
    print("binarySearch noninclusive value 45 correctly returns None")

    invalidValue = dArray.linearSearch(45)
    if invalidValue != None:
        raise ValueError("linearSearch fail on value 45")
    print("linearSearch noninclusive value 45 correctly returns None")

    inValidValue = dArray.binarySearchRec(45, 0, n)
    if invalidValue != None:
        raise ValueError("binarySearchRec fail on value 45")
    print("binarySearchRec noninclusive value 45 correctly returns None")
    
    dArray = DynamicArray(2*n)
    for i in range(0, 2*n, 2):
        dArray.addToBack(i)
    for i in range(0, 2*n):
        print(dArray.binarySearch(i))
    for i in range(0, 2*n):
        print(dArray.binarySearchRec(i, 0, len(dArray)))

if __name__ == "__main__":
    main(1000)
