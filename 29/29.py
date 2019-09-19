# Solution to problem 29

from sets import Set

def distinct(a, b):
    nums = Set([])
    for i in range(2, a + 1):
        for k in range(2, b + 1):
            nums.add(i ** k)
    return len(nums)

if __name__ == "__main__":
    print distinct(100, 100)
