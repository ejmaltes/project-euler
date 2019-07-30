# Solution to problem 5

import math

def findSmallest(limit):
    target = 0
    primes, the_rest = findPrimes(limit)
    primes = primes[::-1]
    step = getStep(limit, primes)
    current = step
    while target == 0:
        if checkDivisible(current, primes, the_rest):
            target = current
        current += step
    return target

def checkDivisible(num, primes, the_rest):
    for i in primes:
        if num % i != 0:
            return False

    for i in the_rest:
        if num % i != 0:
            return False

    return True

def getStep(limit, primes):
    temp = limit
    for i in primes:
        if limit % i == 0:
            break
        else:
            temp = temp * i
    return temp

def checkPrimes(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def findPrimes(limit):
    temp = []
    rest = []
    for i in range(3, limit):
        if checkPrimes(i):
            temp.append(i)
        else:
            rest.append(i)
    return temp, rest

if __name__ == "__main__":
    print(findSmallest(20))
