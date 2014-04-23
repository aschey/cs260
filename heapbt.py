from binarytree import BinaryTree
from binarynode import BinaryNode
from queuesll import QueueSLL
from stacksll import StackSLL
class HeapBT(object):
    def __init__(self):
        self.store = BinaryTree()
        # used to access each node in reverse order for the build heap operation
        self.stack = StackSLL()

    def readData(self, data):
        """
        reads data from a queue and inserts it into the heap
        """
        queue = QueueSLL()
        parent = None
        i = 1
        while not data.isEmpty():
            node = data.dequeue()
            # the parent changes every other leaf
            if i % 2 == 0:
                parent = queue.dequeue()
            queue.enqueue(node)
            self._addNode(node, parent)
            i += 1

    def _addNode(self, node, parent):
        """
        adds the node to the heap
        """
        self.store.add(node, parent)
        self.stack.push(node)

    def heapify(self, current):
        """
        makes the parent node and its children have the heap property
        """
        swapNode = self.store.getMinChild(current)
        if swapNode != None:
            # swap the min child with the parent
            self.store.swapValues(swapNode, current)
            # continue down the tree while current has at least one child
            if swapNode.getLeft() != None or swapNode.getRight() != None:
                self.heapify(swapNode)

    def buildHeap(self):
        """
        makes the entire tree into a heap
        """
        if self.stack.isEmpty():
            raise ValueError("The tree is empty or the heap has already been built")
        i = 0
        while True:
            current = self.stack.pop()
            # continue until the root is reached
            if current.getParent() == None:
                break
            # heapify every other node's parent to prevent duplicate calls
            if i % 2 == 0:
                self.heapify(current.getParent())
            i += 1

    def extract(self):
        """
        returns the root node and restores the heap property on the rest of the tree
        """
        root = self.store.getRoot()
        # if root is None, the tree is empty
        if root == None:
            return
        pruneNode = self.store.getLastNode()
        # remove the last node
        self.store.prune(pruneNode)
        # swap the first and last values
        #self.store.swapValues(root, pruneNode)
        root.setValue(pruneNode.getValue())
        # put the new root value in its proper place
        self.heapify(root)
        return pruneNode.getValue()

    def sort(self):
        """
        performs a heapsort
        """
        queue = QueueSLL()
        while True:
            minVal = self.extract()
            if minVal == None:
                break
            queue.enqueue(minVal)
        return queue

    def isCorrect(self):
        """
        returns True if the tree is a heap
        """
        queue = QueueSLL()
        queue.enqueue(self.store.getRoot())
        while not queue.isEmpty():
            current = queue.dequeue()
            incorrectNode = self.store.getMinChild(current)
            # if any node has a min child, the tree is not a heap
            if self.store.getMinChild(current) != None:
                return False
            left = current.getLeft()
            if left != None:
                queue.enqueue(left)
            right = current.getRight()
            if right != None:
                queue.enqueue(right)
        return True

    def peek(self):
        """
        returns the value at the root of the heap
        """
        return self.store.getRoot()

    def isEmpty(self):
        """
        returns true if the heap is empty
        """
        return self.store.getRoot() == None 

def main():
    heap = HeapBT()
    queue = QueueSLL()
    for i in range(10):
        queue.enqueue(BinaryNode(i))
    heap.readData(queue)
    heap.buildHeap()
    queue = heap.sort()
    for i in range(10):
        print(queue.dequeue())
    #while not heap.store.store.isEmpty():
    #       print(heap.store.store.dequeue().value)
    # heap.buildHeap()
    # heap.insert(2)
    # #heap.insert(10)
    # #heap.insert(1)
    # stack = heap.store.levelOrderTraverse()
    # while not stack.isEmpty():
    #       print(stack.pop().getValue())
    # print(heap.isCorrect())
    # #while not queue.isEmpty():
    # #     print(queue.dequeue())
    

if __name__ == '__main__':
    main()
