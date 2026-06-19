# def charCount(s):
#     vowels = 0
#     consonants = 0
#     for char in s:
#         if char in "aeiouy":
#             vowels += 1
#         else:
#             consonants += 1
#     return (vowels, consonants)


# print(charCount("hello"))


def sumAndProd(L):
    sum, product = (0, 1)
    for i in L:
        sum += i
        product *= i
    return (sum, product)


print(sumAndProd([1, 2, 3, 8]))
