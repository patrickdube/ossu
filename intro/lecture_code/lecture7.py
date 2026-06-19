def sumOfOdds(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            total += i
    return total


print(sumOfOdds(0, 11))
