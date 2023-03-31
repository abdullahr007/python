# JTMS-14
# a8 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de

queue = []


def main():
    # using queue to implement list
    # enequeu, dequeue and print
    while (True):
        ch = int(input("your option\n1:Add data\
            \n2:Remove data \n3:Print queue\n4:Exit\n"))
        if ch == 1:
            enqueue()
        elif ch == 2:
            dequeue()
        elif ch == 3:
            printq()
        elif (ch == 4):
            print("see ya!")
            break
        else:
            print("Dobara try kr")

# adding item to queue


def enqueue():
    val = int(input("number to be added = "))
    queue.append(val)
    print("\n{} added to the queue".format(val))
    print()

# remove item from queue


def dequeue():
    if len(queue) != 0:
        print("\nThe value removed from the queue is", queue.pop(0))
        print()
    else:
        print("Queue underflow!")
        print()
        return

# function to print


def printq():
    print("\nThe elements of the queue are:")
    for elem in queue:
        print(elem, end=" ")
    print()
    print()
    return


main()
