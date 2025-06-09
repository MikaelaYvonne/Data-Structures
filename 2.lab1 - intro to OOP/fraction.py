# Author: Mikaela Yvonne Dacanay
# Date: 05/20/2025
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

        return Fractions(sum_numerator, sum_denominator)

    def __sub__(self, other):
        """
        overloads '-' and subtracts two fractions
        :param other: The fraction to subtract with the current fraction.
        :return: A new fraction that is the difference of the two fractions
        """
        diff_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        diff_denominator = self.__denominator * other.__denominator

        return Fractions(diff_numerator, diff_denominator)


    def __mul__(self, other):
        """
        overloads '*' and multiplies two fractions
        :param other: The fraction to multiply with the current fraction.
        :return: A new fraction object representing the product of the two fractions.
        """
        prod_n = self.__numerator * other.__numerator
        prod_d = self.__denominator * other.__denominator

        return Fractions(prod_n, prod_d)

    def __truediv__(self, other):
        """
        overloads '/' and divides two fractions
        :param other:The fraction to divide with the current fraction.
        :return: A new fraction that is the quotient of the two fractions
        """
        q_numerator = self.__numerator * other.__denominator
        q_denominator = self.__denominator * other.__numerator

        return Fractions(q_numerator, q_denominator)

def main():
    f1 = Fractions(10, 1)
    f2 = Fractions(-4, -3)
    f3 = Fractions(3, -4)

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

if __name__ == "__main__":
    main()