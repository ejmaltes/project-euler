# Solution to problem 31

def coins():
    total = 200
    values = [1, 2, 5, 10, 20, 50, 100, 200]
    result = [1] + [0] * total
    for i in range(len(values)):
        for k in range(values[i], total + 1):
            result[k] += result[k - values[i]]
    return result[len(result) - 1]

if __name__ == "__main__":
    print coins()
