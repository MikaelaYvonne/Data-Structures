# Author: Mikaela Yvonne Dacanay
# Date: 06/03/2025
# Description : The program defines a BinaryTree class that represents a
# binary tree. It uses operations for modifying nodes and methods for preorder
# , inorder, and postorder traversals

class BinaryTree:
    """
    Represents a binary tree with payload, leftChild, and rightChild.
    """

    def __init__(self, payload = None, left_child = None, right_child = None):
        """
        Constructor to initialize the Binary Tree

        :param payload: The value of the root node
        :param left_child: left child of the node
        :param right_child: right child of the node
        """
        self.__payload = payload
        self.__leftChild = left_child
        self.__right_child = right_child

    def get_payload(self):
        """
        Getter for the payload
        """
        return self.__payload

    def set_payload(self, payload):
        """
        setter for the payload
        """
        self.__payload = payload

    def get_left_child(self):
        """
        getter for the left child node
        """
        return self.__leftChild

    def set_left_child(self, left_child):
        """
        setter for the left child node
        """
        self.__leftChild = left_child

    def get_right_child(self):
        """
        getter for the right child node
        """
        return self.__right_child

    def set_right_child(self, right_child):
        """
        setter for the right child node
        """
        self.__right_child = right_child

    def isEmpty(self):
        """
        Checks if the payload(parent/root node) is empty or is None
        :return: True is the payload is None, False otherwise
        """
        return self.__payload is None

    def preorder_trav(self):
        """
        Does a preorder traversal, where it visits the root, left, then right
        :return: str of the tree in its preorder
        """

        result = ""

        if self.__payload is not None:
            result += str(self.__payload)

        if self.__leftChild:
            result += " " + self.__leftChild.preorder_trav()

        if self.__right_child:
            result += " " + self.__right_child.preorder_trav()

        return result

    def inorder_trav(self):
        """
        Does a inorder traversal, where it visits the left, root, then right
        :return: str of the tree in its inorder
        """

        result = ""

        if self.__leftChild:
            result += self.__leftChild.inorder_trav() + " "

        if self.__payload is not None:
            result += str(self.__payload)

        if self.__right_child:
            result += " " + self.__right_child.inorder_trav()

        return result

    def postorder_trav(self):
        """
        Does a postorder traversal, where it visits the left, right, then the root
        :return: str of the tree in its postorder
        """

        result = ""

        if self.__leftChild:
            result += self.__leftChild.postorder_trav() + " "

        if self.__right_child:
            result += self.__right_child.postorder_trav() + " "

        if self.__payload:
            result += str(self.__payload)

        return result

    def __str__(self):
        """
        string representation of a the tree using the inorder
        traversal
        """

        return self.inorder_trav()

def main():
    """
    Demonstrates the use of the BinaryTree class, adding nodes and
    displaying the three kinds of traversals
    """
    bt = BinaryTree()
    print("isEmpty() = " + str(bt.isEmpty()))
    print(bt)

    bt.set_payload(101)
    print("isEmpty() = " + str(bt.isEmpty()))
    print(bt)

    bt.set_left_child(BinaryTree(50))
    print(bt)

    bt.set_right_child(BinaryTree(250))
    print(bt)

    bt.get_left_child().set_leftChild(BinaryTree(42))
    print(bt)

    bt.get_left_child().get_leftChild().set_leftChild(BinaryTree(31))
    print(bt)

    bt.get_right_child().set_right_child(BinaryTree(315))
    print(bt)

    bt.get_right_child().set_leftChild(BinaryTree(200))


    print("Inorder traversal: " + bt.inorder_trav())
    print("Preorder traversal: " + bt.preorder_trav())
    print("Postorder traversal: " + bt.postorder_trav())

if __name__ == "__main__":
    main()