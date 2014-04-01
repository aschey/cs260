###############################################
# dynamiccirculararray.py
# 
# creates the dynamic circular array class
#
# Based on the outline created by Dr. John Lusth
#
# 01/17/2014
################################################

from circulararray import CircularArray
import time

class DynamicCircularArray(CircularArray):
    def __init__(self, capacity):
        super().__init__(capacity)
        # how much to grow or shrink self.store by
        self.factor = 2
        self.INIT_CAPACITY = capacity
    
    @staticmethod
    def fromArray(array):
        """
        used as an alternative constructor, creates a DynamicCircularArray
        from a normal array
        """
        temp = DynamicCircularArray(len(array))
        temp.store = array
        temp.size = len(array)
        temp.endIndex = len(array)
        return temp
    
    def addToBack(self, value):
        """
        adds the value to the back of the array
        """
        self._growCheck()
        super().addToBack(value)

    def removeFromBack(self):
        """
        removes the value from the back of the array
        """
        super().removeFromBack()
        self._shrinkCheck()
        
    def addToFront(self, value):
        """
        adds the value to the front of the array
        """
        self._growCheck()
        super().addToFront(value)

    def removeFromFront(self):
        """
        removes the first value in the array
        """
        super().removeFromFront()
        self._shrinkCheck()
    
    def _grow(self):
        """
        increases the size of self.store by the factor
        """
        tempCapacity = self.capacity * self.factor
        self.store = self._copyValues(tempCapacity)
        self.capacity = tempCapacity
        # reset the startIndex because all the elements are now pushed all the
        # way to the left
        self.startIndex = 0
        self.endIndex = self.size

    def _shrink(self):
        """
        decreases the size of self.store by the factor
        """
        tempCapacity = round(self.capacity / self.factor)
        self.store = self._copyValues(tempCapacity)
        self.capacity = tempCapacity
        self.startIndex = 0
        self.endIndex = self.size

    def _copyValues(self, capacity):
        temp = [None] * capacity
        for i in range(self.size):
            temp[i] = self.get(i)
        return temp

    def _growCheck(self):
        """
        grows the array if it is full
        """
        if self.isFull():
            self._grow()

    def _shrinkCheck(self):
        """
        shrinks the array if it is small enough
        """
        if self.size / self.capacity <= 0.25 and self.capacity > self.INIT_CAPACITY:
            self._shrink()

def main():
    def testStore():
        print("length of store:",len(dcArray.store))
        input()

    t.setSleepTime(0)

    dcArray = DynamicCircularArray(1)
    
    dcArray.addToFront(2)
    dcArray.addToBack(4)
    dcArray.addToFront(3)
    dcArray.addToFront(5)
    dcArray.addToBack(7)
    
    def test1():
        t.template(1, "addToFront and addToback", dcArray.toArray(), [5,3,2,4,7])
        testStore()
    if t.toPrint(1):
        test1()

    dcArray.addToBack(3)
    dcArray.addToFront(4)
    dcArray.addToBack(4)
    dcArray.addToBack(6)
    dcArray.addToBack(5)
    dcArray.addToFront(9)
    
    def test2():
        t.template(2, "if the array expands correctly", dcArray.toArray(), \
                [9,4,5,3,2,4,7,3,4,6,5])
        testStore()
    if t.toPrint(2):
        test2()

    for i in range(10):
        dcArray.addToFront(i)

    def test3():
        t.template(3, "array expansion again", dcArray.toArray(),
                [9,8,7,6,5,4,3,2,1,0,9,4,5,3,2,4,7,3,4,6,5])
        testStore()
    if t.toPrint(3):
        test3()

    dcArray.setAtIndex(0, 10)
    dcArray.setAtIndex(21, 10)

    def test4():
        t.template(4, "setAtIndex", dcArray.toArray(),
                [10,8,7,6,5,4,3,2,1,0,9,4,5,3,2,4,7,3,4,6,5,10])
        testStore()
    if t.toPrint(4):
        test4()

    for i in range(8):
        dcArray.removeFromBack()
        dcArray.removeFromFront()

    dcArray.removeFromBack()
    dcArray.removeFromBack()

    def test5():
        t.template(5, "removeFromFront and removeFromBack", dcArray.toArray(),
                [1,0,9,4])
        testStore()
    if t.toPrint(5):
        test5()

    for i in range(4):
        dcArray.removeFromFront()

    def test6():
        t.template(6, "if the array shrinks correctly", dcArray.toArray(), [])
        testStore()
    if t.toPrint(6):
        test6()

    for i in range(1000):
        dcArray.setAtIndex(i, i)

    def test7():
        t.template(7, "find", dcArray.find(10), 10)
        testStore()
    if t.toPrint(7):
        test7()

    for i in range(1000, 2000):
        dcArray.setAtIndex(i, i-1000)

    def test8():
        t.template(8, "rfind", dcArray.rfind(10), 1010)
        testStore()
    if t.toPrint(8):
        test8()

    def test9():
        t.template(9, "findall", dcArray.findAll(10), [10,1010])
        testStore()
    if t.toPrint(9):
        test9()
    
    for i in range(2000):
        dcArray.removeFromFront()
    
    def test10():
        t.template(10, "isEmpty", dcArray.isEmpty(), True)
        testStore()
    if t.toPrint(10):
        test10()
    
    for i in range(100000):
        dcArray.addToFront(i)
    for i in range(100000):
        dcArray.addToBack(i)
    for i in range(100000):
        dcArray.removeFromFront()
    for i in range(100000):
        dcArray.removeFromBack()

    def test11():
        t.template(11, "adding and removing a large amount of values",
                dcArray.isEmpty(), True)
        testStore()
    if t.toPrint(11):
        test11() 

    for i in range(100000):
        dcArray.setAtIndex(i,i)
    
    def test12():
        t.template(12, "adding a large amount with setAtIndex", dcArray.get(99999), 
                99999)
        testStore()
    if t.toPrint(12):
        test12()

    for i in range(50000):
        dcArray.removeFromFront()
        dcArray.removeFromBack()

    def test13():
        t.template(13, "removal of the previous values", dcArray.toArray(), [])
        testStore()
    if t.toPrint(13):
        test13()

    dcArray = DynamicCircularArray.fromArray([1,2,3])

    def test14():
        t.template(14, "fromArray", dcArray.toArray(), [1,2,3])
        testStore()
    if t.toPrint(14):
        test14()
    
    for i in range(100000):
        dcArray.addToFront(i)
    for i in range(100000):
        dcArray.addToBack(i)
    for i in range(100000):
        dcArray.setAtIndex(i, i)

    def test15():
        t.template(15, "large input values", dcArray.get(99999), 99999)
        testStore()
    if t.toPrint(15):
        test15()
    
    for i in range(100001):
        dcArray.removeFromBack()
        dcArray.removeFromFront()
    dcArray.removeFromFront()
    
    for i in range(10000):
        dcArray.addToFront(i)
    for i in range(10000):
        dcArray.removeFromFront()
    for i in range(10000):
        dcArray.addToBack(i)
    for i in range(10000):
        dcArray.removeFromBack()
    for i in range(10000):
        dcArray.addToBack(i)
    for i in range(10000):
        dcArray.removeFromFront()
    for i in range(10000):
        dcArray.addToFront(i)
    for i in range(10000):
        dcArray.removeFromBack()
    
    def test16():
        t.template(16, "removing large input values", dcArray.toArray(), [])
        testStore()
    if t.toPrint(16):
        test16()

    def test17():
        t.errorTemplate(17, AssertionError, "invalid capacity in constructor",
                DynamicCircularArray, 0)
        testStore()
    if t.toPrint(17):
        test17()

def main1():
    a = DynamicCircularArray.fromArray([0])
    for i in range(100000):
        a.addToFront(i)
    print(a.capacity)
    for i in range(100000):
        a.setAtIndex(i,i)
    print(a.capacity)
    for i in range(100000):
        a.removeFromFront()
    print(a.capacity)
    for i in range(100000):
        a.addToBack(i)
    print(a.capacity)
    for i in range(100000):
        a.removeFromBack()
    print(a.capacity)
    a.display()
    

if __name__ == "__main__":
    main1()
