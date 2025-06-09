# Author: Mikaela Yvonne Dacanay
# Date: 05/29/2025
# Description : This program implements a linked list ADT
# using operations like insertion at any index, overloading
# the __len__ to get the size of the list, and getting
# values/items from the front and back of the list.

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

    def insert(self, i, x):
        """
        Inserts a new node with the given value at the specific position

        :param i: int - index where to insert the node
        :param x:  the value - payload, to store in the new node
        """
        if self.isEmpty():
            self.__head = ListNode(x)
            self.__tail = self.__head

        # Inserting before head
        elif i <= 0:
            self.__head = ListNode(x, self.__head)

        # After tail
        elif i >= self.__size:
            self.__tail.set_next(ListNode(x))
            self.__tail = self.__tail.get_next()

        # somewhere in between
        else:
            # Traversing until it gets the (i-1)st one
            prev = self.__getIthNode(i - 1)
            prev.set_next(ListNode(x, prev.get_next()))

            if self.__tail == prev:
                self.__tail = self.__tail.get_next()

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
        self.insert(0, x)

    def append(self, x):
        """
        Adds an element at the end
        """
        self.insert(self.__size, x)

    def pop(self, i = None):
        """
        Removes then returns the payload of the node at index i

        If i is None the method removes then returns that last node

        :param i: int, the index of the node to be removed
        :return x: - payload of the removed node; if list is empty returns None
        """

        if self.isEmpty():
            return None

        else:
            if i is None:
                i = self.__size - 1

            if i == 0:
                x = self.__head.get_next()

                self.__head = self.__head.get_next()
                self.__size -= 1

                if self.__head is None:
                    self.__tail = None

                return x

            else:
                prev = self.__getIthNode(i - 1)

                x = prev.get_next().get_payload()

                if self.__tail == prev.get_next():
                    self.__tail = prev

                prev.set_next(prev.get_next().get_next())

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


    theLL.insert(0, 'A')
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert(1, 1)
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert(0, 123)
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert(len(theLL), 'a')
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"theLL  = ", str(theLL))

    theLL.insert((len(theLL)//2), 'b')
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
    theLL.append(12)
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After appending theLL  = ", str(theLL))

    theLL.append("13")
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: {len(theLL)}")
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After appending theLL  = ", str(theLL))

    theLL.prepend("Amy")
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After prepending theLL  = ", str(theLL))

    theLL.prepend("1227")
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After prepending theLL  = ", str(theLL))

    print("\n")

    theLL.pop() #pop from the end
    print("\ntheLL is Empty == ", theLL.isEmpty())
    print(f"The size of the list: ", len(theLL))
    print("The item in at the front is ", theLL.front())
    print("The item in at the back is ", theLL.back())
    print(f"After popping [1] from theLL  = ", str(theLL))
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