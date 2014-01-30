from queuesll import QueueSLL
from queuecdll import QueueCDLL
import sys
def main():
    while True:
        print("menu")
        print("====")
        print("new QueueTTT: new queue of type TTT")
        print("enqueue NNN: add value NNN to the back of the queue")
        print("dequeue: remove the first value")
        print("peek: print the next value to be dequeued")
        print("size: print the size")
        print("visualize: print the queue")
        print("exit: exit the interpreter")
        print()
        command = input("enter a command: ")
        splitCommand = command.split()
        command = command.lower()
        if command == "new queuesll":
            queue = QueueSLL()
            print()
        elif command == "new queuecdll":
            queue = QueueCDLL()
            print()
        elif splitCommand[0] == "enqueue":
            queue.enqueue(eval(splitCommand[1]))
            #ex = "queue.enqueue("+splitCommand[1]+")"
            #value = compile(splitCommand[1], "queuemain.py", "single")
            #try:
            #    queue.enqueue(eval(value))
            #except NameError:
            #    queue.enqueue(splitCommand[1])
            #exec(ex)
            print()
        elif command == "dequeue":
            print()
            print(queue.dequeue())
            input()
        elif command == "size":
            print()
            print(queue.store.getSize())
            input()
        elif command == "visualize":
            print()
            queue.store.display()
            input()
        elif command == "exit":
            exit()
        else:
            print("invalid command")
            input()

