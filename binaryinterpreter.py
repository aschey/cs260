from binarysearchtree import BinarySearchTree
from scanner import Scanner
bst = BinarySearchTree
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

    command = input("input a command")
    option = command[0]
    value = command[2:]
    
    if option == "f":
        filename = value
        scan = Scanner(filename)
        while True:
            nextInt = scan.readint()
            if nextInt = "":
                break
            bst.insert(nextInt)

    elif option == "v":
        pass

    elif option == "t":
        print(bst.testCorrectness())
    
    elif option == "s":
        oldNode
        self.replace(

    value = int(value)

    elif option == "i":
        bst.insert(value)

    elif option == "l":
        foundVal = bst.find(value)
        print(foundVal != None)

    elif option == "d":
        bst.delete(value)

    elif option == "r":
        pass
