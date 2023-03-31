# JTMS-14
# a8 p5.py
# Abdullah Rafique
# arafique@jacobs-university.de

# adding item to queue
def enqueue(queue):
    val = int(input("Input number to add to the queue = "))
    queue.append(val)
    print("\n{} added to the queue".format(val))
    print()
    return

# remove item from queue


def dequeue(queue):
    if len(queue) != 0:
        print("\nThe value removed from the queue is", queue.pop(0))
        print()
    else:
        print("Queue underflow!")
        print()
    return
# function to print


def printq(queue):
    print("\nThe elements of the queue are:")
    for elem in queue:
        print(elem, end=" ")
    print()
    print()
    return
