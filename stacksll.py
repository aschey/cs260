from singlylinkedlist import SinglyLinkedList
class StackSLL(object):
    def __init__(self):
        self.store = SinglyLinkedList()

    def push(self, value):
        self.store.addToFront(value)

    def pop(self):
        value = self.peek()
        self.store.removeFromFront()
        return value

    def peek(self):
        return self.store.get(0)

    def isEmpty(self):
        return self.store.isEmpty()
