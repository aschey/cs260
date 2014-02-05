from circulardoublylinkedlist import CircularDoublyLinkedList
class QueueCDLL(object):
    def __init__(self):
        self.store = CircularDoublyLinkedList()

    def enqueue(self, value):
        """
        adds the value to the back of the list
        """
        self.store.addToBack(value)

    def dequeue(self):
        """
        removes the value from the front of the list
        """
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
        return self.store.isEmpty()

def main():
    a = QueueCDLL()
    for i in range(100):
        a.enqueue(i)
    for i in range(100):
        print(a.dequeue())
    for i in range(5):
        a.enqueue(i)
    while not a.isEmpty():
        print(a.dequeue())
    

if __name__ == "__main__":
    main()
