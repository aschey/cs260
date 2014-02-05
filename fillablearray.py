################################################
# fillablearray.py
#
# Creates the fillable array class
#
# Author: Austin Schey
#
# Based on the outline creates by Dr. John Lusth
# 01/13/2014
################################################

import testtemplate as t
import sys

class FillableArray(object):
    def __init__(self, capacity):
        if capacity < 0:
            raise IndexError("the capacity must be a positive integer")
        # stores the values of the array
        self.store = [None] * capacity
        # max number of elements
        self.capacity = capacity
        # how many elements there currently are
        self.size = 0

    def addToFront(self, value):
        """
        adds the specified value to the front of the array
        """
        if self.isFull():
            raise IndexError("the array is full")
        # move all the values up one slot
        for i in range(self.size, 0, -1):
            self.store[i] = self.store[i-1]
        self.store[0] = value
        self.size += 1

    def removeFromFront(self):
        """
        removes the first value in the array
        """
        if self.isEmpty():
            raise IndexError("the array is empty")
        # move all the values down one slot
        for i in range(self.size-1):
            self.store[i] = self.store[i+1]
        self.size -= 1

    def addToBack(self, value):
        """
        adds the specified value to the end of the array
        """
        if self.isFull():
            raise indexError("the array is full")
        self.store[self.size] = value
        self.size += 1

    def removeFromBack(self):
        """
        removes the last value in the array
        """
        if self.isEmpty():
            raise IndexError("the array is empty")
        # no need to remove anything because decrementing the size causes the last
        # value to be ignored
        self.size -= 1

    def get(self, index):
        """
        returns the value at the specified index
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        return self.store[index]

    def setAtIndex(self, index, value):
        """
        updates the index to reflect the given value
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        self.store[index] = value

    def insertAtIndex(self, index, value):
        """
        inserts the value at the index, moving other values out of the way
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        # move values up one to make room
        for i in range(self.size, index, -1):
            self.store[i] = self.store[i-1]
        self.store[index] = value
        self.size += 1

    def removeFromIndex(self, index):
        """
        removes the value at the specified index
        """
        if self.isEmpty():
            raise IndexError("the array is empty")
        if index >= self.size:
            raise IndexError("index out of bounds")
        for i in range(index, self.size):
            self.store[i] = self.store[i+1]
        self.size -= 1

    def find(self, value):
        """
        searches the array for the given value
        returns None if not found
        """
        for i in range(self.size):
            if self.store[i] == value:
                return i
        return None

    def rfind(self, value):
        """
        searches the array for the given value, starting from the right
        returns None if not found
        """
        for i in range(self.size-1, -1, -1):
            if self.store[i] == value:
                return i
        return None

    def findAll(self, value):
        """
        searches the array and returns all instances of the given value
        returns an empty array if not found
        """
        indeces = [None] * self.size
        start = 0
        for i in range(self.size):
            if self.store[i] == value:
                indeces[start] = i
                start += 1
        return indeces[:start]

    def toArray(self):
        """
        returns a simple array representation of the FillableArray
        """
        array = [None] * self.size
        for i in range(self.size):
            array[i] = self.get(i)
        return array

    def display(self):
        """
        prints out the array
        """
        print(self.toArray())

    def isEmpty(self):
        """
        returns True if the array is empty
        """
        return self.size == 0

    def isFull(self):
        """
        returns True if the array is full
        """
        return self.size == self.capacity

def main():
    t.setSleepTime(0)
    t.setStopOnInput()

    fArray = FillableArray(10)
    fArray.addToFront(1)
    fArray.addToFront(5)
    fArray.addToFront(7)
    fArray.addToBack(3)
    fArray.addToBack(5)
    fArray.addToFront(2)
    
    def test1():
        t.template(1, "addToFront and addToBack", fArray.toArray(),[2,7,5,1,3,5])
    if t.toPrint(1):
        test1()

    fArray.removeFromBack()
    fArray.removeFromBack()
    fArray.removeFromFront()
    fArray.removeFromFront()
    fArray.removeFromBack()

    def test2():
        t.template(2, "removeFromFront and removeFromBack", fArray.toArray(), [5])
    if t.toPrint(2):
        test2()

    fArray.addToBack(4)
    fArray.addToFront(9)
    fArray.addToFront(3)
    fArray.addToBack(3)

    def test3():
        t.template(3, "get", fArray.get(2), 5)
    if t.toPrint(3):
        test3()
    
    fArray.setAtIndex(3, 10)

    def test4():
        t.template(4, "setAtIndex", fArray.toArray(), [3,9,5,10,3])
    if t.toPrint(4):
        test4()

    def test5():
        fArray = FillableArray(10)
        fArray.setAtIndex(0, 3)
        t.template(5, "setAtIndex on empty array", fArray.toArray(), [3])
    #if t.toPrint(5):
    #    test5()

    fArray.addToBack(10)

    def test6():
        t.template(6, "find", fArray.find(10), 3)
    if t.toPrint(6):
        test6()

    def test7():
        t.template(7, "rfind", fArray.rfind(10), 5)
    if t.toPrint(7):
        test7()

    def test8():
        t.template(8, "findAll", fArray.findAll(10), [3,5])
    if t.toPrint(8):
        test8()

    def test9():
        t.template(9, "toArray", fArray.toArray(), [3,9,5,10,3,10])
    if t.toPrint(9):
        test9()

    def test10():
        t.errorTemplate(10, AssertionError, "constructor", FillableArray, -1)
    if t.toPrint(10):
        test10()

    fArray.addToFront(2)
    fArray.addToBack(3)
    fArray.addToFront(1)
    fArray.addToBack(5)

    def test11():
        t.errorTemplate(11, AssertionError, "addToFront", fArray.addToFront, 0)
    if t.toPrint(11):
        test11()

    def test12():
        t.errorTemplate(12, AssertionError, "addToBack", fArray.addToBack, 0)
    if t.toPrint(12):
        test12()

    for i in range(10):
        fArray.removeFromFront()

    def test13():
        t.errorTemplate(13, AssertionError, "removeFromFront", fArray.removeFromFront)
    if t.toPrint(13):
        test13()

    def test14():
        t.errorTemplate(14, AssertionError, "removeFromBack", fArray.removeFromBack)
    if t.toPrint(14):
        test14()

    def test15():
        t.errorTemplate(15, AssertionError, "get on empty array", fArray.get, 0)
    if t.toPrint(15):
        test15()

    fArray.addToFront(5)

    def test16():
        t.errorTemplate(16, AssertionError, "get", fArray.get, 1)
    if t.toPrint(16):
        test16()
    
    def test17():
        t.errorTemplate(17, AssertionError, "get with index greater than capacity", \
                fArray.get, 10)
    if t.toPrint(17):
        test17()

    def test18():
        t.errorTemplate(18, AssertionError, "set", fArray.setAtIndex, 3, 9)
    if t.toPrint(18):
        test18()

    fArray.insertAtIndex(1,9)
    fArray.insertAtIndex(1,10)
    fArray.insertAtIndex(0,3)
    fArray.insertAtIndex(4,5)

    def test19():
        t.template(19, "insertAtIndex", fArray.toArray(), [3,5,10,9,5])
    if t.toPrint(19):
        test19()

    fArray.removeFromFront()
    fArray.removeFromBack()

    fArray = FillableArray(1000)

    for i in range(1000):
        fArray.addToFront(i)
    for i in range(1000):
        fArray.removeFromFront()
    for i in range(1000):
        fArray.addToBack(i)
    for i in range(1000):
        fArray.removeFromBack()
    for i in range(1000):
        fArray.addToFront(i)
    for i in range(1000):
        fArray.removeFromBack()
    for i in range(1000):
        fArray.addToBack(i)
    for i in range(1000):
        fArray.removeFromFront()

    def test20():
        t.template(20, "addition and subtraction of large input sizes", 
                fArray.toArray(), [])
    if t.toPrint(20):
        test20()

    for i in range(10):
        fArray.addToBack(i)

    fArray.removeFromIndex(0)
    fArray.removeFromIndex(0)
    fArray.removeFromIndex(7)

    def test21():
        t.template(21, "removeFromIndex", fArray.toArray(), [2,3,4,5,6,7,8])
    if t.toPrint(21):
        test21()


if __name__ == "__main__":
    main()
