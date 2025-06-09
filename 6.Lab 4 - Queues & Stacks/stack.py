# Author: Mikaela Yvonne Dacanay
# Date: 05/27/2025
# Description : This program implements a Stack ADT. It includes methods to
# push, pop, peak, isEmpty, and overloads the len operation to get the size of the
# stack.

import random

class Stack:
    """
    A class representation of a stack ADT.
    """
    def __init__(self):
        """
        Initializes an empty stack
        """
        self.__items = []

    def isEmpty(self):
        """
        Checks if the stack is empty

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.__items) == 0

    def push(self, x):
        """
        Adds the item(x) on top of the stack

        :param x: The item to be added to the stack
        """
        self.__items.append(x)

    def pop(self):
        """
        Removes and returns the top element from the stack.

        :return: The removed element from the stack. Returns None if the stack is empty.
        """
        if self.isEmpty():
            return None
        else:
            return self.__items.pop()

    def peek(self):
        """
        Returns front of the stack without changing or removing it.

        :return: item at the front of the stack; None if the queue is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.__items[len(self)-1]

    def __len__(self):
        """
        Overloads the 'len' operator to return the size of the stack.

        :return: int - the number of items in the stack
        """

        return len(self.__items)

def main():
    """
    Test Function to demonstrate the operations and methods in the Stack Class.
    """

    # Creates instance of a Stack
    the_stack = Stack()
    print("Testing the Stack implementation")

    # Checks/shows the initial state of the Stack
    print("The stack is Empty ==", the_stack.isEmpty())
    print("The size of the stack is ", len(the_stack))
    print("The item at the front is ", the_stack.peek())
    print()

    # Pushes/adds 20 random integers to the stack
    for i in range(20):
        x = random.randint(-100, 100)
        print(x, end = " ")
        the_stack.push(x)
    print()

    # Checks/shows the state of the stack after pushing 20 items, and the class methods
    print("The stack is Empty ==", the_stack.isEmpty())
    print("The size of the stack is ", len(the_stack))
    print("The item at the front is ", the_stack.peek())
    print()

    # Popping all items from the stack and print them as they are getting popped
    print("\nPopping all items:")
    while not the_stack.isEmpty():
        x = the_stack.pop()
        print("Popped the value: ", x)
    print()

    # This is an extra pop at the end after the stack has been
    # emptied. This is to ensure that pop() on an empty list
    # only  returns None

    print(the_stack.pop())

    # Final state of the stack
    print("The stack is Empty ==", the_stack.isEmpty())
    print("The size of the stack is ", len(the_stack))
    print("The item at the front is ", the_stack.peek())
    print()
if __name__ == "__main__":
    main()


