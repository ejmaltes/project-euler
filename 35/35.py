# Solution to problem 35

from sets import Set

def circular():
    primes = sieve(1000000)
    nums = Set([])

    for i in range(2, 1000000):
        temp = checkRotations(i, primes)
        if temp:
            for num in temp:
                nums.add(num)
    return len(nums)

def checkRotations(num, primes):
    length = len(str(num))
    temp = str(num) + str(num)
    nums = []
    for i in range(length):
        rotation = int(temp[i:i + length])
        nums.append(rotation)
        if not primes[rotation]:
            return False
    return nums

def sieve(limit):
    nums = []
    for i in range(0, limit):
        nums.append(True)

    for i in range(2, limit):
        for k in range(i * i, limit, i):
            nums[k] = False

    count = 0
    return nums

if __name__ == "__main__":
    print circular()
