# Solution to problem 21


LIMIT = 10000
NUMS = []

def amicable():
    sum = 0
    for i in range (0, LIMIT):
        if checkNum(i):
            print i
            sum += i
    return sum

def checkNum(num):
    temp = sumDivisors(num)
    if temp != num and sumDivisors(temp) == num:
        return True
    return False

def sumDivisors(num):
    sum = 0
    for i in range(1, num / 2 + 1):
        if num % i == 0:
            sum += i
    return sum

if __name__ == "__main__":
    print amicable()
