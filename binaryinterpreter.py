from binarysearchtree import BinarySearchTree
from binarynode import BinaryNode
from scanner import Scanner
import subprocess
from queuesll import QueueSLL
class GraphWriter(object):
    def __init__(self, filename, bst):
        self.nodeNum = 1
        self.nullNum = 0
        self.filename = filename
        self.graph = open(filename + ".dot", "w")
        self.queue = QueueSLL()
        self.bst = bst

    def createGraph(self):
        self.graph.write("digraph {\n")
        self.graph.write("graph [ordering=\"out\"];\n")
        self.queue.enqueue(self.bst.getRoot())
        self.graph.write("Node0 [label=" + str(self.bst.getRoot().getValue()) + "];\n")
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

bst = BinarySearchTree()

while True:
    print("Menu")
    print("----")
    print("f XXX: load data from file XXX into tree")
    print("i XXX: insert value XXX into tree")
    print("l XXX: determine whether XXX is in the tree or not")
    print("d XXX: delete value XXX from tree")
    print("v: visualize the tree")
    print("t: test tree for correctness")
    print("c: correct the tree")
    print("s XXX YYY: find node XXX and change it to YYY")
    print("r XXX: rotate node with value XXX one level closer to root")
    print("e: exit")

    command = input("input a command: ")
    option = command[0]
    value = command[2:]
    
    if option == "e":
        exit()

    elif option == "f":
        filename = value
        scan = Scanner(filename)
        while True:
            nextInt = scan.readint()
            if nextInt == "":
                break
            bst.insert(nextInt)
        scan.close()

    elif option == "v":
        if bst.getRoot() == None:
            print("Error: the tree is empty")
            input()
        else:
            gw = GraphWriter("graph", bst)
            gw.createGraph()
            gw.display()

    elif option == "t":
        print(bst.getIncorrectNode() == None)
        input()
    
    elif option == "s":
        oldVal = int(value.split()[0])
        newVal = int(value.split()[1])
        bst.replace(bst.find(oldVal), BinaryNode(newVal))

    elif option == "c":
        bst.correct()

    if option in "fvtsc":
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
        bst.rotate(bst.find(value))

    else:
        print("invalid command")
