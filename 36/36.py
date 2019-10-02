# Solution to problem 36

import math

def doubleBase():
    nums = []
    for i in range(1, 1000000):
        if checkPalindrome(str(i)) and checkPalindrome(binary(i)):
            nums.append(i)

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

def binary(num):
    if num == 0:
        return 0
    temp = 0
    while num > math.pow(2, temp + 1):
        temp += 1

    temp += 1
    result = ""
    while temp >= 0:
        if num >= math.pow(2, temp):
            result += "1"
            num -= int(math.pow(2, temp))
        else:
            result += "0"
        temp -= 1
    while result[0] == "0":
        result = result[1::]
    return result

def checkPalindrome(num):
    return num == num[::-1]


if __name__ == "__main__":
    print doubleBase()
