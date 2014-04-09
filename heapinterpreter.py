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
            self.graph.write(nextNode + " [label=" + str(directionNode.getValue()) + 
                    "];\n")
            self.graph.write(curNode + " -> " + nextNode + ";\n")
            self.queue.enqueue(directionNode)
        else:
            null = "Null" + str(self.nullNum)
            self.nullNum += 1
            self.graph.write(null + " [shape=point]\n;")
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
            self.writeToGraph(curNode, self.heap.getLeftIndex(currentIndex)current.getLeft())
            self.writeToGraph(curNode, current.getRight())
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
            self.graph.write(null + " [shape=point]\n;")
            self.graph.write(curNode + " -> " + null + ";\n")

while True:
    print("Menu")
    print("----")
    print("f XXX: load data from file XXX into tree")
    print("a: choose array-based implementation")
    print("t: choose tree-based implementation")
    print("s: sort data in ascending order")
    print("v: visualize with graphviz")
    print("t: test for correctness")
    print("e: exit")

    command = input("input a command: ")
    if command == "":
        continue

    option = command[0]
    
    if option == "e":
        exit()

    elif option == "t":
        heap = HeapBT()

    elif option == "a":
        heap = Heap(size)

    elif option == "f":
        filename = command[2:]
        values = []
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
            values.append(nextInt)
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
        

    elif option == "t":
        isCorrect = bst.isCorrect()
        if isCorrect:
            print("The tree is correct")
        else:
            print("The tree is incorrect")
            print("Incorrect node:", bst.incorrectNode.getValue())
        input()
    
    elif option == "s":
        oldVal = int(value.split()[0])
        newVal = int(value.split()[1])
        node = bst.find(oldVal)
        node.setValue(newVal)

    if option in "fvts":
        continue

    if option not in "inldr":
        print("invalid option")
        input()
        continue

    value = int(value)

    if option == "i":
        bst.insert(value)

    elif option == "l":
        foundVal = bst.find(value)
        print(foundVal != None)
        input()

    elif option == "d":
        bst.delete(bst.find(value))

    elif option == "r":
        try:
            bst.rotate(bst.find(value))
        except ValueError:
            print("invalid rotation")
            input()
            continue