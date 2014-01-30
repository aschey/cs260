from stackdca import StackDCA
from stacksll import StackSLL
def main():
    while True:
        print("menu")
        print("====")
        print("new StackTTT: new stack of type TTT")
        print("push NNN: push value NNN")
        print("pop: pop the last value")
        print("size: print the size")
        print("visualize: print the stack")
        print("exit: exit the interpreter")
        print()
        command = input("enter a command: ")
        command = command.lower()
        splitCommand = command.split()
        if command == "new stackdca":
            capacity = int(input("capacity: "))
            stack = StackDCA(capacity)
            print()
        elif command == "new stacksll":
            stack = StackSLL()
            print()
        elif splitCommand[0] == "push":
            stack.push(eval(splitCommand[1]))
            print()
        elif command == "pop":
            print()
            print(stack.pop())
            input()
        elif command == "size":
            print()
            print(stack.store.getSize())
            input()
        elif command == "visualize":
            print()
            stack.store.display()
            input()
        elif command == "exit":
            exit()
        else:
            print("invalid command")
            input()

