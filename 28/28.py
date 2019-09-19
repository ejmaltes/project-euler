# Solution to problem 28

def spiral(limit):
    curr = 1
    increment = 2
    sum = 1

    while curr < limit * limit:
        for i in range(4):
            curr += increment
            sum += curr
        increment += 2
    return sum

if __name__ == "__main__":
    print spiral(1001)
