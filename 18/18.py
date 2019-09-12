# Solution to problem 18

def pathSum(file):
    data = open(file, "r")

    row_array = []

    for line in data:
        row = line.split(" ")
        row[len(row) - 1] = row[len(row) - 1][0:-1]
        row_array.append(row)

    sum = pathSumRecurse(0, 0, len(row_array), row_array, int(row_array[0][0]))

    return sum

def pathSumRecurse(curr_row, curr_index, length, row_array, sum):
    if curr_row >= length - 1:
        return sum
    else:
        sum_left = pathSumRecurse(curr_row + 1, curr_index, length, row_array, sum + int(row_array[curr_row + 1][curr_index]))
        sum_right = pathSumRecurse(curr_row + 1, curr_index + 1, length, row_array, sum + int(row_array[curr_row + 1][curr_index + 1]))

        if sum_left > sum_right:
            return sum_left
        return sum_right

if __name__ == "__main__":
    print pathSum("data.txt")
