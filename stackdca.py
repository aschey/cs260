from dynamiccirculararray import DynamicCircularArray

class StackDCA(object):
    def __init__(self, capacity):
        self.store = DynamicCircularArray(capacity)

    def push(self, value):
        """
        adds the value to the back of the array
        """
        self.store.addToBack(value)

    def pop(self):
        """
        removes the value from the back of the array and returns that value
        """
        value = self.peek()
        self.store.removeFromBack()
        return value

    def peek(self):
        """
        returns the next value to be popped
        """
        index = self.store.getSize() - 1
        return self.store.get(index)

    def isEmpty(self):
        """
        returns True if the array is empty
        """
        return self.store.isEmpty()

def main():
    a = StackDCA(1)
    for i in range(100):
        a.push(i)
    for i in range(100):
        print(a.pop())
    print(a.store.getSize())
    for i in range(5):
        a.push(i)
    for i in range(5):
        print(a.pop())
        


if __name__ == "__main__":
    main()
