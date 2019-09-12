# Solution to problem 17

ONE_TO_NINETEEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
AND = "and"

def sumWords(limit):
    sum_length = 0

    for i in range(1, limit + 1):
        num_string = ""
        if i == 1000:
            num_string = "onethousand"

        if i % 1000 >= 100:
            num_string = ONE_TO_NINETEEN[(i % 1000) / 100 - 1] + HUNDRED
            if i % 100 > 0:
                num_string += AND

        if i % 100 <= 19 and i % 100 > 0:
            num_string += ONE_TO_NINETEEN[(i % 100) % 19 - 1]
        elif i % 100 >= 20:
            num_string += TENS[(i % 100) / 10 - 1]
            if i % 10 > 0:
                num_string += ONE_TO_NINETEEN[i % 10 - 1]
        sum_length += len(num_string)

    return sum_length

if __name__ == "__main__":
    print sumWords(1000)
