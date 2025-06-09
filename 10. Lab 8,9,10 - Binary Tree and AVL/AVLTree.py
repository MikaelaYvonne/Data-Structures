# Author: Mikaela Yvonne Dacanay
# Date: 06/03/2025
# Description : The program implements an AVL tree that is self-balances
# during insertion by doing rotations that are dependent on which case
# the insertion falls under.

from BinaryTree import BinaryTree
from bst import BST

class AVLTree(BST):
    """
    AVLTree class is an extension of the BST and adds methods for
    self-balancing during insertion.
    AVL tree needs to have its left and right subtree have a height difference
    of less than 2
    """

    def balanced(self):
        """
        returns True id tree is unbalanced

        :return: True if tree is unbalanced, False otherwise
        """
        if self.get_left_child() is not None:
            l_height = self.get_left_child().get_height()
        else:
            l_height = -1
        if self.get_right_child() is not None:
            r_height = self.get_right_child().get_height()
        else:
            r_height = -1

        return abs(l_height - r_height) < 2

    def insert(self, x):
        """
        Insert a new value into the AVL tree
        :param x: value to insert to the tree
        :return: new root of the tree
        """

        if self.isEmpty():
            self.set_payload(x)
            return self

        # left subtree
        elif x < self.get_payload():
            if self.get_left_child() is None:
                self.set_left_child(AVLTree(x)) # instantiate new AVLTree node set as left child
                self.compute_height()
                return self
            else:
                self.set_left_child(self.get_left_child().insert(x)) # recursive insertion into the left subtree
                if not self.balanced():
                    # case 1:
                    if x < self.get_left_child().get_payload():
                        return self.rotate_with_leftChild()

                    else:
                    # case 2:
                        self.set_left_child(self.get_left_child().rotate_with_rightChild())
                        return self.rotate_with_leftChild()

                self.compute_height()
                return self

        # right subtree
        else:
            if self.get_right_child() is None:
                self.set_right_child(AVLTree(x)) # instantiate a new AVLTree node if the right child doesn't exist
                self.compute_height()
                return self
            else:
                self.set_right_child(self.get_right_child().insert(x))
                if not self.balanced():
                    # Case 4:
                    if x >= self.get_right_child().get_payload():
                        return self.rotate_with_rightChild()

                    # Case 3:
                    else:
                        self.set_right_child(self.get_right_child().rotate_with_leftChild())
                        return self. rotate_with_rightChild()


                self.compute_height()
                return self



    def rotate_with_leftChild(self):
        """
        rotate self with its left child
        :return: the new root of the tree
        """
        k1 = self.get_left_child() # left child to be rotated

        # where the rotation happen
        self.set_left_child(k1.get_right_child())
        k1.set_right_child(self)

        self.compute_height()
        k1.compute_height()

        return k1


    def rotate_with_rightChild(self):
        """
        Rotate self with its right child
        :return: the new root of the tree
        """
        k2 = self.get_right_child() # right child to be rotated

        # where rotation happen
        self.set_right_child(k2.get_left_child())
        k2.set_left_child(self)

        self.compute_height()
        k2.compute_height()

        return k2



def main():
    """
    function to test the program's methods.

    inserts values into the tree printing the inorder tree
    traversal each insertion
    """
    #print inorder traversal
    avl_tree = AVLTree()

    print()
    print("The tree is Empty == ", avl_tree.isEmpty())
    print("The AVL Tree: ", avl_tree.inorder_trav())
    print(avl_tree.balanced())


    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]

    for value in values:
        print("Inserting: ", value)
        avl_tree = avl_tree.insert(value)
        print("Inorder traversal after insertion: \n",avl_tree.inorder_trav())
        print()
        print()

    print()
    print("The tree is Empty == ", avl_tree.isEmpty())
    print("The AVL Tree:\n", avl_tree.inorder_trav())


if __name__ == "__main__":
    main()