
# Author: Mikaela Yvonne Dacanay
# Date: 05/30/2025
# Description : This program implements a linked list ADT
# using operations like insertion at any index, overloading
# the __len__ to get the size of the list, and getting
# values/items from the front and back of the list.
# updated insert(), pop(), prepend() for the Student class. - only do insertion at
# the end of the Linked List and popping at the front. keeping both O(1)

class ListNode:
    """
    Represents a node in a Linked List
    """
    def __init__(self, payload = None, next_node = None):
        """
        Initialized a new node with a payload and reference
        to the next node.
        :param payload: value or data in the node
        :param next_node: a pointer to the next node
        """
        self.__payload = payload
        self.__nextListNode = next_node

    def get_payload(self):
        """
        Retrieves the payload on the node
        """
        return self.__payload

    def set_payload(self, value):
        """
        Sets and updates the payload of a node
        """
        self.__payload = value

    def get_next(self):
        """
        Retrieves the reference to the next code

        :return: next ListNode object or None if its last node
        """
        return self.__nextListNode

    def set_next(self, value):
        """
        Updates the reference to the next node
        """
        self.__nextListNode = value


class LinkedList:

    """
    Represents a linked list containing ListNode elements.
    """
    def __init__(self):
        """ Initializes an empty linked list"""
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __getIthNode(self, i): # O(N)
        """
        Retrieves the node at a specific index in the linked list.

        :param i: int - The index of the node to retrieve
        :return: ListNode object at the given index
        """
        # negative indexing
        if i < 0:
            i = self.__size + i

        if i < 0 or i >= self.__size:
            raise IndexError("List index is out of range")

        current = self.__head
        count = 0

        while current is not None and count < i:
            count += 1
            current = current.get_next()
        return current

    def insert(self, value):
        """
        Inserts a new node with the given value at the end of the Linked List

        :param value:
        """

        if self.isEmpty():
            # initializes the head and tail if the list is empty and create a new node
            # with value and use that to se the head and tail of the list
            self.__head = ListNode(value)
            self.__tail = self.__head
        else:
            self.__tail.set_next(ListNode(value)) # if not create new node, add to the end
            self.__tail = self.__tail.get_next() # this updates the tail pointer from curr to new

        self.__size += 1

    def front(self):
        """
        Retrieves the payload of the head

        :return: payload of the head or None if the list is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.__head.get_payload()

    def back(self):
        """
        Retrieves the payload of the tail

        :return: payload of the tail, or None if the list is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.__tail.get_payload()

    def __len__(self):
        """
        Gets the number of elements - values within the linked list

        :return: int - size of the linked list
        """
        return self.__size

    def isEmpty(self):
        """
        Checks if the linked list is empty

        :return: True if the list is empty, False otherwise
        """
        return self.__size == 0

    def __str__(self):
        """
        Returns a string representation of the linked list.
        Added ' - ' for clear separation of elements

        :return: str representation of elements - values
        within the list.
        """
        alist = ""
        current = self.__head

        while current is not None:
            alist += str(current.get_payload())

            if current.get_next() is not None:
                alist += " - "
            current = current.get_next()
        return alist

    def prepend(self, x):
        """
        Adds an element to the beginning of the Linked list
        """
        new_node = ListNode(x, self.__head) # new node that has its pointer to the curr head
        self.__head = new_node # makes the head point to the new node

        if self.__tail is None:
            # if list isEmpty, make the tail point to the new node
            self.__tail = new_node
        self.__size += 1

    def append(self, x):
        """
        Adds an element at the end
        """
        self.insert(x)

    def pop(self):
        """
        Removes then returns the payload of the node at front of the Linked List
        if list is empty return None

        :return x: - payload of the removed node; if list is empty returns None
        """

        if self.isEmpty():
            return None

        x = self.__head.get_payload()

        self.__head = self.__head.get_next()

        if self.__head is None:
            self.__tail = None

        self.__size -= 1

        return x

    def find(self, x):
        """
        Searches for a node with a given value and returns it, or
        returns None if not found

        :param x: value to search for
        :return: value if found, None otherwise
        """
        current = self.__head
        while current is not None:
            if current.get_payload() == x:
                return current.get_payload()

            current = current.get_next()

        return None

def main():
    """
    Tests the implementation of the LinkedList class and all of its
    methods' functionality
    """
    print("Creating a LinkedList")
    theLL = LinkedList()

    # Testing len() and isEmpty() on an empty list and printing it.
    print(f"Length of the list: {len(theLL)}")
    print(f"The list is empty == {theLL.isEmpty()}")
    print(f"Contents of the list: {theLL}")


    theLL.insert('A')
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert(1)
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert(123)
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert('a')
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert('b')
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    # Testing the filled list
    print("\n")
    print(f"Length of the list: {len(theLL)}")
    print(f"The list is empty == {theLL.isEmpty()}")
    print(f"The item on the front(head) of the list: {theLL.front()}")
    print(f"The item on the back(tail) of the list: {theLL.back()}")
    print(f"Contents of the list: {theLL}")

    # testing prepend(), append(), po()
    x = 12
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    theLL.append(x)
    print(f"After appending {x} to theLL  = ", str(theLL))

    x = "13"
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    theLL.append(x)
    print(f"After appending \"{x}\" to theLL  = ", str(theLL))

    x = "Amy"
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    theLL.prepend(x)
    print(f"After prepending {x} to theLL  = ", str(theLL))

    x = "1227"
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    theLL.prepend(x)
    print(f"After prepending \"{x}\" to theLL  = ", str(theLL))

    print("\n")

    theLL.pop() #pop from the end
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After popping from theLL  = ", str(theLL))
    print("\n")

    # Testing find()
    x = theLL.find("A")
    print("Finding A from theLL : ", x)

    x = theLL.find("123")
    print("Finding \"123\" from theLL : ", x)

    x = theLL.find(123)
    print("Finding 123 from theLL : ", x)

    x = theLL.find("13")
    print("Finding \"13\" from theLL : ", x)




if __name__ == "__main__":
    main()