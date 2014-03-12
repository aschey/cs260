from binarynode import BinaryNode
from queuesll import QueueSLL
import copy
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.incorrectNode = None

    def insert(self, n):
        node = BinaryNode(n)
        value = node.getValue()
        if self.root == None:
            self.root = node
            self.maxVal = value
            self.minVal = value
        else:
            self._insertHelper(self.root, node)
    
    def _insertHelper(self, current, node):
        if node.getValue() < current.getValue():
            if current.getLeft() == None:
                current.setLeft(node)
                node.setParent(current)
            else:
                self._insertHelper(current.getLeft(), node)
        else:
            if current.getRight() == None:
                current.setRight(node)
                node.setParent(current)
            else:
                self._insertHelper(current.getRight(), node)

    def find(self, value):
        current = self.root
        while current != None:
            if current.getValue() == value:
                return current
            if value < current.getValue():
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

    def delete(self, delNode):
        left = delNode.getLeft()
        right = delNode.getRight()
        parent = delNode.getParent()
        if left == None and right == None:
            if parent == None:
                self.root = None
            elif delNode.isLeftChild():
                parent.setLeft(None)
            else:
                parent.setRight(None)
        else:
            predecessor = self._getPredecessor(delNode)
            if predecessor != None:
                pCopy = BinaryNode(predecessor.getValue())
                self.replace(delNode, pCopy)
                self.delete(predecessor)
            else:
                successor = self._getSuccessor(delNode)
                sCopy = BinaryNode(successor.getValue())
                self.replace(delNode, sCopy)
                self.delete(successor)

    def _getSuccessor(self, current):
        if current.getRight() != None:
            return self._getSuccessorRec(current.getRight())

    def _getSuccessorRec(self, current):
        """
        finds the smallest value in the subtree
        """
        if current.getLeft() != None:
            return self._getSuccessorRec(current.getLeft())
        else:
            return current

    def _getPredecessor(self, current):
        if current.getLeft() != None:
            return self._getPredecessorRec(current.getLeft())
    
    def _getPredecessorRec(self, current):
        """
        finds the largest value in the subtree
        """
        if current.getRight() != None:
            return self._getPredecessorRec(current.getRight())
        else:
            return current


    def replace(self, oldNode, newNode):
        if oldNode == self.root:
            self.root = newNode
        if oldNode.getLeft() != None:
            oldNode.getLeft().setParent(newNode)
        if oldNode.getRight() != None:
            oldNode.getRight().setParent(newNode)
        if oldNode.getParent() != None:
            if newNode.getValue() < oldNode.getParent().getValue():
                oldNode.getParent().setLeft(newNode)
            else:
                oldNode.getParent().setRight(newNode)
        newNode.setLeft(oldNode.getLeft())
        newNode.setRight(oldNode.getRight())
        newNode.setParent(oldNode.getParent())
        oldNode.setLeft(None)
        oldNode.setRight(None)
        oldNode.setParent(None)

    def _findMin(self, current):
        if current.getLeft() != None:
            self._findMin(current.getLeft())
        return current

    def printInOrder(self):
        return self._printInOrderRec(self.root)

    def _printInOrderRec(self, current):
        if current != None:
            self._printInOrderRec(current.getLeft())
            print(current.getValue())
            self._printInOrderRec(current.getRight())

    def levelOrderTraverse(self):
        queue = QueueSLL()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            current = queue.dequeue()
            vals.append(current)
            if current.getLeft() != None:
                queue.enqueue(current.getLeft())
            if current.getRight() != None:
                queue.enqueue(current.getRight())
        return vals

    def getIncorrectNode(self):
        return self._getIncorrectNodeRec(self.root, self.getMinVal(self.root),
                self.getMaxVal(self.root))

    def _getIncorrectNodeRec(self, current, minVal, maxVal):
        if current == None:
            return True
        if current.getValue() < minVal or current.getValue() > maxVal:
            self.incorrectNode = current
            return False
        return self._getIncorrectNodeRec(current.getLeft(), minVal, 
                current.getValue()-1) and \
                        self._getIncorrectNodeRec(current.getRight(), 
                        current.getValue()+1, maxVal)
    
    def getMinVal(self, current):
        if current.getLeft() != None:
            return self.getMinVal(current.getLeft())
        else:
            return current.getValue()

    def getMaxVal(self, current):
        if current.getRight() != None:
            return self.getMaxVal(current.getRight())
        else:
            return current.getValue()
    
    def correct(self):
        self.getIncorrectNode()
        if self.incorrectNode == None:
            return
        self.delete(self.incorrectNode)
        self.insert(BinaryNode(self.incorrectNode.getValue()))
        self.incorrectNode = None

    def rotate(self, current):
        parent = current.getParent()
        if parent == None:
            raise ValueError("cannot rotate root element")
        grandparent = parent.getParent()
        if current == parent.getLeft():
            parent.setLeft(current.getRight())
            current.setRight(parent)
            parent.setParent(current)
        else:
            parent.setRight(current.getLeft())
            if parent.getRight() != None:
                parent.getRight().setParent(parent)
            current.setLeft(parent)
            parent.setParent(current)
        if grandparent == None:
            self.root = current
        elif parent == grandparent.getLeft():
            grandparent.setLeft(current)
        else:
            grandparent.setRight(current)
        current.setParent(grandparent)

    def getRoot(self):
        return self.root

def main():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(5)
    bst.insert(4)
    bst.delete(bst.find(2))
    print(bst.root.right.parent.value)
if __name__ == "__main__":
    main()
