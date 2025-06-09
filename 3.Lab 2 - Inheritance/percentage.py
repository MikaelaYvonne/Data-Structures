# Author: Mikaela Yvonne Dacanay
# Date: 05/21/2025
# Description : This program exhibits inheritance, where Percentage class is getting
# everything that is already in the Fractions class. It also overloads the Fraction class'
# __str__ to better suit the string representation of a percentage.

from fraction import Fractions

class Percentage(Fractions):
    """
    Represents a percentage value using fractions.

    The class is a representation of inheritance. where Percentage class
    is inheriting everything that is already in the Fractions class
    """
    def __init__(self, numerator = 0, denominator = 100):
        """
        A class for fractions that is represented using a numerator and a denominator.
        It allows the use of operations from Fractions class. Arithmetic and comparison
        operations for fraactions.

        :param numerator: The numerator of the fraction. Default is 0.
        :param denominator: The denominator of the fraction. Default is 100.

        """
        Fractions.__init__(self,numerator, denominator)

    def __str__(self):
        """
        Overloads the __str__ from fractions class, in order to represent the
        percentage value of the fraction properly.
        :return: float: percentage value of the fraction.
        """
        percentage = (self.get_numerator() / self.get_denominator()) * 100

        return f"{percentage:.1f}%"

def main():
    test1 = Percentage(76)
    test2 = Percentage(83)
    test3 = Percentage(81)

    weight1 = Percentage(30)
    weight2 = Percentage(30)
    weight3 = Percentage(40)

    final_grade = test1 * weight1 + test2 * weight2 + test3 * weight3

    print("Final Grade = " + str(final_grade))

    # Grade aspect weights in percentage
    test1_weight = Percentage(30)
    test2_weight = Percentage(40)
    test3_weight = Percentage(10)
    ftest_weight = Percentage(20)

    # test scores
    test1_score = Percentage(15,20)
    test2_score = Percentage(9,10)
    test3_score = Percentage(2, 10)
    ftest_score = Percentage(2,4)

    test1_wa = test1_weight * test1_score
    test2_wa = test2_weight* test2_score
    test3_wa = test3_weight * test3_score
    ftest_wa = ftest_weight * ftest_score

    print()
    print("Test 1: ", test1_wa)
    print("Test 2: ", test2_wa)
    print("Test 3: ", test3_wa)
    print("Final Test: ", ftest_wa)
    print()
    print(f"Final Grade: {test1_wa + test2_wa + test3_wa + ftest_wa}")
if __name__ == "__main__":
    main()


