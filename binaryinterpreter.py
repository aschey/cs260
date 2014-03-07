from binarysearchtree import BinarySearchTree
from binarynode import BinaryNode
from scanner import Scanner
import subprocess
from queuesll import QueueSLL

def writeToGraph(current, getDirectionNode, queue, graph):
    curVal = str(current.getValue())
    directionNode = getDirectionNode()
    if directionNode != None:
        graph.write(curVal + " -> " + str(directionNode.getValue()) + ";\n")
        queue.enqueue(directionNode)
    else:
        global nullNum
        null = "null" + str(nullNum)
        graph.write(null + " [shape=point];\n")
        graph.write(curVal + " -> " + null + ";\n")
        nullNum += 1
    return queue

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
        graph = open("graph.dot", "w")
        queue = QueueSLL()
        global nullNum
        nullNum = 0
        graph.write("digraph {\n")
        graph.write("graph [ordering=\"out\"];")
        queue.enqueue(bst.getRoot())
        while not queue.isEmpty():
            current = queue.dequeue()
            queue = writeToGraph(current, current.getLeft, queue, graph)
            queue = writeToGraph(current, current.getRight, queue, graph)
        graph.write("}")
        graph.close()
        subprocess.call("dot -Teps graph.dot -o graph.eps", shell=True)
        subprocess.call("evince graph.eps", shell=True)

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
        bst.insert(BinaryNode(value))

    elif option == "l":
        foundVal = bst.find(value)
        print(foundVal != None)
        input()

    elif option == "d":
        bst.delete(value)

    elif option == "r":
        pass

    else:
        print("invalid command")
