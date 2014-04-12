class BinaryNode(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent
    
    def setValue(self, value):
        self.value = value

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setParent(self, node):
        self.parent = node

    def isLeftChild(self):
        if self.parent == None:
            return False
        return self.parent.left == self

    def isRightChild(self):
        if self.parent == None:
            return False
        return self.parent.right == self

    def hasChildren(self):
        return self.left != None or self.right != None

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):   
        return self.value > other.value
