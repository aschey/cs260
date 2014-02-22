#################################################
# dynamicarray.py
#
# Creates the DynamicArray class
#
# Author: Austin Schey
#
# Based on the outline created by Dr. John Lusth
#
# 01/15/2014
################################################

from fillablearray import FillableArray

class DynamicArray(FillableArray):
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be 1 or greater")
        super().__init__(capacity)
        # how much to grow or shrink self.store by
        self.factor = 2
        self.INIT_CAPACITY = capacity

    def addToBack(self, value):
        """
        adds the specified value to the end of the array
        """
        # grow the array if it has reached its capacity
        self._growCheck()
        super().addToBack(value)

    def addToFront(self, value):
        """
        adds the specified value to the front of the array
        """
        self._growCheck()
        super().addToFront(value)

    def removeFromBack(self):
        """
        removes the last value in the array
        """
        if self.size <= 0:
            raise IndexError("the array is empty")
        self._shrinkCheck()
        super().removeFromBack()

    def removeFromFront(self):
        """
        removes the first value in the array
        """
        if self.size <= 0:
            raise IndexError("the array is empty")
        self._shrinkCheck()
        super().removeFromFront()

    def _grow(self):
        """
        grows the array by the factor specified in init
        """
        self.capacity *= self.factor
        temp = [None] * self.capacity
        for i in range(self.size):
            temp[i] = self.store[i]
        self.store = temp

    def _shrink(self):
        """
        shrinks the array by the factor specified in init
        """
        self.capacity = round(self.capacity / self.factor)
        temp = [None] * self.capacity
        for i in range(self.capacity):
            temp[i] = self.store[i]
        self.store = temp

    def _growCheck(self):
        """
        grows the array if it is full
        """
        if self.isFull():
            self._grow()

    def _shrinkCheck(self):
        """
        shrinks the array if the size is small enough
        """
        if self.size > self.INIT_CAPACITY and self.size / self.capacity <= 0.25:
            self._shrink()

    def insertAtIndex(self, index, value):
        """
        inserts the value at the specified index
        """
        self._growCheck()
        super().insertAtIndex(index, value)

    def removeFromIndex(self, index):
        """
        removes the value at the specified index
        """
        if self.size <= 0:
            raise IndexError("the array is empty")
        super().removeFromIndex(index)
        self._shrinkCheck()

    def binarySearch(self, value):
        minVal = 0
        maxVal = self.size
        while maxVal > minVal:
            mid = (minVal + maxVal) // 2
            check = self.get(mid)
            if check > value:
                maxVal = mid
            elif check < value:
                minVal = mid + 1
            else:
                return mid

    def binarySearchRec(self, value, minVal, maxVal):
        if maxVal == minVal:
            return None
        mid = (minVal + maxVal) // 2
        check = self.get(mid)
        if check > value:
            return self.binarySearchRec(value, minVal, mid)
        elif check < value:
            return self.binarySearchRec(value, mid+1, maxVal)
        else:
            return mid

    def linearSearch(self, value):
       return self.find(value)

    def mergeSort(self):
        self.helper = [None] * self.size
        self._sort(0, self.size)

    def _sort(self, low, high):
        if high - low < 2:
            return
        middle = (high+low)//2
        self._sort(low, middle)
        self._sort(middle, high)
        self._merge(low, middle, high)

    def _merge(self, low, middle, high):
        for i in range(low, high):
            self.helper[i] = self.store[i]
        i = low
        j = middle
        k = low
        while i < middle and j < high:
            if self.helper[i] <= self.helper[j]:
                self.store[k] = self.helper[i]
                i += 1
            else:
                self.store[k] = self.helper[j]
                j += 1
            k += 1
        while i < middle:
            self.store[k] = self.helper[i]
            k += 1
            i += 1

    def stoogeSort(self):
        return self._stoogeRec(0, self.size-1)

    def _stoogeRec(self, i, j):
        if self.store[j] < self.store[i]:
            self._swap(i, j)
        if j - i + 1 >= 3:
            t = (j - i + 1) // 3
            self._stoogeRec(i, j-t)
            self._stoogeRec(i+t, j)
            self._stoogeRec(i, j-t)

    def _swap(self, a, b):
        temp = self.store[a]
        self.store[a] = self.store[b]
        self.store[b] = temp
   
    def insertionSort(self):
        for i in range(self.size):
            key = self.store[i]
            j = i - 1
            while j >= 0 and self.store[j] > key:
                self.store[j+1] = self.store[j]
                j -= 1
            self.store[j+1] = key
            
    def selectionSort(self):
        for j in range(self.size-1):
            iMin = j
            for i in range(j+1, self.size):
                if (self.store[i] < self.store[iMin]):
                    iMin = i
            if iMin != j:
                self._swap(iMin, j)

    def quickSort(self):
        return self._quickSortRec(0, self.size-1)

    def _quickSortRec(self, low, high):
        if high <= low:
            return
        self._swap(low, (low+high)//2)
        last = low
        for i in range(low+1, high+1):
            if self.store[i] < self.store[low]:
                self._swap(last, i)
        self._swap(low, last)
        self._quickSortRec(low, last-1)
        self._quickSortRec(last+1, high)

def main1():
    dArray = DynamicArray(1)

    dArray.addToFront(3)
    dArray.addToBack(2)
    dArray.addToBack(1)
    dArray.addToFront(4)
    dArray.addToFront(9)
    dArray.addToBack(5)
    dArray.addToBack(2)
    dArray.addToBack(6)
    dArray.addToFront(0)
    dArray.addToFront(9) # 0 9 9 4 3 2 1 5 2 6
    dArray.removeFromFront()
    dArray.removeFromBack()
    dArray.removeFromFront()
    dArray.removeFromBack() # 9 4 3 2 1 5
    a = DynamicArray(1)
    a.addToBack(8)
    a.addToBack(7)
    a.addToBack(6)
    a.addToBack(5)
    a.addToBack(4)
    a.addToBack(3)
    a.addToBack(2)
    a.addToBack(1)
    a.mergeSort()
    a.display()


def main():
    def testStore():
        print("length of store:", len(dArray.store))
        input()

    t.setSleepTime(0)

    dArray = DynamicArray(1)

    dArray.addToFront(3)
    dArray.addToBack(2)
    dArray.addToBack(1)
    dArray.addToFront(4)
    dArray.addToFront(9)
    dArray.addToBack(5)
    dArray.addToBack(2)
    dArray.addToBack(6)
    dArray.addToFront(0)
    dArray.addToFront(9) # 0 9 9 4 3 2 1 5 2 6

    def test1():
        t.template(1, "addToBack and addToFront", dArray.toArray(),
                [9,0,9,4,3,2,1,5,2,6])
        testStore()
    if t.toPrint(1):
        test1()

    dArray.addToFront(1)

    def test2():
        t.template(2, "if grow works correctly", dArray.toArray(),
                [1,9,0,9,4,3,2,1,5,2,6])
        testStore()
    if t.toPrint(2):
        test2()

    dArray.removeFromFront()
    dArray.removeFromFront()
    dArray.removeFromBack()
    dArray.removeFromBack()
    dArray.removeFromFront()
    dArray.removeFromBack()

    def test3():
        t.template(3, "removeFromFront and removeFromBack", dArray.toArray(),
                [9,4,3,2,1])
        testStore()
    if t.toPrint(3):
        test3()

    dArray.removeFromBack()
    dArray.removeFromFront()

    def test4():
        t.template(4, "if shrink works correctly", dArray.toArray(), [4,3,2])
        testStore()
    if t.toPrint(4):
        test4()

    dArray.insertAtIndex(1, 5)

    def test5():
        t.template(5, "insertAtIndex", dArray.toArray(), [4,5,3,2])
        testStore()
    if t.toPrint(5):
        test5()

    dArray.removeFromFront()
    dArray.removeFromBack()

    def test6():
        t.template(6, "shrink at capacity less than the original", dArray.toArray(),
                [5,3])
        testStore()
    if t.toPrint(6):
        test6()

    dArray.removeFromFront()
    dArray.removeFromBack()

    def test7():
        t.template(7, "if capacity will be greater than 0 after" +
                " all elements are removed", dArray.toArray(), [])
        testStore()
    if t.toPrint(7):
        test7()

    for i in range(1000):
        dArray.addToFront(i)
    for i in range(1000):
        dArray.removeFromFront()
    for i in range(1000):
        dArray.addToBack(i)
    for i in range(1000):
        dArray.removeFromBack()
    for i in range(1000):
        dArray.addToBack(i)
    for i in range(1000):
        dArray.removeFromFront()
    for i in range(1000):
        dArray.addToFront(i)
    for i in range(500):
        dArray.removeFromFront()
    for i in range(500):
        dArray.removeFromBack()
    dArray.display()

    def test8():
        t.template(8, "addition and removal of large quantities", dArray.toArray(), [])
        testStore()
    if t.toPrint(8):
        test8()
    
    def test9():
        t.template(9, "insertAtIndex and removeFromIndex", dArray.toArray(), 
                [1,4,3,4])
        testStore()
    if t.toPrint(9):
        test9()

    def test10():
        t.errorTemplate(10, AssertionError, "constructor", DynamicArray, 0)
        testStore()
    if t.toPrint(10):
        test10()

    for i in range(4):
        dArray.removeFromFront()

    def test11():
        t.errorTemplate(11, AssertionError, "removeFromFront", dArray.removeFromFront)
        testStore()
    if t.toPrint(11):
        test11()

    def test12():
        t.errorTemplate(12, AssertionError, "removeFromBack", dArray.removeFromBack)
        testStore()
    if t.toPrint(12):
        test12()

    def test13():
        t.errorTemplate(13, AssertionError, "get", dArray.get, 0)
        testStore()
    if t.toPrint(13):
        test13()

    def test14():
        t.errorTemplate(14, AssertionError, "removeFromIndex", 
                dArray.removeFromIndex, 0)
        testStore()
    if t.toPrint(14):
        test14()
    
    dArray = DynamicArray(1)
    
    dArray.addToFront(0)
    dArray.removeFromFront()
    dArray.addToFront(0)
    dArray.removeFromBack()
    dArray.addToBack(0)
    dArray.removeFromBack()

    def test15():
        t.template(15, "adding and removing on size 1 array", dArray.toArray(), [])
        testStore()
    if t.toPrint(15):
        test15()


if __name__ == "__main__":
    main1()
