from singlylinkedlist import SinglyLinkedList

class StackSLL(object):
    def __init__(self):
        self.store = SinglyLinkedList()

    def push(self, value):
        """
        adds the value to the front of the list
        """
        self.store.addToFront(value)

    def pop(self):
        """
        removes the value from the front of the list and returns it
        """
        value = self.peek()
        self.store.removeFromFront()
        return value

    def peek(self):
        """
        returns the next value to be popped
        """
        return self.store.get(0)

    def isEmpty(self):
        """
        returns True if the value is empty
        """
        return self.store.isEmpty()
def main():
    stackmain.main()
if __name__ == "__main__":
    main()
