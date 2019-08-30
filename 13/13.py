# Solution to problem 13

def sumHundred():
    data = open("data.txt", "r")

    sum = 0
    for line in data:
        sum += int(line)

    while sum >= 10000000000:
        sum /= 10
        
    return sum

if __name__ == "__main__":
    print(sumHundred())
