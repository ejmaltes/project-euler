# Solution to problem 19

MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def countSundays():
    total_days = 0
    sundays = 0
    year = 1
    for i in range(0, 12 * 101):
        if (total_days + 1) % 7 == 0:
            sundays += 1
        if i % 12 == 1 and year % 4 == 0:
            total_days += 1
        if i % 12 == 0:
            year += 1

        total_days += MONTHS[i % 12]

    return sundays - 1

if __name__ == "__main__":
    print countSundays()
