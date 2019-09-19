# Solution to problem 27

import math

def quadratic():
    primes = getNeg(sieve(1000))
    max_nums = [0, 0, 0]
    for i in range(len(primes)):
        for k in range(len(primes)):
            test = primeTest(primes[i], primes[k])
            if test[2] > max_nums[2]:
                max_nums = test
    return max_nums[0] * max_nums[1]

def getNeg(list):
    for i in range(len(list)):
        list.append(-list[i])
    return list

def primeTest(a, b):
    n = 0
    while testPrime(int(math.pow(n, 2)) + a * n + b):
        n += 1
    return [a, b, n]

def testPrime(num):
    if num < 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sieve(limit):
    nums = []
    for i in range(0, limit):
        nums.append(True)

    for i in range(2, limit):
        for k in range(i * i, limit, i):
            nums[k] = False

    primes = []
    for i in range(2, limit):
        if nums[i]:
            primes.append(i)
    return primes

if __name__ == "__main__":
    print quadratic()
