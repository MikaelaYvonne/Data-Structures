# Author: Mikaela Yvonne Dacanay
# Date: 06/03/2025
# Description: Compares Binary Search Tree (BST) and AVLTree performance with Student records.

from BinaryTree import BinaryTree
from bst import BST
from AVLTree import AVLTree
from Student import Student
import time

# File paths
s_roster = "listOfNames_short.txt"
s_roster_sort = "listOfNames_short_sorted.txt"
s_target = "searchIds_short.txt"

m_roster = "listOfNames_med.txt"
m_roster_sort = "listOfNames_med_sorted.txt"
m_target = "searchIds_med.txt"

l_roster = "listOfNames_long.txt"
l_roster_sort = "listOfNames_long_sorted.txt"
l_target = "searchIds_long.txt"


def process_tree(tree, roster_file, search_file, tree_name):
    """
    General function to process tree insertion and searching
    """
    try:
        # Reading and inserting into the tree
        insert_counter = 0
        start_time = time.time()
        with open(roster_file, "r") as roster:
            for line in roster:
                try:
                    student_id, name = line.strip().split("\t")
                    student = Student(int(student_id), name)
                    tree.insert(student)
                    insert_counter += 1
                except ValueError:
                    print(f"Skipping invalid line in {roster_file}: {line.strip()}")
        insert_time = time.time() - start_time
        print(f"\n[{tree_name}] Time to insert {insert_counter} records: {insert_time:.6f} seconds")

        # Searching in the tree
        search_counter = 0
        found_counter = 0
        start_time = time.time()
        with open(search_file, "r") as search:
            for line in search:
                try:
                    student_id = int(line.strip())
                    target = Student(student_id, None)
                    found = tree.find(target)  # Assuming `find` method returns the node or None
                    if found:
                        found_counter += 1
                    search_counter += 1
                except ValueError:
                    print(f"Skipping invalid ID in {search_file}: {line.strip()}")
        search_time = time.time() - start_time
        print(f"[{tree_name}] Time to search {search_counter} records: {search_time:.6f} seconds")
        print(f"[{tree_name}] Found {found_counter}/{search_counter} records")

    except FileNotFoundError:
        print(f"Error: File {roster_file} or {search_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    print("\nBinary Search Tree implementation")
    bst = BST()
    process_tree(bst, m_roster_sort, m_target, "BST")

    print("\nAVL Tree implementation")
    avl = AVLTree()
    process_tree(avl, m_roster_sort, m_target, "AVL")


if __name__ == "__main__":
    main()
