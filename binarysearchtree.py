from binarynode import BinaryNode
from queuesll import QueueSLL
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.incorrectNode = None

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
            print("parent=",current.getParent().getValue())
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

    def delete(self, current):
        """
        removes the node from the tree
        """
        if current == None:
            raise ValueError("Node is not in the tree")
        # node is a leaf
        if current.getLeft() == None and current.getRight() == None:
            self.prune(current)
        else:
            # the largest value in the left subtree
            predecessor = self._getPredecessor(current)
            if predecessor != None:
                # replace current's value with the predecessor's value
                current.setValue(predecessor.getValue())
                # remove the duplicate value
                self.delete(predecessor)
            else:
                # the smallest value in the right subtree
                successor = self._getSuccessor(current)
                current.setValue(successor.getValue())
                self.delete(successor)

    def prune(self, current):
        """
        removes the leaf from the tree
        precondition: current MUST be a leaf
        """
        parent = current.getParent()
        # the node to delete is the root node
        if parent == None:
            self.root = None
        elif current.isLeftChild():
            parent.setLeft(None)
        else:
            parent.setRight(None)

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
        returns True if the tree has no nodes out of place
        """
        return self._isCorrectRec(self.root, float("-inf"), float("inf"))

    def _isCorrectRec(self, current, minVal, maxVal):
        """
        recursive helper for isCorrect
        """
        if current == None:
            return True
        if current.getValue() < minVal or current.getValue() > maxVal:
            self.incorrectNode = current
            return False
        return self._isCorrectRec(current.getLeft(), minVal, 
                current.getValue()-1) and self._isCorrectRec(current.getRight(),
                        current.getValue() +1, minVal)

    def getIncorrectNode(self):
        """
        returns the first node that is out of place in the tree
        """
        return self._getIncorrectNodeRec(self.root, float("-inf"),
                float("inf"))

    def _getIncorrectNodeRec(self, current, minVal, maxVal):
        """
        recursive helper for getIncorrectNode
        TODO: fix this
        """
        if current == None:
            return None
        if current.getValue() < minVal or current.getValue() > maxVal:
            return current
        if self._getIncorrectNodeRec(current.getLeft(), minVal, 
                current.getValue()-1) != None:
            print(current.getValue())
            return current.getLeft()
        if self._getIncorrectNodeRec(current.getRight(), 
                current.getValue()+1, maxVal) != None:
            return current.getRight()
    

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
        TODO: make this work
        """
        while True:
            offender = self.getIncorrectNode()
            print(offender)
            if offender == None:
                break
            self.delete(offender)
            self.insert(offender.getValue())

    def rotate(self, current):
        """
        moves the node one level closer to the root
        """
        if current == None:
            raise ValueError("node not found")
        parent = current.getParent()
        if parent == None:
            raise ValueError("cannot rotate root element")
        grandparent = parent.getParent()
        # right rotation
        # leaves current's left subtree alone
        if current.isLeftChild():
            self._setLeftChild(parent, current.getRight())
            self._setRightChild(current, parent)
        # left rotation
        # leaves current's right subtree alone
        else:
            # same as right rotation, but reversed
            self._setRightChild(parent, current.getLeft())
            self._setLeftChild(current, parent)
        # current is now at the level of its previous parent, 
        # so it is the new root if there was no grandparent
        if grandparent == None:
            self.root = current
        # update the grandparent's child to reflect the swap
        # can't use parent.isLeftChild because parent's parent has changed
        elif grandparent.getLeft() == parent:
            self._setLeftChild(grandparent, current)
        else:
            self._setRightChild(grandparent, current)

    def _setLeftChild(self, parent, child):
        """
        sets the child node as the left child of parent and updates pointers
        """
        parent.setLeft(child)
        if child != None:
            child.setParent(parent)

    def _setRightChild(self, parent, child):
        """
        sets the child node as the right child of the parent and updates pointers
        """
        parent.setRight(child)
        if child != None:
            child.setParent(parent)

    def getRoot(self):
        return self.root

def main():
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.find(1).setValue(10)
    print(bst.isCorrect())
if __name__ == "__main__":
    main()
