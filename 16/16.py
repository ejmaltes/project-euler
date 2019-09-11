# Solution to problem 16

def sumPower(limit):
    num = long(2**limit)
    sum = 0

    while num > 0:
        sum += num % 10;
        num = num / 10
    return sum

if __name__ == "__main__":
    print sumPower(1000)
