# Solution to problem 32

from sets import Set

def pan():
    products = Set([])

    # Check 1 digit times 4 digit
    for i in range(1, 10):
        for k in range(1000, 10000):
            if checkNum(i, k, i * k):
                products.add(i * k)

    # Check 2 digit times 3 digit
    for i in range(1, 100):
        for k in range(100, 1000):
            if checkNum(i, k, i * k):
                products.add(i * k)

    sum = 0
    for num in products:
        sum += num
    return sum

def checkNum(a, b, c):
    total = [char for char in (str(a) + str(b) + str(c))]
    if "0" in total:
        return False
    if not (len(total)) == 9:
        return False
    digits = []
    for i in range(9):
        if total[i] in digits:
            return False
        else:
            digits.append(total[i])
    return True

if __name__ == "__main__":
    print pan()
