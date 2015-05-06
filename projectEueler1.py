# Find all multiples of 3 or 5 below N
#
#
def multof3and5(input):
    start = 0
    end = int(input)
    total = 0

    while start < end:
        if start % 15 == 0 or start % 5 == 0 or start % 3 == 0:
            total += start

        start += 1

    return total

print multof3and5(1000)