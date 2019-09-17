# Solution to problem 23
def sumAbundant():
    abundant = getAbundant(28123)
    nums = [False] * 28123

    for i in range(len(abundant)):
        for k in range(i, len(abundant)):
            sum = abundant[i] + abundant[k]
            if sum < len(nums):
                nums[sum] = True

    not_abundant_sum = 0
    for i in range(len(nums)):
        if not nums[i]:
            not_abundant_sum += i
    return not_abundant_sum

def getAbundant(limit):
    abundant = []
    for i in range (12, limit + 1):
        if sumDivisors(i) > i:
            abundant.append(i)
    return abundant

def sumDivisors(num):
    sum = 0
    for i in range(1, num / 2 + 1):
        if num % i == 0:
            sum += i
    return sum

if __name__ == "__main__":
    print sumAbundant()
