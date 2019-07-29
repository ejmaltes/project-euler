# Solution to problem 4

import math

def largestProduct(digits):
    largest = 0
    lowerLimit = int(math.pow(10, digits - 1))
    higherLimit = int(math.pow(10, digits))
    for i in range(lowerLimit, higherLimit):
        for k in range(lowerLimit, higherLimit):
            product = i * k
            if checkPalindrome(product) and product > largest:
                largest = product;
    return largest

def checkPalindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(largestProduct(3))
