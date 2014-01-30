from dynamiccirculararray import DynamicCircularArray
import stackmain
class StackDCA(object):
    def __init__(self, capacity):
        self.store = DynamicCircularArray(capacity)

    def push(self, value):
        self.store.addToBack(value)

    def pop(self):
        value = self.peek()
        self.store.removeFromBack()
        return value

    def peek(self):
        index = self.store.getSize() - 1
        return self.store.get(index)

def main():
    stackmain.main()

if __name__ == "__main__":
    main()
