# Solution to problem 7

import math

UPPER_LIMIT = 1000000

def sieve(target):
    nums = []
    for i in range(0, UPPER_LIMIT):
        nums.append(True)

    for i in range(2, UPPER_LIMIT):
        for k in range(i * i, UPPER_LIMIT, i):
            nums[k] = False

    count = 0
    for i in range(2, len(nums)):
        if nums[i]:
            count += 1
            if count == target:
                return i
    return -1

if __name__ == "__main__":
    print(sieve(10001))
