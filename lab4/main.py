from lab4.lfrs import *
from lab4.cryptoanaliz import *

if __name__ == '__main__':
    l1 = LFSR([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
    l2 = LFSR([1, 0, 0, 0, 0, 1, 1, 0, 1, 1])
    l3 = LFSR([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    # l1.set_state([0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0])
    # l2.set_state([1, 0, 1, 0, 0, 0, 1, 0, 1])
    # l3.set_state([0, 0, 1, 0, 1, 1, 0, 1, 0, 1])
    n1, n2 = 113, 97
    c1, c2 = 39, 35
    arr1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cand1 = get_candidates(l1, arr1, n1, c1)
    print(len(cand1))
    for el in cand1:
        print(el)
    cand2 = get_candidates(l2, arr2, n2, c2)
    print(len(cand2))
    for el in cand2:
        print(el)
    g1 = GeffeGen(l1, l2, l3)
    cand3 = get_candidates3(cand1, cand2, g1, arr3)
    print(cand3)
    # arr1 = l1.gener_sequence(100)
    # for elem in arr1:
    #     print(elem, end='')
    # print()
    # arr2 = l2.gener_sequence(100)
    # for elem in arr2:
    #     print(elem, end='')
    # print()