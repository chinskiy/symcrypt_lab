from lab4.lfrs import *
from lab4.cryptoanaliz import *

if __name__ == '__main__':
    l1 = LFSR([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
    l2 = LFSR([1, 0, 0, 0, 0, 1, 1, 0, 1, 1])
    l3 = LFSR([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    g1 = GeffeGen(l1, l2, l3)
    n1, n2, n3 = 106, 82, 82
    c1, c2 = 36, 30
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cand1 = get_candidates(l1, arr1, n1, c1)
    cand2 = get_candidates(l2, arr2, n2, c2)
    print(len(cand1))
    print(len(cand2))