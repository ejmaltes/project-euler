# Solution to problem 20

def facDigiSum(limit):
    product = 1
    for i in range(2, limit + 1):
        product = product * i

    sum = 0
    while product > 0:
        sum += product % 10
        product = product / 10

    return sum
    
if __name__ == "__main__":
    print facDigiSum(100)
