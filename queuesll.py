from singlylinkedlist import SinglyLinkedList
import queuemain
class QueueSLL(object):
    def __init__(self):
        self.store = SinglyLinkedList()

    def enqueue(self, value):
        """
        adds the value to the back of the list
        """
        self.store.addToBack(value)

    def dequeue(self):
        """
        removes the value from the front of the list
        """
        if self.isEmpty():
            raise IndexError("the queue is empty")
        value = self.peek()
        self.store.removeFromFront()
        return value

    def peek(self):
        """
        returns the first value to be dequeued
        """
        if self.isEmpty():
            raise IndexError("the queue is empty")
        return self.store.get(0)
    
    def isEmpty(self):
        return self.store.getSize() == 0

def main():
    queuemain.main()

if __name__ == "__main__":
    main()
