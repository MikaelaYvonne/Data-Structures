# Mikaela Yvonne Dacanay
# CSC 231 - 001
# This program's goal is to open, read and process .txt files and create a list of tuples

def student_info(filename):
    """
    Opens and reads a file of student information and create a tuple then append
    the tuple on the list (student_id, student_name)

    :param filename: a .txt file
    :return: list (tuple) of (student_id, student_name)
    :raises: FileNotFoundError when the file does not exist
    """
    roster = [] # initialize an empty list

    try:
        # open the file to be read
        with open(filename, "r") as file:
            # read each line of the file
            for line in file:
                line = line.strip() # strips the whitespace
                file = line.split("\t") # splitting it by tabs

                student_id = int(file[0])
                student_name = file[1]

                #append the tuple to the roster list
                roster.append((student_id, student_name))

    except FileNotFoundError:
        print('Error: File does not exist')
        return []

    for student_id, student_name in roster:
        print(f"Student record: {student_id} ({student_name})")

    return roster


def main():
    #filename = input("Enter filename for the student roster as a .txt file")
    filename = "listOfNames_short.txt"

    student_info(filename)

if __name__ == "__main__":
    main()


