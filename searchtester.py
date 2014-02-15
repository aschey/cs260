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

    invalidValue = dArray.binarySearch(-1)
    if invalidValue != None:
        raise ValueError("binarySearch fail on value -1")
    print("binarySearch noninclusive value correctly returns None")

    invalidValue = dArray.linearSearch(-1)
    if invalidValue != None:
        raise ValueError("linearSearch fail on value -1")
    print("linearSearch noninclusive value correctly returns None")

if __name__ == "__main__":
    main(1000)
