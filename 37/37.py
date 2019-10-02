# Solution to problem 37

import math

def trunc():
    count = 0
    curr = 10
    sum = 0
    while count < 11:
        if test_num(curr):
            sum += curr
            count += 1
        curr += 1
    return sum

def test_num(num):
    truncs = get_truncs(num)
    for num in truncs:
        if not test_prime(num):
            return False
    return True

def get_truncs(num):
    result = []
    temp = num
    while temp > 0:
        result.append(temp)
        temp /= 10

    temp = num
    count = 1
    while count < len(str(num)):
        result.append(num % int(math.pow(10, count)))
        count += 1

    return result

def test_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(trunc())
