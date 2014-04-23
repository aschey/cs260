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
        rootNode = data.dequeue()
        self._addNode(rootNode, None)
        parent = rootNode
        while not data.isEmpty():
            node = data.dequeue()
            if parent.getRight() != None:
                parent = queue.dequeue()
            queue.enqueue(node)
            self._addNode(node, parent)

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
        # save the root value before it gets overwritten
        rootValue = root.getValue()
        pruneNode = self.store.getLastNode()
        root.setValue(pruneNode.getValue())
        self.store.prune(pruneNode)
        self.heapify(root)
        return rootValue

    def sort(self):
        """
        performs a heapsort
        """
        queue = QueueSLL()
        while self.store.getRoot() != None:
            minVal = self.extract()
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
    pass

if __name__ == '__main__':
    main()
