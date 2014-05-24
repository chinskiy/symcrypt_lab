def deg(polyn):
    for i in range(len(polyn)):
        if polyn[i] == 1:
            return len(polyn) - i


def shift(polyn, n):
    return polyn + [0] * n


def add_pol(pol1, pol2):
    for elem in range(len(pol2)):
        pol1[elem] = pol1[elem] ^ pol2[elem]
    while pol1[0] == 0:
        pol1.pop(0)
    return pol1


def polyn_reduction(pol, gener):
    while deg(pol) >= deg(gener):
        pol = add_pol(pol[:], shift(gener[:], deg(pol) - deg(gener)))
    return [0] * (len(gener) - len(pol) - 1) + pol


