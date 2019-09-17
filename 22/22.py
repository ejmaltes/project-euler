# Solution to problem 22

def getScores():
    data = open("names.txt", "r")
    names = ""
    for line in data:
        names += line[:len(line) - 1]
    names = names.split(",")
    names = bubbleSort(names)

    total_score = 0
    for i in range (len(names)):
        total_score += getNameScore(names[i], i + 1)

    return total_score

def getNameScore(name, rank):
    score = 0
    for i in range(1, len(name) - 1):
        score += getAsciiScore(name[i])
    return score * rank

def getAsciiScore(letter):
    return ord(letter) - ord("A") + 1

def bubbleSort(names):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(names) - 1):
            if names[i] > names[i + 1]:
                temp = names[i]
                names[i] = names[i + 1]
                names[i + 1] = temp
                sorted = False
    return names

if __name__ == "__main__":
    print getScores()
