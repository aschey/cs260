from heap import Heap
from heapbt import HeapBT
from binarynode import BinaryNode
from scanner import Scanner
import subprocess
from queuesll import QueueSLL
class TreeGraphWriter(object):
    def __init__(self, filename, heap):
        self.nodeNum = 1
        self.nullNum = 0
        self.filename = filename
        self.graph = open(filename + ".dot", "w")
        self.queue = QueueSLL()
        self.heap = heap

    def createGraph(self):
        self.graph.write("digraph {\n")
        self.graph.write("graph [ordering=\"out\"];\n")
        self.queue.enqueue(self.heap.peek())
        self.graph.write("Node0 [label=" + str(self.heap.peek().getValue()) + "];\n")
        localRootNode = 0
        while not self.queue.isEmpty():
            current = self.queue.dequeue()
            curNode = "Node" + str(localRootNode)
            self.writeToGraph(curNode, current.getLeft())
            self.writeToGraph(curNode, current.getRight())
            localRootNode += 1
        self.graph.write("}")
        self.graph.close()

    def writeToGraph(self, curNode, directionNode):
        if directionNode != None:
            nextNode = "Node" + str(self.nodeNum)
            self.nodeNum += 1
            self.graph.write(nextNode + " [label=" + str(directionNode.getValue()) + "];\n")
            self.graph.write(curNode + " -> " + nextNode + ";\n")
            self.queue.enqueue(directionNode)
        else:
            null = "Null" + str(self.nullNum)
            self.nullNum += 1
            self.graph.write(null + " [shape=point];\n")
            self.graph.write(curNode + " -> " + null + ";\n")

    def display(self):
        subprocess.call("dot -Teps " + self.filename + ".dot -o " +
                self.filename + ".eps", shell=True)
        subprocess.call("evince " + self.filename + ".eps", shell=True)

class ArrayGraphWriter(TreeGraphWriter):
    def createGraph(self):
        self.graph.write("digraph {\n")
        self.graph.write("graph [ordering=\"out\"];\n")
        self.queue.enqueue(0)
        self.graph.write("Node0 [label=" + str(self.heap.peek()) + "];\n")
        localRootNode = 0
        while not self.queue.isEmpty():
            currentIndex = self.queue.dequeue()
            curNode = "Node" + str(localRootNode)
            self.writeToGraph(curNode, self.heap.getLeftIndex(currentIndex))
            self.writeToGraph(curNode, self.heap.getRightIndex(currentIndex))
            localRootNode += 1
        self.graph.write("}")
        self.graph.close()

    def writeToGraph(self, curNode, directionIndex):
        if directionIndex != None:
            nextNode = "Node" + str(self.nodeNum)
            self.nodeNum += 1
            self.graph.write(nextNode + " [label=" + str(self.heap.get(directionIndex)) + 
                    "];\n")
            self.graph.write(curNode + " -> " + nextNode + ";\n")
            self.queue.enqueue(directionIndex)
        else:
            null = "Null" + str(self.nullNum)
            self.nullNum += 1
            self.graph.write(null + " [shape=point];\n")
            self.graph.write(curNode + " -> " + null + ";\n")

while True:
    print()
    print("Menu")
    print("----")
    print("f XXX: load data from file XXX into tree")
    print("a XXX: choose array-based implementation with size XXX")
    print("i XXX: insert value XXX into the tree (array-based version only)")
    print("b: choose binary tree-based implementation")
    print("h: build the heap")
    print("s: sort data in ascending order")
    print("v: visualize with graphviz")
    print("t: test for correctness")
    print("e: extract min")
    print("q: exit")
    print()

    command = input("input a command: ")
    if command == "":
        continue

    option = command[0]
    
    if option == "q":
        exit()

    elif option == "e":
        print(heap.extract())

    elif option == "b":
        heap = HeapBT()

    elif option == "a":
        size = int(command[2:])
        heap = Heap(size)

    elif option == "h":
        heap.buildHeap()

    elif option == "i":
        if type(heap) == HeapBT:
            print("Cannot be done because the heap is tree-based")
            input()
        else:
            value = int(command[2:])
            heap.insert(value)

    elif option == "f":
        filename = command[2:]
        values = QueueSLL()
        try:
            scan = Scanner(filename)
        except IOError:
            print("file not found")
            input()
            continue
        while True:
            nextInt = scan.readint()
            if nextInt == "":
                break
            if type(heap) == HeapBT:
                values.enqueue(BinaryNode(nextInt))
            else:
                values.enqueue(nextInt)
        scan.close()
        heap.readData(values)

    elif option == "v":
        if heap.peek() == None:
            print("Error: the tree is empty")
            input()
        else:
            if type(heap) == HeapBT:
                gw = TreeGraphWriter("graph", heap)
            else:
                gw = ArrayGraphWriter("graph", heap)
            gw.createGraph()
            gw.display()

    elif option == "s":
        if type(heap) == HeapBT:
            queue = heap.sort()
            while not queue.isEmpty():
                print(queue.dequeue())
        else:
            heap.sort()
            for i in range(heap.getSize()):
                print(heap.get(i))

    elif option == "t":
        print(heap.isCorrect())
        input()

    else:
        print("invalid option")
        input()
