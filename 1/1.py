# Solution to problem 1

def sumMultiples(limit):
    sum = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    print(sumMultiples(1000))
