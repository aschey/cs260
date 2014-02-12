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
import testtemplate as t
import subprocess

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
        self.shrinkCheck()
        super().removeFromFront()

    def _grow(self):
        """
        grows the array by the factor specified in init
        """
        self.capacity = self.capacity * self.factor
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
        self.growCheck()
        super().insertAtIndex(index, value)

    def removeFromIndex(self, index):
        """
        removes the value at the specified index
        """
        if self.size <= 0:
            raise IndexError("the array is empty")
        self.shrinkCheck()
        super().removeFromIndex(index)

    def binarySearch(self, value):
        minVal = 0
        maxVal = self.size - 1
        while maxVal >= minVal:
            mid = (minVal + maxVal) // 2
            check = self.get(mid)
            if value < check:
                maxVal = mid - 1
            elif value > check:
                minVal = mid + 1
            else:
                return mid

    def linearSearch(self, value):
       return self.find(value)

def main1():
    a = DynamicArray(1)
    for i in range(100000):
        a.addToBack(i)
    a.binarySearch(74345)

    
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
    dArray.addToFront(9)
    
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
