# Solution to problem 34

def digifac():
    result = []
    for i in range(3, 100000):
        if i == factorialSum(i):
            result.append(i)
    sum = 0
    for i in range(len(result)):
        sum += result[i]
    return sum

def factorialSum(num):
    sum = 0
    while num > 0:
        temp = num % 10
        product = 1
        for i in range(2, temp + 1):
            product *= i
        sum += product
        num /= 10
    return sum

if __name__ == "__main__":
    print digifac()
