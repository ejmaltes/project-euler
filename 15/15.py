# Solution to problem 15

def pascal(limit):
    start = [1,1]
    result = recursePascal(1, limit * 2 - 1, start)
    return result[len(result) / 2]

def recursePascal(current, limit, array):
    if current > limit:
        return array
    else:
        newarray = [1]
        for i in range(1, len(array)):
            newarray.append(array[i - 1] + array[i])
        newarray.append(1)
        return recursePascal(current + 1, limit, newarray)

if __name__ == "__main__":
    print pascal(20);
