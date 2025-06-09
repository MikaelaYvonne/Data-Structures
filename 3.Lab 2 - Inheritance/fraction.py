# Author: Mikaela Yvonne Dacanay
# Date: 05/21/2025
# Description : A program that represents a fraction and performs arithmetic functions
# or operations such as addition, subtraction, multiplication and division. The program
# also finds the greatest common denominator (GCD)

class Fractions:
    """
    A class representation of a fraction that performs arithmetic functions -
    additions, subtraction, multiplication and division
    """
    def __init__(self, numerator = 0, denominator = 1):
        """
        Initializes a Fraction object with numerator and denominator.
        reduces the fraction and makes sure that the denominator will always be positive
        :param numerator: must be equal or greater than 0
        :param denominator: cannot be zero- must be greater than 0
        """
        if denominator == 0:
            raise ValueError("Fractions cant have 0 as a denominator")

        gcd = self.__gcd(abs(numerator), abs(denominator))

        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator


    def __gcd(self, a, b):
        """
        Finds and returns the greatest common divisor
        Takes self and two integers as parameters
        :return: returns greatest common denominator
        """
        while a % b != 0:
            old_a = a
            old_b = b

            a = old_b
            b = old_a % old_b
        return b

    def get_numerator(self):
        """
        Returns the numerator of the fraction
        """
        return self.__numerator

    def set_numerator(self, numerator):
        """
        Sets the numerator of the fraction
        :param numerator: new numerator value to set
        """
        self.__numerator = numerator


    def get_denominator(self):
        """
        gets the denominator of the fraction
        """
        return self.__denominator

    def set_denominator(self, denominator):
        """
        Sets the denominator of the function
        :param denominator: new denominator value to set
        """
        self.__denominator = denominator

    def __cmp__(self,other):
        """
        Compares this fraction with another fraction

        :param other: another fraction to compare with
        :return: positive, negative, or zero value based on the difference(comparison)
        """
        return self.get_numerator() * other.get_denominator() - other.get_numerator() * self.get_denominator()

        # return difference

    def __lt__(self, other):
        """
        Overloads the "<" operator and checks if the fraction is less than the other fraction

        :param other: another fraction to compare wit
        :return: True if self is < other, False, otherwise
        """
        return self.__cmp__(other) < 0


    def __le__(self, other):
        """
        Overloads the "<=" operator and checks if the fraction is less than or
        equal to the other fraction

        :param other: another fraction to compare with
        :return: True if self is <= other, False, otherwise
        """
        return self.__cmp__(other) <= 0


    def __gt__(self, other):
        """
        Overloads the ">" operator and checks if the fraction is greater than the other fraction

        :param other: another fraction to compare with
        :return: True if self is > other, False, otherwise
        """
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        """
        Overloads the ">=" operator and checks if the fraction is greater
        than or equal to the other fraction

        :param other: another fraction to compare with
        :return: True if self is >= other, False, otherwise
        """
        return self.__cmp__(other) >= 0


    def __eq__(self, other):
        """
        Overloads the "==" operator and checks if the fraction is
        equal to the other fraction
        :param other: another fraction to compare with
        :return: True if self is == other, False, otherwise
        """
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        """
        Overloads the "!=" operator and checks if the fraction is
        not equal to the other fraction

        :param other: another fraction to compare with
        :return: True if self is != other, False, otherwise
        """
        return self.__cmp__(other) != 0

    def __str__(self):
        """
        Converts the fractions - the numerator and denominator into a string
        :return: str
        """
        return f"{self.__numerator}/{self.__denominator}"


    def __add__(self, other):
        """
        overloads '+' and adds two fractions
        :param other: The fraction to add with the current fraction.
        :return: A new fraction that is the sum of the two fractions
        """
        sum_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        sum_denominator = self.__denominator * other.__denominator

        # return Fractions(sum_numerator, sum_numerator)

        return self.__class__(sum_numerator, sum_denominator)

    def __sub__(self, other):
        """
        overloads '-' and subtracts two fractions
        :param other: The fraction to subtract with the current fraction.
        :return: A new fraction that is the difference of the two fractions
        """
        diff_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        diff_denominator = self.__denominator * other.__denominator

        # return Fractions(diff_numerator, diff_denominator)

        return self.__class__(diff_numerator, diff_denominator)


    def __mul__(self, other):
        """
        overloads '*' and multiplies two fractions
        :param other: The fraction to multiply with the current fraction.
        :return: A new fraction object representing the product of the two fractions.
        """
        prod_n = self.__numerator * other.__numerator
        prod_d = self.__denominator * other.__denominator

        # return Fractions(prod_n, prod_d)
        return self.__class__(prod_n, prod_d)

    def __truediv__(self, other):
        """
        overloads '/' and divides two fractions
        :param other:The fraction to divide with the current fraction.
        :return: A new fraction that is the quotient of the two fractions
        """
        q_numerator = self.__numerator * other.__denominator
        q_denominator = self.__denominator * other.__numerator

        # return Fractions(q_numerator, q_denominator)
        return self.__class__(q_numerator, q_denominator)

def main():
    f1 = Fractions(10,16)
    f2 = Fractions(-4,-3)
    f3 = Fractions(3, -4)
    f4 = Fractions(4,3)

    print("f1 is ", f1)
    print("f2 is ", f2)
    print("f3 is ", f3)

    print(f1, "plus", f2, "=", f1 + f2)
    print(f1, "plus", f3, "=", f1 + f3)
    print()

    print(f1, "minus", f2, "=", f1 - f2)
    print(f1, "minus", f3, "=", f1 - f3)
    print()

    print(f1, "times", f2, "=", f1 * f2)
    print(f1, "times", f3, "=", f1 * f3)
    print()

    print(f1, "divided by", f2, "=", f1 / f2)
    print(f1, "divided by", f3, "=", f1 / f3)
    print()

    print(f1, "==", f3, "is", f1 == f3)
    print(f2, "==", f4, "is", f2 == f4)
    print(f1, "!=", f3, "is", f1 != f3)
    print(f2, "!=", f4, "is", f2 != f4)

    print()
    print(f2, "compare to", f4, f2.__cmp__(f4))
    print()

    print(f1, "<=", f3, "is", f1 <= f3)
    print(f2, "<=", f4, "is", f2 <= f4)
    print(f1, ">=", f3, "is", f1 >= f3)
    print(f1, ">=", f3, "is", f1 >= f3)

    print()
    print(f"{f1} is less than {f2} = {f1 < f2}")
    print(f"{f2} is less than {f1} = {f2 < f1}")
    print(f"{f1} is greater than {f2} = {f1 > f2}")
    print(f"{f2} is greater than {f1} = {f2 > f1}")



if __name__ == "__main__":
    main()