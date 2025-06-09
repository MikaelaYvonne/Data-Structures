# Author: Mikaela Yvonne Dacanay
# Date: 05/29/2025
# Description : This program implements a Queue ADT using a LinkedList class, where
# the back of the queue is the front [0]. The program includes operations/methods
# enqueue, dequeue, peak, isEmpty, and overloads the len operation to get the size of the
# queue

from LinkedList import *
import random

class QueueLL:
    """
    A class that represents a Queue ADT implementation using the LinkedList class,
    where the front of the queue is at position 0 (head) of the list
    """

    def __init__(self):
        """
        Initializes  an empty queue
        """
        self.__items = LinkedList()

    def isEmpty(self):
        """
        Checks if the queue is empty

        :return: True, if the queue is empty. False otherwise.
        """
        return self.__items.isEmpty()

    def enqueue(self, item):
        """
        Adds an item to the back of the queue, which is the tail (end) of the LinkedList

        :param item: item to be added to the queue
        """
        self.__items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        :return: The item at the front of the queue, or None if the queue is empty.
        """
        if self.isEmpty():
            return None
        else:
            return self.__items.pop(0)

    def peek(self):
        """
        Returns front of the queue without changing or removing it.

        :return: item at the front of the queue; None if the queue is empty
        """
        if self.isEmpty():
            return None

        return self.__items.find(0)

    def __len__(self):
        """
        Overloads the 'len' operator to return the size of the queue.

        :return: int - the number of items in the queue
        """
        return len(self.__items)


def main():
    """
    Test function to test the class QueueLL class.
    """
    # Creates instance of a QueueFrontEnd
    queue = QueueLL()

    # Checks/shows the initial state of the Stack
    print("Testing Queue implementation using the LinkedList class")
    print("The queue is Empty ==", queue.isEmpty())
    print("The size of the queue is ", len(queue))
    print("The item at the front is ", queue.peek())
    print()

    # Enqueueing 20 random integers to the queue
    for i in range(20):
        x = random.randint(-100, 100)
        print(x, end = " ")
        queue.enqueue(x)
    print("Enqueueing 20 random integers")
    print()

    # Checks/shows the state of the queue after enqueueing 20 items, and the class methods
    print("The queue is Empty ==", queue.isEmpty())
    print("The size of the queue is ", len(queue))
    print("The item at the front is ", queue.peek())
    print()

    # Dequeueing all items from the queue and print them as they are getting removed
    print("\nDequeuing all items:")
    while not queue.isEmpty():
        x = queue.dequeue()
        print("Dequeued the value: ", x)
    print()

    # This is an extra dequeue at the end after the queue has been
    # emptied. This is to ensure that dequeue() on an empty list
    # only  returns None
    print(queue.dequeue())

    # Final state of the queque
    print("The queue is Empty ==", queue.isEmpty())
    print("The size of the queue is ", len(queue))
    print("The item at the front is ", queue.peek())



if __name__ == "__main__":
    main()