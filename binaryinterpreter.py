from binarysearchtree import BinarySearchTree
from scanner import Scanner
import subprocess
from queuesll import QueueSLL
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
        nullNum = 0
        graph.write("digraph {\n")
        graph.write("graph [ordering=\"out\"];")
        queue.enqueue(bst.getRoot())
        while not queue.isEmpty():
            current = queue.dequeue()
            curVal = str(current.getValue())
            graph.write(curVal + " -> ")
            if current.getLeft() != None:
                left = current.getLeft()
                graph.write(curVal + " -> " + str(left.getValue()) + ";\n")
                queue.enqueue(left)
            else:
                null = "null" + str(nullNum)
                graph.write(null + " [shape=point];\n")
                graph.write(curVal + " -> " + null" + str(nullNum) + " [shape=point];\n")
                nullNum += 1
            graph.write(curVal + " -> ")
            if current.getRight() != None:
                right = current.getRight()
                graph.write(str(right.getValue()) + "\n")
                queue.enqueue(right)
            else:
                graph.write("null" + str(nullNum) + " [shape=point];\n")
                nullNum += 1
        graph.write("}")
        graph.close()
        subprocess.call("dot -Teps graph.dot -o graph.eps", shell=True)
        subprocess.call("evince graph.eps", shell=True)
        

    elif option == "t":
        print(bst.testCorrectness())
    
    elif option == "s":
        oldNode = value.split()[0]
        newNode = value.split()[1]
        bst.replace(oldNode, newNode)

    value = int(value)

    if option == "i":
        bst.insert(value)

    elif option == "l":
        foundVal = bst.find(value)
        print(foundVal != None)

    elif option == "d":
        bst.delete(value)

    elif option == "r":
        pass
