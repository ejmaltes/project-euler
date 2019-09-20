# Solution to problem 30

def fifth():
    nums = []
    for i in range(2, 10 ** 6):
        temp = i
        sum = 0
        while not temp == 0:
            sum += (temp % 10) ** 5
            temp /= 10
        if sum == i:
            nums.append(i)
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total

if __name__ == "__main__":
    print fifth()
