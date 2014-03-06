from binarynode import BinaryNode
from queuecdll import QueueCDLL
from queuesll import QueueSLL
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.minVal = None
        self.maxVal = None

    def insert(self, value):
        n = BinaryNode(value)
        if self.root == None:
            self.root = n
            self.maxVal = value
            self.minVal = value
        else:
            self._insertHelper(self.root, n)
        if value > self.maxVal:
            self.maxVal = value
        if value < self.minVal:
            self.minVal = value
    
    def _insertHelper(self, current, n):
        if n.getValue() < current.getValue():
            if current.getLeft() == None:
                current.setLeft(n)
                n.setParent(current)
            else:
                self._insertHelper(current.getLeft(), n)
        else:
            if current.getRight() == None:
                current.setRight(n)
                n.setParent(current)
            else:
                self._insertHelper(current.getRight(), n)

    def find(self, value):
        current = self.root
        while current != None:
            if current.getValue() == value:
                return current
            elif value < current.getValue():
                current = current.getLeft()
            else:
                current = current.getRight()


    def findRec(self, value):
        return self._findRecHelper(value, self.root)

    def _findRecHelper(self, value, current):
        if current == None or current.getValue() == value:
            return current
        elif value < current.getValue():
            return self._findRecHelper(value, current.getLeft())
        else:
            return self._findRecHelper(value, current.getRight())

    def delete(self, value):
        return self._deleteRec(self.find(value))

    def _deleteRec(self, delNode):
        left = delNode.getLeft()
        right = delNode.getRight()
        parent = delNode.getParent()
        if left == None and right == None:
            if parent.getValue() > delNode.getValue():
                parent.setLeft(None)
            else:
                parent.setRight(None)
        elif left == None:
            parent.setRight(right)
        elif right == None:
            parent.setLeft(left)
        else:
            replaceNode = self._findMin(right)
            self.replace(delNode, replaceNode)
            self.delete(replaceNode.getValue())

    def replace(self, oldVal, newVal):
        oldNode = self.find(oldVal)
        newNode = BinaryNode(newVal)
        if oldNode == self.root:
            self.root = newNode
        newNode.setLeft(oldNode.getLeft())
        newNode.setRight(oldNode.getRight())
        newNode.setParent(oldNode.getParent())
        oldNode.setLeft(None)
        oldNode.setRight(None)
        oldNode.setParent(None)

    def printInOrder(self):
        return self._printInOrderRec(self.root)

    def _printInOrderRec(self, current):
        if current != None:
            #print(node.getValue())
            self._printInOrderRec(current.getLeft())
            print(current.getValue())
            self._printInOrderRec(current.getRight())
            #print(node.getValue())

    def levelOrderTraverse(self):
        queue = QueueSLL()
        queue.enqueue(self.root)
        vals = []
        while not queue.isEmpty():
            current = queue.dequeue()
            vals.append(current)
            if current.getLeft() != None:
                queue.enqueue(current.getLeft())
            if current.getRight() != None:
                queue.enqueue(current.getRight())
        return vals

    def testCorrectness(self):
        return self._testCorrectnessRec(self.root, self.minVal, self.maxVal)

    def _testCorrectnessRec(self, current, minVal, maxVal):
        if current == None:
            return True
        if current.getValue() < minVal or current.getValue() > maxVal:
            return False
        return self._testCorrectnessRec(current.getLeft(), minVal, 
                current.getValue()-1) and self._testCorrectnessRec(current.getRight(), 
                        current.getValue()+1, maxVal)

    def getRoot(self):
        return self.root

def main():
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    bst.insert(7)
    bst.insert(5)
    bst.insert(8)
    #bst.replace(3, 5)
    a = bst.levelOrderTraverse()
    for i in a:
        print(i.getValue())
    #print(bst.find(3))
    #bst.printInOrder()
    #bst.delete(4)
    #print(bst.testCorrectness())
    #a = bst._findMin(bst.root.getRight())
    #print(a.getValue())
    #bst.printInOrder(bst.root)
    #print(bst.root.getLeft().getLeft().getValue())
main()
