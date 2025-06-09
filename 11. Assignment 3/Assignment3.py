# Author: Mikaela Yvonne Dacanay
# Date: 06/03/2025
# Description :

from BinaryTree import BinaryTree
from bst import BST
from AVLTree import AVLTree
from Student import Student
import time

s_roster = "listOfNames_short.txt"
s_roster_sort = "listOfNames_short_sorted.txt"
s_target = "searchIds_short.txt"

m_roster = "listOfNames_med.txt"
m_roster_sort = "listOfNames_med_sorted.txt"
m_target = "searchIds_med.txt"

l_roster = "listOfNames_long.txt"
l_roster_sort = "listOfNames_long_sorted.txt"
l_target = "searchIds_long.txt"

def main():

    # BST implementation
    print("\nBinary Search Tree implementation")
    bst = BST()
    students = []

    # reading the file ans inserting
    bst_insert_counter = 0
    start_time = time.time()
    with open(m_roster, "r") as roster:
        for line in roster:
            student_id, name = line.strip().split("\t")
            student = Student(int(student_id), name)
            students.append(student)

            bst.insert(student)
            bst_insert_counter += 1

    insert_time = time.time() - start_time
    print(f"\nTime to insert {bst_insert_counter} records into BST in {insert_time: .6f}")

    # Searching
    bst_search_counter = 0
    start_time = time.time()
    with open(m_target, "r") as search_file:
        for line in search_file:
            student_id = int(line.strip())
            target = Student(student_id, None)

            found = bst.find(target)

            # if found:
            #     print("Found Student Record: ", found)
            # else:
            #     print("No record found for student ID: ", student_id)

            bst_search_counter += 1

    search_time = time.time() - start_time
    print(f"\nTime to search {bst_search_counter} records into BST in {search_time: .6f}")


    # AVL implementation
    print("\nAVL Tree implementation")
    avl = AVLTree()

    # reading and inserting the file
    avl_insert_counter = 0
    start_time = time.time()
    with open(l_roster, "r") as roster:
        for line in roster:
            student_id, name = line.strip().split("\t")

            student = Student(int(student_id), name)

            avl = avl.insert(student)
            avl_insert_counter += 1

    insert_time = time.time() - start_time
    print(f"\nTime to insert {avl_insert_counter} records into BST in {insert_time: .6f}")

    # Searching
    avl_search_counter = 0
    start_time = time.time()
    with open(l_target, "r") as search_file:
        for line in search_file:
            student_id = int(line.strip())
            target = Student(student_id, None)

            found = avl.find(target)

            # if found:
            #     print("Found Student Record: ", found)
            # else:
            #     print("No record found for student ID: ", student_id)

            avl_search_counter += 1

    insert_time = time.time() - start_time
    print(f"\nTime to search {avl_search_counter} records into BST in {insert_time: .6f}")



if __name__ == "__main__":
    main()