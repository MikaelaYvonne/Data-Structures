import random
import time

def maxSubSum1(a):
    maxSum = 0

    for i in range (len(a)):
        for j in range (i, len(a)):
            thisSum = 0
            start = i
            end = j
            
            for k in range(i, j+1):
                thisSum += a[k]
                if (thisSum > maxSum):
                    maxSum = thisSum
                    maxStart = start
                    maxEnd = end
                    
    return maxSum, a[maxStart], a[maxEnd]

def maxSubSum2(a):
    maxSum = 0

    for i in range(len(a)):

        thisSum = 0
        start = i
        for j in range (i, len(a)):
            
            thisSum += a[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                maxStart = start
                maxEnd = j

    return maxSum, a[maxStart], a[maxEnd]


def maxSubSum3(a):
    subSum, left, right = maxSubSum3Rec(a, 0, len(a) - 1)
    return subSum, a[left], a[right]

def maxSubSum3Rec(a, left, right):
    if (left == right):
        if (a[left] > 0):
            return a[left], left, left
        else:
            return 0, 0, 0;

    center = (left + right) // 2
    maxLeftSum, leftLeftEdge, leftRightEdge = maxSubSum3Rec(a, left, center);
    maxRightSum, rightLeftEdge, rightRightEdge = maxSubSum3Rec(a, center + 1, right);

    maxLeftBorderSum = 0
    leftBorderSum = 0
    leftEdge = center
    for i in range(center, left - 1, -1):
        leftBorderSum += a[i]
        if (leftBorderSum > maxLeftBorderSum):
            maxLeftBorderSum = leftBorderSum
            leftEdge = i

    maxRightBorderSum = 0
    rightBorderSum = 0
    rightEdge = center + 1
    for i in range(center + 1, right+1):
        rightBorderSum += a[i]
        if (rightBorderSum > maxRightBorderSum):
            maxRightBorderSum = rightBorderSum
            rightEdge = i

    maxBorderSum = maxLeftBorderSum + maxRightBorderSum

    if (maxLeftSum >= maxRightSum and maxLeftSum >= maxBorderSum):
        return maxLeftSum, leftLeftEdge, leftRightEdge
    elif (maxRightSum >= maxLeftSum and maxRightSum >= maxBorderSum):
        return maxRightSum, rightLeftEdge, rightRightEdge
    else:
        return maxBorderSum, leftEdge, rightEdge



def maxSubSum4(a):
    maxSum, thisSum = 0, 0
    start, maxStart, maxEnd = 0, 0, 0

    for i in range(len(a)):
        
        thisSum += a[i]
        if (thisSum > maxSum):
            maxSum = thisSum
            maxStart = start
            maxEnd = i
        elif (thisSum < 0):
            thisSum = 0
            start = i + 1

    return maxSum, a[maxStart], a[maxEnd]

        
def main():
    for N in range(50, 51, 100):  # Change this to go from 100 to 1001

        print ("\n\nInput Size: ", N)
        a = [random.randint(-100,100) for i in range(N)] # creates a list of N random integers between -100 and 100

        # comment out this printing of the array after you verify the program works

        print("a = ", end="")
        for i in range(len(a)):
            # print 25 numbers per line
            if (i % 25 == 0):
                print()
            print(a[i], end = " ")
        print("\n")


        print("MaxSubSum1")

        startTime = time.time()
        maxSum, start, end = maxSubSum1(a)
        endTime = time.time()
        print("max subsequence sum =", maxSum)                     # comment out
        print("The sequence starts at", start, "and ends at", end) # comment out
        print ("\t{0:.6f}\tseconds".format(endTime - startTime))

        print("MaxSubSum2")
        startTime = time.time()
        maxSum, start, end = maxSubSum2(a)
        endTime = time.time()
        print("max subsequence sum =", maxSum)                     # comment out
        print("The sequence starts at", start, "and ends at", end) # comment out
        print ("\t{0:.6f}\tseconds".format(endTime - startTime))

        print("MaxSubSum3")
        startTime = time.time()
        maxSum, start, end = maxSubSum3(a)
        endTime = time.time()
        print("max subsequence sum =", maxSum)                     # comment out
        print("The sequence starts at", start, "and ends at", end) # comment out
        print ("\t{0:.6f}\tseconds".format(endTime - startTime))

        print("MaxSubSum4")
        startTime = time.time()
        maxSum, start, end = maxSubSum4(a)
        endTime = time.time()
        print("max subsequence sum =", maxSum)                     # comment out
        print("The sequence starts at", start, "and ends at", end) # comment out
        print ("\t{0:.6f}\tseconds".format(endTime - startTime))
    
if __name__ == "__main__":
    main()
