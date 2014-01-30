class Node(object):
    def __init__(self, value, nextNode, prevNode = None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.nextNode

    def getPrev(self):
        return self.prevNode

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def setPrev(self, prevNode):
        self.prevNode = prevNode

def main():
    a = Node(1, None)
    b = Node(2, a)
    print(b.getValue())
    print(b.getNext().getValue())

if __name__ == "__main__":
    main()
