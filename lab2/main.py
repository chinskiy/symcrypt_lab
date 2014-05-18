def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_ext(a, b):
    assert a != 0 or b != 0
    u0, u1, v0, v1 = 1, 0, 0, 1
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        u0, u1, v0, v1 = v0, v1, u0 - q * v0, u1 - q * v1
    return a, u0, u1


def mult_inv(a, n):
    if gcd(a, n):
        return gcd_ext(a, n)[1]
    else:
        return 0


def linear_comparison(a, b, n):
    res = []
    d = gcd(a, n)
    if d:
        return [(mult_inv(a, n) * b) % n]
    else:
        if b % d == 0:
            a, b, n = a / d, b / d, n / d
            x = mult_inv(a, n) * b % n
            # for _ in range(d):
            #     res.append((x + _ * n) % (n * d))
            res.append(x)
            return res
        else:
            return 0


def readfile(name):
    file = open(name)
    rtext = file.read()
    newtext = ''
    for elem in rtext:
        if ord(elem) == 10:
            pass
        else:
            newtext += elem
    return newtext


def bigram_frequency(txt):
    freq = dict()
    for _ in range(len(txt) // 2):
        tmp = txt[_ * 2] + txt[_ * 2 + 1]
        if tmp not in freq:
            freq[tmp] = 0
        freq[tmp] += 1
    for elem in freq:
        freq[elem] /= (len(txt) - 1)
    return freq


def most_popular_bigram(let_freq):
    i = 0
    bigr = []
    for key, val in sorted(let_freq.items(), key=lambda x: x[1], reverse=True):
        bigr.append(key)
        i += 1
        if i > 4:
            break
    return bigr


def find_numb(bigram, m, inv_symb):
    return inv_symb.get(bigram[0]) * m + inv_symb.get(bigram[1])


def decrypt(encrtext, symb, a, b, m):
    plaintext = ''
    inv_symb = {v: k for k, v in symb.items()}
    for _ in range(len(encrtext) // 2):
        tmp = mult_inv(a, m ** 2) * (find_numb(encrtext[_ * 2] + encrtext[_ * 2 + 1], m, inv_symb) - b) % m ** 2
        plaintext += symb.get(tmp // m) + symb.get(tmp % m)
    return plaintext


def find_key(x1, x2, y1, y2, diction, m):
    key, inv_symb = [], {v: k for k, v in diction.items()}
    x1, x2, y1, y2 = find_numb(x1, m, inv_symb), find_numb(x2, m, inv_symb), find_numb(y1, m, inv_symb), find_numb(y2, m, inv_symb)
    a = linear_comparison(x1 - x2, y1 - y2, m * m)
    if a == 0:
        return 0
    for _ in range(len(a)):
        b = (y1 - a[_] * x1) % m ** 2
        key.append([int(a[_]), int(b)])
    return key


def check_text(txt):
    freq, freq['о'], freq['а'], freq['е'], freq['ф'], freq['щ'], freq['ь'] = dict(), 0, 0, 0, 0, 0, 0
    for elem in txt:
        if elem not in freq:
            pass
        else:
            freq[elem] += 1
    for elem in freq:
        freq[elem] /= (len(txt) - 1)
    if freq['о'] > 0.07 and freq['а'] > 0.05 and freq['ф'] < 0.01 and freq['щ'] < 0.02 and freq['ь'] < 0.05:
        return True
    else:
        return False


if __name__ == '__main__':
    symb = dict()
    symb = {0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й', 10: 'к',
            11: 'л', 12: 'м', 13: "н", 14: 'о', 15: 'п', 16: 'р', 17: 'с', 18: 'т', 19: 'у', 20: 'ф',
            21: 'х', 22: 'ц', 23: 'ч', 24: 'ш', 25: 'щ', 26: 'ь', 27: "ы", 28: 'э', 29: 'ю', 30: 'я'}
    text = readfile('14.txt')
    bigram_freq = bigram_frequency(text)
    pop_encr = most_popular_bigram(bigram_freq)
    pop_plain = ['ст', 'но', 'то', 'на', 'ен']
    for i1 in range(len(pop_encr)):
        for i2 in range(len(pop_encr)):
            for j1 in range(len(pop_plain)):
                for j2 in range(len(pop_plain)):
                    key = find_key(pop_plain[i1], pop_plain[i2], pop_encr[j1], pop_encr[j2], symb, 31)
                    if key != 0:
                        for _ in key:
                            tmptext = decrypt(text, symb, _[0], _[1], 31)
                            if check_text(tmptext):
                                print(_)
                                print(decrypt(text, symb, _[0], _[1], 31))
