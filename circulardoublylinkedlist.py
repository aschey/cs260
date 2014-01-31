from node import Node
class CircularDoublyLinkedList(object):
    def __init__(self):
        self.head = Node(None, None, None)
        self.size = 0
    
    def addToFront(self, value):
        """
        adds the node to the front of the list
        """
        nextNode = Node(value, self.head.getNext(), self.head)
        if self.size > 0:
            # set the node before the current next node
            self.head.getNext().setPrev(nextNode)
        else:
            # set the node as both the next and previous node because there are
            # no other nodes to be the previous
            self.head.setPrev(nextNode)
        # set the node right after the head
        self.head.setNext(nextNode)
        self.size += 1

    def addToBack(self, value):
        """
        adds the node to the back of the list
        """
        if self.size == 0:
            # add to front must be used because there is no current previous node
            self.addToFront(value)
        else:
            nextNode = Node(value, self.head, self.head.getPrev())
            self.head.getPrev().setNext(nextNode)
            self.head.setPrev(nextNode)
            self.size += 1

    def removeFromFront(self):
        """
        removes the node from the front of the list
        """
        if self.size == 0:
            raise IndexError("the list is empty")
        newNext = self.head.getNext().getNext()
        newNext.setPrev(self.head)
        self.head.setNext(newNext)
        self.size -= 1

    def removeFromBack(self):
        """
        removes the node from the back of the list
        """
        if self.size == 0:
            raise IndexError("the list is empty")
        newPrev = self.head.getPrev().getPrev()
        newPrev.setNext(self.head)
        self.head.setPrev(newPrev)
        self.size -= 1

    def insertAtIndex(self, index, value):
        """
        inserts the node at the specified index
        """
        if index >= self.size:
            raise IndexError("index out of bounds")
        current = self._traverse(index)
        nextNode = Node(value, current.getNext(), current)
        current.getNext().setPrev(nextNode)
        current.setNext(nextNode)
        self.size += 1

    def removeFromIndex(self, index):
        """
        removes the node at the specified index
        """
        if self.size == 0:
            raise IndexError("the list is empty")
        if index < 0 or index >= self.size:
            raise IndexError("index out of bounds")
        current = self._traverse(index)
        newNext = current.getNext().getNext()
        newNext.setPrev(current)
        current.setNext(newNext)
        self.size -= 1
    
    def get(self, index):
        """
        returns the value that the node contains at the specified index
        """
        if index >= self.size or index < 0:
            raise IndexError("Index out of bounds")
        current = self._traverse(index+1)
        return current.getValue()

    def display(self):
        """
        displays the whole list
        """
        values = []
        current = self.head.getNext()
        for i in range(self.size):
            values.append(current.getValue())
            current = current.getNext()
        print(values)

    def revDisplay(self):
        """
        prints the list in reverse
        """
        values = []
        current = self.head.getPrev()
        for i in range(self.size):
            values.append(current.getValue())
            current = current.getPrev()
        print(values)

    def getSize(self):
        """
        returns the size of the list
        """
        return self.size

    def isEmpty(self):
        """
        returns True if the list is empty
        """
        return self.size == 0

    def _traverse(self, steps):
        """
        steps through the list and returns the node there
        """
        current = self.head
        if steps / self.size < 0.5:
            for i in range(steps):
                current = current.getNext()
        else:
            for i in range(self.size-steps+1):
                current = current.getPrev()
        return current

def main():
    a = CircularDoublyLinkedList()
    a.addToBack(1)
    a.addToFront(1)
    a.addToFront(2)
    a.addToFront(3)
    a.addToBack(4)
    a.addToBack(5)
    a.addToFront(6)
    a.addToBack(3) #63211453
    a.removeFromFront() #3211453
    a.removeFromBack() #321145
    a.removeFromBack() #32114
    a.removeFromFront() #2114
    a.insertAtIndex(0, 1) #12114
    a.insertAtIndex(1, 5) #152114
    a.removeFromIndex(0) #52114
    a.removeFromIndex(4) #5211
    a.insertAtIndex(1, 0) #50211
    a.removeFromIndex(3) #5021
    a.display()
    a.revDisplay()
    print(a.get(0))
    print(a.get(1))
    print(a.get(2))
    print(a.get(3))
    for i in range(100000):
        a.addToBack(i)
    for i in range(100000):
        a.removeFromBack()
    for i in range(100000):
        a.addToFront(i)
    for i in range(100000):
        a.removeFromFront()

if __name__ == "__main__":
    main()
