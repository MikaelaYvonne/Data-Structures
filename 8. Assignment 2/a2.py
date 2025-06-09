# Author: Mikaela Yvonne Dacanay
# Date: 05/30/2025
# Description : This program reads student information from a file
# that has both the student ID and name, inserts this data into a
# a Linked List and searches for specific students using the IDs
# that are on the target/search file. It also measures the time of
# insertion and searches. It uses the LinkedList and Student classes

from LinkedList import *
from Student import Student
import time

S_ROSTER = "listOfNames_short.txt"
M_ROSTER = "listOfNames_med.txt"
TARGET_S = "searchIds_short.txt"
TARGET_M = "searchIds_med.txt"


def main():
    """
    The main functions performs the:
    - reading of the student data from the file and calls the insert function from the
        Linked List class, and times the process of inserting all data into the Linked List.
    - reading the stu
    :return:
    """
    roster = LinkedList()
    insert_count = 0
    search_count = 0

    start_insert = time.time()
    with open(M_ROSTER, "r") as file:
        for line in file:
            line = line.strip()
            data = line.split("\t")

            student_id = int(data[0])
            name = data[1]
            student = Student(student_id, name)
            roster.insert(student)
            insert_count += 1
    end_insert = time.time()
    time_insert = end_insert - start_insert
    print(f"The time to insert {insert_count} student records into a Linked List = {time_insert:.4f} seconds.")

    start_search = time.time()
    with open(TARGET_M, "r") as file:
        for line in file:
            line = line.strip()
            student_id = int(line)

            target_student = Student(student_id, "")
            result = roster.find(target_student)

            # if result:
            #     print(f"Found student record: {result}")
            # else:
            #     print(f"Student ID {student_id} not found")
            search_count += 1
    end_search = time.time()
    time_search = end_search - start_search
    print(f"The time to search {search_count} student records from a Linked List = {time_search: .4f} seconds")


if __name__ == "__main__":
    main()
