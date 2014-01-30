##################################################
# circulararray.py
#
# Creates the circular array class
#
# Author: Austin Schey
#
# Based on the outline created by Dr. John Lusth 
# 
# 01/12/2014
#################################################

import testtemplate as t

class CircularArray(object):
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        # an array to hold the values
        self.store = [None] * capacity
        # max number of values (length of store)
        self.capacity = capacity
        # how many values are filled
        self.size = 0
        # index of the first value
        self.startIndex = 0
        # index of the last value
        self.endIndex = 0

    def _correctIndex(self, index):
        """
        corrects the index to a valid one if it is either < 0 or >= the 
        capacity 
        """
        return (index + self.capacity) % self.capacity

    def addToFront(self, value):
        """
        adds a value to the front of the array
        """
        if self.size == self.capacity:
            raise ValueError("the array is full")
        if self.size == 0:
            # addToFront would add the element to the end of store instead of
            # the beginning
            self.addToBack(value)
        else:
            self.startIndex = self._correctIndex(self.startIndex - 1)
            self.store[self.startIndex] = value
            self.size += 1

    def addToBack(self, value):
        """
        adds a value to the back of the array
        """
        if self.size == self.capacity:
            raise ValueError("the array is full")
        self.store[self.endIndex] = value
        self.endIndex = self._correctIndex(self.endIndex + 1)
        self.size += 1

    def removeFromFront(self):
        """
        removes the first value in the array
        """
        if self.size == 0:
            raise ValueError("the array is empty")
        # changing the startIndex causes the value at the previous startIndex
        # to now be ignored
        self.startIndex = self._correctIndex(self.startIndex + 1)
        self.size -= 1

    def removeFromBack(self):
        """
        removes the last value in the array
        """
        if self.size == 0:
            raise ValueError("the array is empty")
        self.endIndex = self._correctIndex(self.endIndex - 1)
        self.size -= 1

    def get(self, index):
        """
        returns the value at the specified index
        """
        # any index greater than size will either contain None or be out of bounds
        if index < 0 or index >= self.capacity:
            raise IndexError("index out of bounds")
        if index >= self.size:
            raise IndexError("index hasn't been initialized yet")
        spot = self._correctIndex(index + self.startIndex)
        return self.store[spot]

    def setAtIndex(self, index, value):
        """
        inserts the value at the specified index
        Note: does not change the size of the array
        Note: name changed from the usual "set" because "set" is a keyword in Python
        """
        if index < 0 or index >= self.capacity:
            raise IndexError("index out of bounds")
        if index >= self.size:
            raise IndexError("index has not been initialized yet")
        spot = self._correctIndex(index + self.startIndex)
        self.store[spot] = value

    def getSize(self):
        """
        returns the size of the array
        """
        return self.size

    def find(self, value):
        """
        searches through the array to find the index of the value closest
        to the front of the arrayj
        """
        for i in range(self.size):
            if self.get(i) == value:
                return i
        return None
    
    def rfind(self, value):
        """
        same as find, but searches starting from the right
        """
        for i in range(self.size - 1, -1, -1):
            if self.get(i) == value:
                return i
        return None

    def findAll(self, value):
        """
        returns a list containing the indeces of all instances of the value
        """
        indeces = [None] * self.size
        start = 0
        for i in range(self.size):
            if self.get(i) == value:
                indeces[start] = i
                start += 1
        return indeces[:start]

    def toArray(self):
        """
        returns the circular array in the form of a normal array
        """
        array = [None] * self.size
        for i in range(self.size):
            array[i] = self.get(i)
        return array

    def display(self):
        """
        prints the circular array in the form of a normal array
        """
        print(self.toArray())

    def isEmpty(self):
        """
        returns true if no items have been added to the array, false otherwise
        """
        return self.size == 0

    def isFull(self):
        """
        returns true if the array can hold no more items, false otherwise
        """
        return self.size == self.capacity

def main():
    t.setSleepTime(0)
    t.setStopOnInput()

    cArray = CircularArray(10)

    cArray.addToFront(2)
    cArray.addToFront(10)
    cArray.addToBack(3)
    cArray.addToBack(4)
    cArray.addToFront(1)
    cArray.addToBack(4)
    cArray.addToFront(3)

    def test1():
        t.template(1, "addToFront and addToBack", cArray.toArray(), [3,1,10,2,3,4,4])
    if t.toPrint(1):
        test1()
    
    cArray.setAtIndex(0, 100)
    cArray.setAtIndex(3, 200)

    def test2():
        t.template(2, "testing setAtIndex", cArray.toArray(), [100,1,10,200,3,4,4])
    if t.toPrint(2):
        test2()

    def test3():
        t.template(3, "testing find", cArray.find(4), 5)
    if t.toPrint(3):
        test3()

    def test4():
        t.template(4, "testing find when the value isn't present",
                cArray.find(10000), None)
    if t.toPrint(4):
        test4()

    def test5():
        t.template(5, "rfind", cArray.rfind(100), 0)
    if t.toPrint(5):
        test5()

    def test6():
        t.template(6, "rfind when the value isn't present",
                cArray.rfind(10000), None)
    if t.toPrint(6):
        test6()

    def test7():
        t.template(7, "findAll", cArray.findAll(100), [0])
    if t.toPrint(7):
        test7()

    def test8():
        t.template(8, "findAll when there's more than one value", cArray.findAll(4),
                [5,6])
    if t.toPrint(8):
        test8()

    def test9():
        t.template(9, "findAll when the value isn't present", cArray.findAll(100000), [])
    if t.toPrint(9):
        test9()

    cArray.removeFromFront()
    cArray.removeFromBack()
    cArray.removeFromFront()
    cArray.removeFromBack()

    def test10():
        t.template(10, "removeFromFront and removeFromBack", cArray.toArray(),
                [10,200,3])
    if t.toPrint(10):
        test10()
    
    cArray.addToFront(20)
    cArray.removeFromFront()
    cArray.setAtIndex(2, 45)
    cArray.removeFromBack()
    cArray.addToBack(1)
    cArray.removeFromFront()
    cArray.addToFront(1)
    cArray.setAtIndex(1, 5)

    def test11():
        t.template(11, "adding and removing together", cArray.toArray(), [1,5,1])
    if t.toPrint(11):
        test11()

    def test12():
        t.template(12, "toArray", cArray.toArray(), [1,5,1])
    if t.toPrint(12):
        test12()

    def test13():
        print("testing display...")
        print("should print [1, 5, 1]")
        print("output: ", end = " ")
        cArray.display()
        print()
    if t.toPrint(13):
        test13()

    cArray.removeFromFront()
    cArray.removeFromFront()
    cArray.removeFromBack()

    def test14():
        t.template(13, "if toArray works on empty arrays", cArray.toArray(), [])
    if t.toPrint(14):
        test14()

    def test15():
        print("testing if display works on empty arrays...")
        print("should print []")
        print("output: ", end = " ")
        cArray.display()
        print()
    if t.toPrint(15):
        test15()

    def test16():
        t.template(16, "isEmpty on an empty array", cArray.isEmpty(), True)
    if t.toPrint(16):
        test16()

    cArray.addToBack(1)

    def test17():
        t.template(17, "isEmpty on a non-empty array", cArray.isEmpty(), False)
    if t.toPrint(17):
        test17()

    for i in range(9):
        cArray.addToFront(i)

    def test18():
        t.template(18, "isFull on a full array", cArray.isFull(), True)
    if t.toPrint(18):
        test18()

    cArray.removeFromBack()
    cArray.removeFromFront()

    def test19():
        t.template(19, "isFull on a non-full array", cArray.isFull(), False)
    if t.toPrint(19):
        test19()

    def test20():
        t.errorTemplate(20, AssertionError, "setAtIndex", cArray.setAtIndex, 9, 10)
    if t.toPrint(20):
        test20()

    def test21():
        t.errorTemplate(21, AssertionError, "get", cArray.get, 8)
    if t.toPrint(21):
        test21()

    cArray.addToFront(3)
    cArray.addToFront(5)

    def test22():
        t.errorTemplate(22, AssertionError, "addToFront", cArray.addToFront, 3)
    if t.toPrint(22):
        test22()

    def test23():
        t.errorTemplate(23, AssertionError, "addToBack", cArray.addToBack, 3)
    if t.toPrint(23):
        test23()

    def test24():
        t.errorTemplate(24, AssertionError, "constructor", CircularArray, -1)
    if t.toPrint(24):
        test24()

    cArray = CircularArray(100000)

    for i in range(100000):
        cArray.addToFront(i)
    for i in range(100000):
        cArray.removeFromFront()
    for i in range(100000):
        cArray.addToFront(i)
    for i in range(100000):
        cArray.removeFromBack()
    for i in range(100000):
        cArray.addToBack(i)
    for i in range(100000):
        cArray.removeFromFront()
    for i in range(100000):
        cArray.addToBack(i)
    for i in range(100000):
        cArray.removeFromBack()

    def test25():
        t.template(25, "addition and removal of large values", cArray.toArray(), [])
    if t.toPrint(25):
        test25()

if __name__ == "__main__":
    main()
