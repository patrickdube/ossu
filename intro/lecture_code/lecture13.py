def pairwise_div(Lnum, Ldenom):
    assert len(Lnum)==len(Ldenom), "diff lenghts"
    assert len(Lnum)!=0 and len(Ldenom)!=0, "empty list"
    Ldiv = []
    for i in range(len(Lnum)):
        try:
            Ldiv.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError("Division by 0")
    return Ldiv

L1 = [4, 5, 6]
L2 = [1, 0, 3]
L3 = [1, 2, 3]

Ldiv2 = pairwise_div(L1, L3)
print(Ldiv2)
# Ldiv1 = pairwise_div(L1, L2)
# print(Ldiv1)

