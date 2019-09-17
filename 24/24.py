# Solution to problem 24

def findAllPermutations(initial):
    prev = [initial[0]]
    curr = initial
    permutations = []
    while not curr[0] < prev[0]:
        permutations.append(list(curr))
        prev = list(curr)
        curr = findNextPermutation(curr)
    return permutations[1000000 - 1]

def findNextPermutation(arr):
    first = len(arr) - 2
    while first > 0 and arr[first] > arr[first + 1]:
        first -= 1

    second = first + 1
    for i in range(first + 2, len(arr)):
        if arr[i] < arr[second] and arr[i] > arr[first]:
            second = i
    arr = swap(arr, first, second)
    arr = sortRight(arr, first)

    return arr

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def sortRight(arr, index):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(index + 1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr = swap(arr, i, i + 1)
                sorted = False
    return arr


if __name__ == "__main__":
    print findAllPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
