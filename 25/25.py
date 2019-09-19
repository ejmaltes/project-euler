# Solution to problem 25

def fib(limit):
    prev = 1
    curr = 1
    count = 2
    while not checkLength(curr, limit):
        temp = prev
        prev = curr
        curr = temp + curr
        count += 1

    return count

def checkLength(num, limit):
    return len(str(num)) >= limit

if __name__ == "__main__":
    print fib(1000)
