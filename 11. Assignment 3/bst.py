# Author: Mikaela Yvonne Dacanay
# Date: 06/04/2025
# Description : The program defines a (Binary Search Tree) BST class that
# extends the BinaryTree class. it adds the methods for insert(), find() and
# overloads the payload() and inorder_trav of the BinaryTree class

from BinaryTree import BinaryTree

class BST(BinaryTree):
    def __init__(self, payload = None, left_child = None, right_child = None):
        """
        Initializes the BST node

        :param payload: The value of the root node, default = None for empty tree
        :param left_child: left subtree
        :param right_child: right subtree
        """
        BinaryTree.__init__(self, payload, left_child, right_child)

        if self.get_payload() is None:
            # The height of an empty tree is -1
            self.__height = -1
        else:
            self.__height = 0

    def get_height(self):
        """
        returns the height of the current node

        :return: int value of the height of the said node
        """
        return self.__height


    def compute_height(self):
        """
        Compute and set the height based upon the subtree.
        The height is -1 for an empty tree, o for a leaf. or the max
        if the heights of its children plus one.
        :return: None
        """
        height = -1

        if self.get_left_child() is not None:
            height = max(height, self.get_left_child().get_height())

        if self.get_right_child() is not None:
            height = max(height, self.get_right_child().get_height())

        # Assertion: the height at this point will be the bigger of
        # the heights of the two subtrees. If this is a leaf, then
        # the height will still be a -1

        self.__height = height + 1



    def set_payload(self, payload):
        """
        Setter for the payload.
        overloads the set_payload from the BinaryTree because
        the height was added

        :param payload:  the contents of the root
        :return: None
        """
        BinaryTree.set_payload(self, payload)
        self.compute_height()


    def insert(self, x):
        """
        Insert a new value into the BST

        :param x: the contents of the root
        :return: None
        """
        if self.isEmpty():
            self.set_payload(x)

        elif x < self.get_payload():
            if self.get_left_child() is None:
                self.set_left_child(BST(x))
                self.compute_height()
            else:
                self.get_left_child().insert(x)
                self.compute_height()

        else: # x >= self.payload
            if self.get_right_child() is None:
                self.set_right_child(BST(x))
                self.compute_height()
            else:
                self.get_right_child().insert(x)
                self.compute_height()



    def find(self, x):
        """
        Find the value in the BST
        :param x: the contents of the root
        :return: the value in the tree that matches, or None if it's not there
        """
        if self.isEmpty():
            return None

        elif x == self.get_payload():
            return self.get_payload()

        elif x < self.get_payload():
            if self.get_left_child() is None:
                return None
            else:
                return self.get_left_child().find(x)

        else:
            if self.get_right_child() is None:
                return None
            else:
                return self.get_right_child().find(x)


    def min_value(self):
        """
        Find and return minimum value in the BST - should be the leftmost node
        """
        if self.get_left_child() is None:
            return self.get_payload()

        return self.get_left_child().min_value()


    def max_value(self):
        """
        Find and return maximum value in the BST - rightmost node
        """
        if self.get_right_child() is None:
            return self.get_payload()

        return self.get_right_child().max_value()


    def inorder_trav(self):
        """
        Does an inorder traversal, where it visits the left, root, then right
        :return: str of the tree in its inorder
         """

        result = ""

        if self.get_left_child():
            result += self.get_left_child().inorder_trav() + " "

        if self.get_payload() is not None:
            result += " " + str(self.get_payload()) + "(" + str(self.get_height()) + ")"

        if self.get_right_child():
            result += " " + self.get_right_child().inorder_trav()

        return result

def main():
    # bst = BST()

    my_list = [460, 320, 626, 233,428, 492, 747, 148, 269, 394,
               599, 635, 752, 102, 221, 285, 353, 395, 590, 613, 652]

    # my_list = [43, 37, 36, 41, 75, 57, 44, 58, 65, 64, 98, 78, 95, 102, 85] #in class tree activity
    bst = BST()

    for x in my_list:
        bst.insert(x)

    print(bst)
    print()

    print("Inorder traversal:")
    print(bst.inorder_trav())

    print()
    #testing find
    x = 599
    print(f"Finding the value {x} = {bst.find(x)}") # return 599
    x = 0
    print(f"Finding the value {x} = {bst.find(x)}") # return None
    x = 102
    print(f"Finding the value {x} = {bst.find(x)}") # return 102
    print()

    print("The minimum value in the BST: ",bst.min_value()) # 102
    print("The maximum value in the BST: ",bst.max_value()) # 752

    print("The height of the BST: ",bst.get_height()) # 4
if __name__ == "__main__":
    main()