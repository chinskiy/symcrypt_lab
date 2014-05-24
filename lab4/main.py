from lab4.lfrs import *
from lab4.cryptoanaliz import *
import time

if __name__ == '__main__':
    t1 = time.time()
    l1 = LFSR([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1])
    l2 = LFSR([1, 0, 0, 0, 0, 1, 1, 0, 1, 1])
    l3 = LFSR([1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    g1 = GeffeGen(l1, l2, l3)
    n1, n2, c1, c2 = 112, 95, 38, 33
    cand1 = get_candidates(l1, [0 for _ in range(len(l1.polyn))], n1, c1)
    cand2 = get_candidates(l2, [0 for _ in range(len(l2.polyn))], n2, c2)
    res = get_res(cand1, cand2, g1, [0 for _ in range(len(l3.polyn))])
    for _ in range(len(res)):
        print('l', _ + 1, ' = ', sep='', end='')
        print(''.join(str(_) for _ in res[_]))
    print(time.time() - t1)