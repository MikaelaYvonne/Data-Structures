# Author: Mikaela Yvonne Dacanay
# Date: 06/02/2025
# Description : This program is a recursive implementation of the following operations:
#               - Sum of a list using two implementations
#               - Finding the minimum value of the list
#               - The power of a number given the base and exponent

import random
def recSum1(alist):
    """
    Recursively calculates the sum of the list by dividing in halves

    :param alist: a list of numerical values
    :return: sum of the list
    """
    if len(alist) == 1:
        return alist[0]
    else:
        a = recSum1(alist[:len(alist) // 2])
        b = recSum1(alist[len(alist) // 2:])
        return a + b


def recSum2(alist):
    """
    Recursively calculates the sum of a list by adding the first
    element to the sum of the rest of the list

    :param alist: a list of numerical values
    :return: sum of the list
    """
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + recSum2(alist[1:])

def recMinimum(alist):
    """
    Recursively finds the minimum value in a list by
    dividing the list into halves.

    :param alist: a list of numerical value
    :return: minimum value in the list
    """
    if len(alist) == 1:
        return alist[0]
    else:
        right = recMinimum(alist[:len(alist) // 2])
        left = recMinimum(alist[len(alist) // 2:])

        if left < right:
            return left
        else:
            return right

def recPower(x, n):
    """
    Recursively calculates the power of number

    :param x:  is the base number
    :param n: the exponent
    :return: the result of x raised to the power of n
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        half_power = recPower(x, n//2)

        if n % 2 == 0:
            return half_power * half_power
        else:
            return half_power * half_power * x
def main():
    """
    Tests the functions recSum1(), recSum2(), recMinimum(), recPower()
    by comparing the values it returns to the values returned by the
    built-in function and operations

    """
    N = 100
    myList = [random.randint(-500, 500) for i in range(N)]

    print(myList)
    print("The sum of the numbers is: " + str(sum(myList)))
    print("The sum of the numbers using recSum1 is: " + str(recSum1(myList)))
    print("The sum of the numbers using recSum2 is: " + str(recSum2(myList)))
    print()

    print(myList)
    print("The minimum of the numbers is: " + str(min(myList)))
    print("The minimum of the numbers using recMinimum is: " + str(recMinimum(myList)))
    print()

    x = random.randint(0, 10)
    n = random.randint(0, 10)
    print(f"{x} raise to {n} is: {x ** n}")
    print(f"{x} raise to {n} using recPower is : {recPower(x,n)}")


if __name__ == "__main__":
    main()
