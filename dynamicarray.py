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
import sys
sys.setrecursionlimit(100000)
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
        # an array of size 1 is already sorted
        if high - low < 2:
            return
        middle = (high+low)//2
        # sort the lower half of the array
        self._sort(low, middle)
        # sort the upper half of the array
        self._sort(middle, high)
        # merge the array from low to middle and middle to high
        self._merge(low, middle, high)

    def _merge(self, low, middle, high):
        # make a copy of the values to start to prevent overriding
        for i in range(low, high):
            self.helper[i] = self.store[i]
        # the lowest value of the first array
        i = low
        # the lowest value of the second array
        j = middle
        # the index to place the new lowest value in
        k = low
        # continuously compare the lowest values of the first and second part of the array
        while i < middle and j < high:
            # if the first array has the lower value, move it to the first available space
            if self.helper[i] <= self.helper[j]:
                self.store[k] = self.helper[i]
                i += 1
            # else, move the value from the second array to the first available space
            else:
                self.store[k] = self.helper[j]
                j += 1
            k += 1
        # copy the remaining elements from the helper into the array
        while i < middle:
            self.store[k] = self.helper[i]
            k += 1
            i += 1
        
    def stoogeSort(self):
        return self._stoogeRec(0, self.size)

    def _stoogeRec(self, i, j):
        # swap the first and last values if the first value is greater
        if self.store[j-1] < self.store[i]:
            self._swap(i, j-1)
        # base case: length of the array to be sorted is less than 3
        if j - i >= 3:
            # split the array into three parts
            t = (j - i) // 3
            # sort the first two-thirds of the array
            self._stoogeRec(i, j-t)
            # sort the second two-thirds of the array
            self._stoogeRec(i+t, j)
            # sort the first two-thirds of the array again
            self._stoogeRec(i, j-t)

    def _swap(self, a, b):
        temp = self.store[a]
        self.store[a] = self.store[b]
        self.store[b] = temp
   
    def insertionSort(self):
        for i in range(self.size):
            key = self.store[i]
            j = i
            # move all values up until a value greater than the key is found
            while j > 0 and self.store[j-1] > key:
                self.store[j] = self.store[j-1]
                j -= 1
            # set the key at the index one before the value greater than the key that was found
            self.store[j] = key
            
    def selectionSort(self):
        for j in range(self.size):
            iMin = j
            for i in range(j, self.size):
                # scan the array from the starting value to the end, 
                # searching for a value less than the starting value
                if (self.store[i] < self.store[iMin]):
                    iMin = i
            # if a smaller value is found, swap it with the starting value
            if iMin != j:
                self._swap(iMin, j)

    def quickSort(self):
        return self._quickSortRec(0, self.size)

    def _quickSortRec(self, low, high):
        # base case: the array is size 1
        if high-low > 1:
            # pivot on the first element
            pivot = self.store[low]
            left = low
            right = high
            # while the area to search is greater than 0
            while left < right:
                # find the first value greater than or equal to the pivot
                while self.store[left] < pivot:
                   left += 1
                # find the last value less than or equal to the pivot
                while self.store[right-1] > pivot:
                    right -= 1
                # if the area to search is still greater than 0, swap the values found in the previous two loops
                if left < right:
                    self._swap(left, right-1)
                    left += 1
                    right -= 1
            # sort from the beginning to the last value less than the pivot
            self._quickSortRec(low, right)
            # sort from the pivot to the end
            self._quickSortRec(left, high)

        
def main1():
    import random
    dArray = DynamicArray(3000)
    for i in range(3000): 
        dArray.addToFront(i)
    dArray.stoogeSort()

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
