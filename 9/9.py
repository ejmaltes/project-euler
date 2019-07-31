# Solution to problem 9

def triplet(target):
    for i in range(1, target / 3):
        for k in range(1, target / 2):
            j = target - i - k
            if (i * i + k * k == j * j):
                return i * k * j
    return -1

if __name__ == "__main__":
    print(triplet(1000))
