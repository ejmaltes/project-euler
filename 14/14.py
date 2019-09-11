# Solution to problem 13

def collatz():
    nums = {2: [2,1]}
    max_length = [2, 2]

    for i in range(3, 1000000):
        nums[i] = [i]

        num = checkNum(i)

        while num != 1:
            if num in nums:
                nums[i].extend(nums[num])
                num = 1
            else:
                nums[i].append(num)
                num = checkNum(num)
        length = len(nums[i])
        if length > max_length[1]:
            max_length = [i, length]

    return max_length

def checkNum(num):
    if num % 2 == 0:
        return num / 2
    else:
        return num * 3 + 1


if __name__ == "__main__":
    print collatz()
