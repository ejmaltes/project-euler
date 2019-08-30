# Solution to problem 12

import math

def triangle(limit):
    num = 1
    triangle = 0
    divisors = 0

    while divisors < limit:
        triangle = triangle + num
        divisors = lenDivisors(triangle)
        num += 1
    return triangle

def lenDivisors(num):
    primes = primeFactors(num)
    product = -1
    if len(primes) > 0:
        last = primes[0]
        count = 1
        product = 1
        for i in xrange(1, len(primes)):
            if primes[i] != last:
                product = product * (count + 1)
                last = primes[i]
                count = 1
            else:
                count += 1
        product = product * (count + 1)

    return product

def primeFactors(num):
    temp = num
    primeFactors = []
    while num % 2 == 0:
        primeFactors.append(2)
        num = num / 2

    count = 3
    while num != 1:
        if num % count == 0 and testPrime(count):
            primeFactors.append(count)
            num = num / count
        else:
            count += 2
    return primeFactors

def testPrime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(triangle(500))
