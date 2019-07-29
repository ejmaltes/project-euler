# Solution to problem 3

import math

def largestPrime(limit):
    if limit == 4:
        return 2
    num = limit
    largest = 3
    current = 3
    while current < math.sqrt(num):
        if num % current == 0 and testPrime(current):
            largest = current
        current += 2
    return largest

def testPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(largestPrime(600851475143))
