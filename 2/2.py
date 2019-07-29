# Solution to problem 2

def sumFibonacci(limit):
    last = 1
    current = 2
    sum = 0

    while current < limit:
        if current % 2 == 0:
            sum += current
        temp = last
        last = current
        current += temp
    return sum

if __name__ == "__main__":
    print(sumFibonacci(4000000))
