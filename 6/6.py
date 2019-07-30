# Solution to problem 6

import math

def sumDifference(limit):
    sumSquare = 0
    squareSum = 0

    for i in range(1, limit + 1):
        sumSquare += int(math.pow(i, 2))

    for i in range(1, limit + 1):
        squareSum += i

    squareSum = int(math.pow(squareSum, 2))

    return squareSum - sumSquare


if __name__ == "__main__":
    print(sumDifference(100))
