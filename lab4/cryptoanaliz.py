def findrstat(x, z):
    r = 0
    for _ in range(len(x)):
        r += x[_] ^ z[_]
    return r


def check(seq, code):
    chk = 1
    for _ in range(len(seq)):
        if seq[_] != code[_]:
            chk = 0
            break
    return chk


def nextvect(arr):
    arr = arr[::-1]
    c_b = 1
    for i in range(len(arr)):
        tmp, arr[i] = arr[i], arr[i] ^ c_b
        c_b &= tmp
    return arr[::-1]


def get_candidates(lfrs, arr, numb, c):
    cand = []
    qq = []
    for _ in range(2 ** len(arr)):
        lfrs.set_state(arr[:])
        seq = lfrs.gener_sequence(numb)
        qq.append(findrstat(seq, code))
        if findrstat(seq, code) < c:
            cand.append(arr)
        arr = nextvect(arr)
    print(min(qq))
    return cand


def get_candidates3(cand1, cand2, g1, arr):
    cand3 = []
    for i in range(len(cand1)):
        for j in range(len(cand2)):
            for k in range(2 ** len(arr)):
                g1.set_state(cand1[i][:], cand2[j][:], arr[:])
                seq = g1.gen_sequence(50)
                if check(seq, code) == 1:
                    cand3.append(arr)
                arr = nextvect(arr)
    return cand3


strcode = '100001111110111101001001111001001110001101011001100101101000110000111011001' \
          '110001111000101100110101001101101011001111100110100111111100000010010011000' \
          '000010000110111100011110100101100000011111100010010011100110001110011011001' \
          '101010101100101110001101011010000101010111100010101001001010001010110010100' \
          '010110001010001001110101111011110011011111011001100001110110011000101011100' \
          '010000001000110011100001011011101001010011011100100001010001100011001101111' \
          '00010001100000010110111010010111011011111011000000'


code = [int(code) for code in strcode]