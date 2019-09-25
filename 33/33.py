# Solution to problem 33
# Don't worry. I'll refactor some day

def cancel():
    result = []
    for i in range(10, 100):
        for k in range(10, 100):
            if testFraction(i, k):
                result.append([i, k])

    product = [1, 1]
    for i in range(len(result)):
        product[0] *= result[i][0]
        product[1] *= result[i][1]

    num = product[0]
    den = product[1]
    num_factors = getFactors(num)
    den_factors = getFactors(den)
    overlap_factors = getOverlap(num_factors, den_factors)


    for factor in overlap_factors:
        num /= factor
        den /= factor

    return den

def testFraction(num, den):
    if num / den >= 1 or num % 10 == 0 or den % 10 == 0:
        return False
    possible_cancel = tryCancel(num, den)
    num_factors = getFactors(num)
    den_factors = getFactors(den)
    overlap_factors = getOverlap(num_factors, den_factors)

    for factor in overlap_factors:
        num /= factor
        den /= factor

    factored = [num, den]
    for i in range(len(possible_cancel)):
        num = possible_cancel[i][0]
        den = possible_cancel[i][1]
        temp_num_factors = getFactors(num)
        temp_den_factors = getFactors(den)
        temp_overlap_factors = getOverlap(temp_num_factors, temp_den_factors)

        for factor in temp_overlap_factors:
            num /= factor
            den /= factor
        temp_factored = [num, den]
        if factored == temp_factored:
            return True
    return False

def getFactors(num):
    factors = []
    while num > 1:
        i = 2
        while not num % i == 0:
            i += 1
        factors.append(i)
        num /= i
    return factors

def getOverlap(a, b):
    overlap = []
    for i in range(len(a)):
        if a[i] in b:
            overlap.append(a[i])
            b.remove(a[i])
    return overlap

def simplify(num, den):
    num_factors = getFactors(num)
    den_factors = getFactors(den)
    overlap_factors = getOverlap(num_factors, den_factors)

    for factor in overlap_factors:
        num /= factor
        den /= factor
    return [num, den]

def tryCancel(num, den):
    num = str(num)
    den = str(den)
    possible = []
    for i in range(2):
        for k in range(2):
            if num[i] == den[k]:
                possible.append([int(num[1 - i]), int(den[1 - k])])
    return possible

if __name__ == "__main__":
    print cancel()
