from dynamicarray import DynamicArray
from queuesll import QueueSLL
class Heap(object):
    def __init__(self, capacity):
        self.store = DynamicArray(capacity)
        self.ROOT_INDEX = 0
        self.size = 0
    
    def readData(self, data):
        """
        reads values from a queue and inputs them into a fillable array
        """
        while not data.isEmpty():
            self._addNode(data.dequeue())

    def _addNode(self, value):
        """
        adds the node to the array
        """
        self.store.addToBack(value)
        self.size += 1

    def get(self, currentIndex):
        """
        returns the value at the index
        """
        return self.store.get(currentIndex)

    def getParentIndex(self, nodeIndex):
        """
        returns the parent of the node 
        """
        # node has no parent if it is the root
        if nodeIndex > self.ROOT_INDEX:
            return (nodeIndex - 1) // 2

    def getLeftIndex(self, nodeIndex):
        """
        returns the left child of the node
        """
        leftChildIndex = nodeIndex * 2 + 1
        # don't return anything if the index is out of bounds
        if leftChildIndex < self.size:
            return leftChildIndex

    def getRightIndex(self, nodeIndex):
        """
        returns the right child of the node
        """
        rightChildIndex = nodeIndex * 2 + 2
        if rightChildIndex < self.size:
            return rightChildIndex

    def _getMaxChildIndex(self, parentIndex):
        """
        returns the smallest child of the parent node, None if there is none
        """
        #print("parentValue=",self.store.get(parentIndex))
        leftIndex = self.getLeftIndex(parentIndex)
        rightIndex = self.getRightIndex(parentIndex)
        #if leftIndex != None:
        #    print("leftValue=",self.store.get(leftIndex))
        #if rightIndex != None:
        #    print("rightValue=",self.store.get(rightIndex))
        # if the left or the right child is greater than the parent
        if self._greaterThan(leftIndex, parentIndex) or self._greaterThan(rightIndex, parentIndex):
            if rightIndex == None:
                return leftIndex
            elif self._greaterThan(rightIndex, leftIndex):
                return rightIndex
            else:
                return leftIndex
        else:
            return None

    def _greaterThan(self, index1, index2):
        """
        returns True if the value at index1 is greater than the value at index2
        The None checking for index1 is used for cases where index2 is the parent of index1
        PRECONDITION: index2 should NOT be the child of index1
        """
        return index1 != None and self.store.get(index1) > self.store.get(index2)

    def _swapValues(self, index1, index2):
        """
        swaps the values at index 1 and 2
        """
        temp = self.store.get(index1)
        self.store.setAtIndex(index1, self.store.get(index2))
        self.store.setAtIndex(index2, temp)

    def heapify(self, currentIndex):
        """
        makes the parent node and its children have the heap property
        """
        #print("current value = ", self.store.get(currentIndex))
        swapIndex = self._getMaxChildIndex(currentIndex)
        if swapIndex != None:
            #print("swap value = ", self.store.get(swapIndex))
            # swap the current value and the value of the max child
            self._swapValues(swapIndex, currentIndex)
            # recursively heapify as long as the node has one or more children
            if self.getLeftIndex(swapIndex) != None or self.getRightIndex(swapIndex) != None:
                #print("swap value = ",self.store.get(swapIndex))
                #print("parent value = ",self.store.get(currentIndex))
                self.heapify(swapIndex)
        #else:
            #print("swap value = None")
            

    def buildHeap(self):
        """
        makes the entire array into a heap
        """
        # start at the last node
        currentIndex = self.store.getSize() - 1
        while currentIndex > 0:
            # run heapify on every node except the leaves
            self.heapify(self.getParentIndex(currentIndex))
            # decrement by 2 in order to check each parent once instead of twice
            currentIndex -= 2

    def extract(self):
        """
        returns the root node and restores the heap property on the rest of the tree
        """
        rootValue = self.store.get(self.ROOT_INDEX)
        # decrement the size so already sorted nodes are ignored
        self.size -= 1
        # swap the first and last values
        #self._swapValues(self.ROOT_INDEX, self.size)
        lastNode = self.store.get(self.size)
        self.store.setAtIndex(self.ROOT_INDEX, lastNode)
        # make the new root value go to its proper place
        self.heapify(self.ROOT_INDEX)
        return rootValue

    def sort(self):
        """
        sorts the heap in ascending order
        """
        self.buildHeap()
        for i in range(self.store.getSize()):
            rootValue = self.extract()
            self.store.setAtIndex(self.size, rootValue)
        # reset the size afterwards because it goes down to zero
        self.size = self.store.getSize()
        

    def _bubbleUp(self, currentIndex):
        """
        moves the node up the tree until it is greater than the parent
        """
        parentIndex = self.getParentIndex(currentIndex)
        # if parentIndex is None, we're at the root and should stop
        if parentIndex != None and self._greaterThan(currentIndex, parentIndex):
            self._swapValues(currentIndex, parentIndex)
            self._bubbleUp(parentIndex)

    def isCorrect(self):
        """
        tests the tree for correctness using a level-order traverse
        """
        queue = QueueSLL()
        queue.enqueue(self.ROOT_INDEX)
        while not queue.isEmpty(): 
            current = queue.dequeue()
            # if a node has a child greater than it, the tree is not a heap
            if self._getMaxChildIndex(current) != None:
                return False
            lIndex = self.getLeftIndex(current)
            if lIndex != None:
                queue.enqueue(lIndex)
            rIndex = self.getRightIndex(current)
            if rIndex != None:
                queue.enqueue(rIndex)
        return True

    def insert(self, value):
        """
        inserts the node into the correct place in the heap
        """
        self._addNode(value)
        # the last node is at self.size-1
        self._bubbleUp(self.size-1)

    def peek(self):
        """
        returns the value at the root of the heap
        """
        if not self.store.isEmpty():
            return self.store.get(self.ROOT_INDEX)

    def getSize(self):
        """
        returns the number of elements in the heap
        """
        return self.store.getSize()

    def isEmpty(self):
        """
        returns true if the heap is isEmpty
        """
        return self.store.getSize() == 0

def main():
    heap = Heap(10)
    heap.readData([3,4,1,6,8,2,3,8,5])
    heap.insert(10)
    heap.insert(4)
    heap.buildHeap()
    for i in range(11):
        print(heap.store.get(i))

#if __name__ == '__main__':
#    main()
