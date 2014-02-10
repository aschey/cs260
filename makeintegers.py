import sys
import random
def main():
    #gets the command-line arguments
    count = int(sys.argv[1])
    start = int(sys.argv[2])
    step = int(sys.argv[3])
    swaps = int(sys.argv[4])
    ints = []

    #generates the numbers
    for i in range(count):
        ints.append(start + i*step)

    #randomly swaps
    for i in range(0, swaps, 1):
        a = random.randint(0, len(ints) - 1)
        b = random.randint(0, len(ints) - 1)
        temp = ints[a]
        ints[a] = ints[b]
        ints[b] = temp

    #prints the newly swapped array
    for i in ints:
        print(i, end=" ")

main()
