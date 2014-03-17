from binarynode import BinaryNode
from queuesll import QueueSLL
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, n):
        """
        inserts a node with value n into the tree
        """
        node = BinaryNode(n)
        value = node.getValue()
        # use the first value inserted as the root
        if self.root == None:
            self.root = node
        else:
            self._insertRec(self.root, node)
    
    def _insertRec(self, current, node):
        """
        recursive helper for insert
        """
        if node.getValue() < current.getValue():
            if current.getLeft() == None:
                # we've reached the first empty slot where the node will fit
                current.setLeft(node)
                node.setParent(current)
            else:
                self._insertRec(current.getLeft(), node)
        else:
            if current.getRight() == None:
                current.setRight(node)
                node.setParent(current)
            else:
                self._insertRec(current.getRight(), node)

    def find(self, value):
        """
        searches for the first node with the given value
        """
        return self._findRec(value, self.root)

    def _findRec(self, value, current):
        """
        recursive helper for find
        """
        if current == None or current.getValue() == value:
            return current
        if value < current.getValue():
            return self._findRec(value, current.getLeft())
        else:
            return self._findRec(value, current.getRight())

    def bruteForceFind(self, value):
        return self._bruteForceFindRec(value, self.root)

    def _bruteForceFindRec(self, value, current):
        if current.getValue() == value:
            return current
        if current.getLeft() != None:
            return self._bruteForceFindRec(value, current.getLeft())
        if current.getRight() != None:
            return self._bruteForceFindRec(value, current.getRight())

    def delete(self, delNode):
        """
        removes the node from the tree
        """
        if delNode == None:
            raise ValueError("Node is not in the tree")
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
        """
        finds the smallest value in the subtree, starting at the right child
        of current
        """
        if current.getRight() != None:
            return self._getSuccessorRec(current.getRight())

    def _getSuccessorRec(self, current):
        """
        recursive helper for getSuccessor
        """
        if current.getLeft() != None:
            return self._getSuccessorRec(current.getLeft())
        else:
            return current

    def _getPredecessor(self, current):
        """
        finds the largest value in the subtree, starting at the left child
        of current
        """
        if current.getLeft() != None:
            return self._getPredecessorRec(current.getLeft())
    
    def _getPredecessorRec(self, current):
        """
        recursive helper for getPredecessor
        """
        if current.getRight() != None:
            return self._getPredecessorRec(current.getRight())
        else:
            return current


    def replace(self, oldNode, newNode):
        """
        replaces oldNode with newNode
        """
        if oldNode == None:
            raise ValueError("Node is not in the tree")

        if oldNode == self.root:
            self.root = newNode
        if oldNode.getLeft() != None:
            oldNode.getLeft().setParent(newNode)
        if oldNode.getRight() != None:
            oldNode.getRight().setParent(newNode)
        if oldNode.getParent() != None:
            if oldNode.isLeftChild():
                oldNode.getParent().setLeft(newNode)
            else:
                oldNode.getParent().setRight(newNode)
        newNode.setLeft(oldNode.getLeft())
        newNode.setRight(oldNode.getRight())
        newNode.setParent(oldNode.getParent())
        oldNode.setLeft(None)
        oldNode.setRight(None)
        oldNode.setParent(None)

    def printInOrder(self):
        """
        prints the nodes in order from least to greatest
        """
        return self._printInOrderRec(self.root)

    def _printInOrderRec(self, current):
        """
        recursive helper for printInOrder
        """
        if current != None:
            self._printInOrderRec(current.getLeft())
            print(current.getValue())
            self._printInOrderRec(current.getRight())

    def levelOrderTraverse(self):
        """
        returns an array of all the nodes in level order
        """
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

    def isCorrect(self):
        """
        returns the first node that is out of place in the tree
        """
        return self._getIncorrectNodeRec(self.root, self.root.getValue(),
                self.root.getValue())

    def _isCorrectRec(self, current, minVal, maxVal):
        """
        recursive helper for getIncorrectNode
        """
        if current == None:
            return True
        if current.getValue() < minVal or current.getValue() > maxVal:
            return False
        return self._getIncorrectNodeRec(current.getLeft(), minVal, 
                current.getValue()-1) and \
                        self._getIncorrectNodeRec(current.getRight(), 
                                current.getValue()+1, maxVal)

    def findMin(self):
        """
        returns the smallest value in the tree
        """
        return self._findMinRec(self.root)
    
    def _findMinRec(self, current):
        """
        recursive helper for findMin
        """
        if current.getLeft() != None:
            return self._findMinRec(current.getLeft())
        else:
            return current.getValue()

    def findMax(self):
        """
        returns the maximum value in the tree
        """
        return self._findMaxRec(self.root)

    def _findMaxRec(self, current):
        """
        recursive helper for findMax
        """
        if current.getRight() != None:
            return self._findMaxRec(current.getRight())
        return current.getValue()
    
    def correct(self):
        """
        puts any incorrect nodes in their correct place
        """
        while True:
            offender = self.getIncorrectNode()
            print(offender)
            if offender == None:
                break
            self.delete(offender)
            self.insert(offender.getValue())

    def rotate(self, current):
        parent = current.getParent()
        if parent == None:
            raise ValueError("cannot rotate root element")
        grandparent = parent.getParent()
        # right rotation
        if current == parent.getLeft():
            parent.setLeft(current.getRight())
            current.setRight(parent)
            parent.setParent(current)
        # left rotation
        else:
            parent.setRight(current.getLeft())
            if parent.getRight() != None:
                parent.getRight().setParent(parent)
            current.setLeft(parent)
            parent.setParent(current)
        if grandparent == None:
            self.root = current
        elif parent.isLeftChild():
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
    bst.insert(8)
    bst.insert(9)
    bst.insert(3)
if __name__ == "__main__":
    main()
