# Solution to problem 26

def repeat(limit):
    max = 0
    max_index = 0
    for i in range(2, limit):
        repeat = findNumRepeat(i)
        if repeat > max:
            max = repeat
            max_index = i
    return max_index

def findNumRepeat(denom):
    remainders = []
    decimals = []
    repeat = False
    numer = 10

    while not repeat:
        while numer / denom == 0:
            numer *= 10
            remainders.append(0)
            decimals.append(0)

        div = numer / denom
        remainder = numer % denom

        if remainder == 0:
            return 0
        elif remainder in remainders and div == decimals[len(remainders) - remainders[::-1].index(remainder) - 1]:
            return remainders[::-1].index(remainder) + 1
        else:
            remainders.append(remainder)
            decimals.append(div)
            numer = remainder * 10

    return remainders

if __name__ == "__main__":
    print repeat(1000)
