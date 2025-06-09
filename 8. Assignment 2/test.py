# Author: [Your Name]
# Date: [Today's Date]
# Description: This program reads student information from a names file, inserts the records into a custom Linked List,
# searches for specific student IDs in the Linked List based on a search file, and measures the time taken for
# insertions and searches. Uses the MyLinkedList and Student classes.

from LinkedList import LinkedList  # Replace with MyLinkedList if needed
from Student import Student
import time


def main():
    """
    The main function performs the following:
    1. Reads student information from a names file, inserts them into a linked list, and times the process.
    2. Reads search IDs from a search file, searches for students in the linked list, and times the process.
    3. Outputs search results and the time taken for insertion and searching.

    No parameters and no return value.
    """
    R_SHORT = "listOfNames_short.txt"
    R_MED = "listOfNames_med.txt"
    TARGET_S = "searchIds_short.txt"
    TARGET_M = "searchIds_med.txt"

    names_file = R_SHORT
    search_file = TARGET_S

    # names_file = R_MED
    # search_file = TARGET_M

    # Create a LinkedList instance
    student_list = LinkedList()
    insert_count = 0
    search_count = 0

    # === Insertion timing and logic ===
    start_insert = time.time()
    try:
        # Open the names file
        with open(names_file, "r") as infile:
            for line in infile:
                # Strip whitespace and process each line
                line = line.strip()
                if line:  # Ensure line is not empty
                    parts = line.split("\t")  # Split by tab
                    if len(parts) == 2:  # Ensure valid record
                        student_id = int(parts[0])  # Convert student ID to integer
                        name = parts[1]
                        student = Student(student_id, name)  # Create new Student object
                        student_list.insert(student)  # Insert into LinkedList
                        insert_count += 1
    except FileNotFoundError:
        print(f"File not found: {names_file}")
        return
    end_insert = time.time()
    print(
        f"The time to insert {insert_count} student records into a Linked List = {format(end_insert - start_insert, '.4f')} seconds."
    )

    # === Search timing and logic ===
    start_search = time.time()
    try:
        # Open the search file
        with open(search_file, "r") as infile:
            for line in infile:
                # Strip whitespace and process each line
                line = line.strip()
                if line:  # Ensure line is not empty
                    student_id = int(line)  # Convert search ID to integer
                    search_student = Student(student_id, "")  # Create a Student object with only ID
                    result = student_list.find(search_student)  # Search for the student in the LinkedList

                    # Uncomment the following lines when NOT timing performance:
                    # if result:
                    #     print(f"Found student record:  {result}")
                    # else:
                    #     print(f"Student ID {student_id} not found")
                    search_count += 1
    except FileNotFoundError:
        print(f"File not found: {search_file}")
        return
    end_search = time.time()
    print(
        f"The time to search {search_count} student records from a Linked List = {format(end_search - start_search, '.4f')} seconds."
    )


if __name__ == "__main__":
    main()
