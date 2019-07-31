# Solution to problem 10

import math

UPPER_LIMIT = 2000000

def sieve(target):
    nums = []
    sum = 0
    for i in range(0, UPPER_LIMIT):
        nums.append(True)

    for i in range(2, UPPER_LIMIT):
        if nums[i]:
            sum += i
        for k in range(i * i, UPPER_LIMIT, i):
            nums[k] = False

    return sum

if __name__ == "__main__":
    print(sieve(10001))
