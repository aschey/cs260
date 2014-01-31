from node import Node
class SinglyLinkedList(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = None
        self.size = 0

    def addToFront(self, value):
        """
        adds the node to the front of the list
        """
        nextNode = Node(value, self.head.getNext())
        # the head is the dummy node, this will be the one that immediately follows
        self.head.setNext(nextNode)
        if self.isEmpty():
            # no tail has been set yet, so the first real node will serve as the tail
            self.tail = nextNode
        self.size += 1

    def addToBack(self, value):
        """
        adds the node to the back of the list
        """
        if self.isEmpty():
            # no tail has been set yet, so the assignment in addToFront must be used
            self.addToFront(value)
        else:
            nextNode = Node(value, None)
            # add the node after the old tail
            self.tail.setNext(nextNode)
            # update the tail to reflect the new end (the node just created)
            self.tail = nextNode
            self.size += 1
    
    def removeFromFront(self):
        """
        removes the node from the front of the list
        """
        newNext = self.head.getNext().getNext()
        # remove the first real node in the list
        self.head.setNext(newNext)
        self.size -= 1
        self._tailRemoveCheck()

    def removeFromBack(self):
        """
        removes the node from the back of the list
        """
        if self.size == 1:
            self.removeFromFront()
        else:
            # get the second to last value
            current = self._traverse(self.size-1)
            # remove the last one
            current.setNext(None)
            # update the tail to reflect the new last value
            self.tail = current
            self.size -= 1

    def insertAtIndex(self, index, value):
        """
        inserts the node at the specified index
        """
        current = self._traverse(index)
        nextNode = Node(value, current.getNext())
        # set the node after the node at index-1
        current.setNext(nextNode)
        self.size += 1

    def removeFromIndex(self, index):
        """
        removes the node from the specified index
        """
        if index >= self.size:
            raise IndexError("index out of bounds")
        if self.size == 1:
            self.removeFromFront()
        elif self.size == 2 and index == 1:
            self.removeFromBack()
        else:
            current = self._traverse(index)
            # get the node two nodes after the one to remove
            newNext = current.getNext().getNext()
            # set that node as the new nextNode to remove the one before that
            current.setNext(newNext)
            self.size -= 1

    def get(self, index):
        """
        returns the node at the specified index
        """
        if index < 0  or index >= self.size:
            raise IndexError("index out of bounds")
        # add 1 to the index to account for the dummy node
        current = self._traverse(index+1)
        return current.getValue()

    def find(self, value):
        """
        returns the first index that contains the specified value
        """
        current = self.head.getNext()
        for i in range(self.size):
            if current.getValue() == value:
                return i
            else:
                current = current.getNext()

    def display(self):
        """
        prints the list
        """
        values = []
        current = self.head
        for i in range(self.size):
            current = current.getNext()
            values.append(current.getValue())
        print(values)

    def isEmpty(self):
        """
        returns True if the list is empty
        """
        return self.size == 0

    def getSize(self):
        """
        returns the size of the list
        """
        return self.size
    
    def _traverse(self, steps):
        """
        moves down the list by the specified number of steps
        """
        current = self.head
        for i in range(steps):
            current = current.getNext()
        return current

    def _tailRemoveCheck(self):
        if self.isEmpty():
            self.tail = None

def main():
    a = SinglyLinkedList() 
    a.addToBack(1)
    a.addToFront(1)
    a.addToFront(2)
    a.addToBack(3)
    a.addToBack(4)
    a.addToFront(5)
    a.removeFromFront()
    a.removeFromFront()
    a.removeFromFront()
    a.removeFromFront()
    a.removeFromFront()
    a.addToFront(1)
    a.addToFront(2)
    a.removeFromBack()
    a.addToBack(1)
    a.insertAtIndex(1,3)
    a.insertAtIndex(1,4)
    a.display()
    a.removeFromIndex(0)
    a.display()
    a.removeFromIndex(1)
    a.display()
    a.removeFromIndex(2)
    a.display()
    a.removeFromIndex(1)
    #a.display()
    a = SinglyLinkedList()
    a.addToFront(1)
    a.addToBack(2)
    a.removeFromIndex(1)
    print(a.tail.getValue())
    #a.display()
    
    
    

if __name__ == "__main__":
    main()
