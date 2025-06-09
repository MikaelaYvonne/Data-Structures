# Author: Mikaela Yvonne Dacanay
# Date: 05/23/2025
# Description : This program works to process Student records using a list of Student objects.
# this program also perform operations like sorting, searching (linear and binary), and file
# handling.

R_SHORT = "listOfNames_short.txt"
R_MED = "listOfNames_med.txt"
TARGET_S = "searchIds_short.txt"
TARGET_M = "searchIds_med.txt"

class Student:
    """
    A class that represents a student with their name and student ID and compares said IDs
    using comparison operators
    """

    def __init__(self, student_id = None, name = ""):
        self.__student_id = int(student_id)
        self.__name = name

    def get_student_id(self):
        """
        Returns the student ID
        """
        return self.__student_id

    def get_name(self):
        """
        Returns the student name
        """
        return self.__name

    def set_id(self, student_id):
        """
        Sets the student ID
        """
        self.__student_id = student_id

    def set_name(self, name):
        """
        Sets the student name
        """
        self.__name = name

    def __str__(self):
        """
        Return a string representation of the student name and ID
        :return: str of student name and id
        """
        return f"{self.__student_id} ({self.__name})"

    def __cmp__(self, other):
        """
        Comparison of two students using their student IDs
        """
        return self.get_student_id() - other.get_student_id()

    def __eq__(self, other):
        """
        Checks if two students are equal based on their ID's
        """
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        """
        Checks if two students are not equal based on their ID's
        """
        return self.__cmp__(other) != 0

    def __lt__(self, other):
        """
        Checks if one student is less than the other based on their IDs
        """
        return self.__cmp__(other) < 0

    def __le__(self, other):
        """
        Checks if one student is less than or equal to the other based on their IDs
        """
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        """
        Checks if one student is greater than the other based on their IDs
        """
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        """
        Checks if one student is greater than or equal to the other based on their IDs
        """
        return self.__cmp__(other) >= 0

def find(roster, target_student):
    """
    Linear search to find the student in the roster using their ID
    :param roster:  List of Student objects
    :param target_student: student object to search for
    :return: Student if the student is found in the roster. otherwise it returns None
    """
    for student in roster:
        if student == target_student:
            return student
    return None

def findBS(roster, target_student):
    """
    Binary search to find a student in the roster using their ID
    :param roster: List of Student objects
    :param target_student: The student object to search for
    :return: Student if the student is found in the roster. otherwise it returns None
    """
    left = 0
    right = len(roster) - 1

    while left <= right:
        middle = (left + right) // 2
        if roster[middle] == target_student:
            return roster[middle]
        elif roster[middle] < target_student:
            left = middle + 1
        else:
            right = middle - 1
    return None


def main():
    """
    Main function that handles file reading, sorting and initiating search
    """

    roster = []
    with open(R_MED, 'r') as file:
        for line in file:
            line = line.strip()
            data = line.split('\t')

            student_id = int(data[0])
            name = data[1]

            roster.append(Student(student_id, name))

    roster.sort()

    with open(TARGET_M, 'r') as file:
        for line in file:
            line = line.strip()
            target_id = int(line) # converts the ID on each line from the file to an integer
            target_student = Student(target_id) # creates a Student object using its ID

            result = find(roster, target_student) #linear
            #result = findBS(roster, target_student)  # binary

            if result:
                print(f"Found student record: {result}")
            else:
                print(f"Student ID {target_id} not found")


if __name__ == "__main__":
    main()