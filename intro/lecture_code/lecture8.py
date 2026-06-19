def isTriangular(n):
    total = 0
    for i in range(n + 1):
        total += i
        if total == n:
            return True
        elif total > n:
            return False


# def bisectionRoot(square):
#     lowerBound = 0
#     higherBound = square
#     guess = (lowerBound + higherBound) / 2
#     epsilon = 0.01
#     while abs(guess**2 - square) >= epsilon:
#         if guess**2 < square:
#             lowerBound = guess
#         elif guess**2 > square:
#             higherBound = guess
#         guess = (lowerBound + higherBound) / 2
#     return guess
#
#
# def countNumsWithSqrtCloseTo(n, epsilon):
#     count = 0
#     for i in range(n**3):
#         if abs(bisectionRoot(i) - n) < epsilon:
#             print(i, bisectionRoot(i))
#             count += 1
#     return count
#
#
# print(countNumsWithSqrtCloseTo(10, 0.1))


def isEven(n):
    return n % 2 == 0


def apply(criteria, n):
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count


print(apply(isTriangular, 49))
print(apply(isEven, 49))
