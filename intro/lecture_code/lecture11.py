# def remove_all(L, e):
#     Lcopy = L[:]
#     L.clear()
#     for i in Lcopy:
#         if i != e:
#             L.append(i)
#
# def remove_all(L, e):
#     for i in L[:]:
#         if i == e:
#             L.remove(i)

def remove_all(L, e):
    while e in L:
        L.remove(e)

L = [1, 2, 2]
remove_all(L, 2)
print(L)


