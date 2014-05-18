import time
import math


def readfile(name):
    file = open(name)
    return file.read()


def filtertext_without_spaces(text):
    text = text.lower()
    newtext = ''
    for _ in range(len(text)):
        if 1072 <= ord(text[_]) <= 1105:
            if ord(text[_]) == 1105:
                newtext += chr(1077)
            else:
                newtext += text[_]
    return newtext


def filtertext_with_spaces(oltxt):
    oltxt = oltxt.lower()
    newtxt = ''
    for _ in range(len(oltxt)):
        if (1072 <= ord(oltxt[_]) <= 1105) or oltxt[_] == chr(32) or oltxt[_] == chr(10):
            if ord(oltxt[_]) == 32 or ord(oltxt[_]) == 10:
                if ord(newtxt[- 1]) == 32:
                    pass
                else:
                    newtxt += ' '
            elif ord(oltxt[_]) == 1098:
                newtxt += chr(1100)
            elif ord(oltxt[_]) == 1105:
                newtxt += chr(1077)
            else:
                newtxt += oltxt[_]
    return newtxt


def letter_frequency(text):
    freq = dict()
    for elem in text:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1
    for elem in freq:
        freq[elem] /= len(text)
    return freq


def letter_appearance(text):
    freq = dict()
    for elem in text:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1
    return freq


def bigram_frequency(text):
    freq = dict()
    for _ in range(len(text) - 1):
        tmp = text[_] + text[_ + 1]
        if tmp not in freq:
            freq[tmp] = 1
        else:
            freq[tmp] += 1
    for elem in freq:
        freq[elem] /= (len(text) - 1)
    return freq


def print_letter_frequency(let_freq):
    for elem in sorted(let_freq):
        print(elem, '    ', round(let_freq[elem], 4))


def print_bigram_frequency(let_freq):
    for key, val in sorted(let_freq.items(), key=lambda x: x[1], reverse=True):
        print(key, '    ', round(val, 4))


def find_entropy(let_freq, numb):
    entr = 0
    for elem in let_freq.values():
        entr -= elem * math.log(elem, 2)
    entr /= numb
    print(entr)


def encode_vigenere(text, passwrd):
    decrtext = ''
    for _ in range(len(text)):
        decrtext += chr((((ord(text[_]) + ord(passwrd[_ % len(passwrd)])) % 1072) % 32) + 1072)
    return decrtext


def index_of_matching(let_freq):
    index, numb = 0, 0
    for elem in let_freq:
        index += let_freq[elem] * (let_freq[elem] - 1)
        numb += let_freq[elem]
    index /= (numb * (numb - 1))
    print(index)

if __name__ == '__main__':
    # 1частина
    # text = readfile('bigtext.txt')
    # text = filtertext_without_spaces(text)
    # print(text)
    # let_freq = letter_frequency(text)
    # print_letter_frequency(let_freq)
    # find_entropy(let_freq, 1)
    # bigram_freq = bigram_frequency(text)
    # print_bigram_frequency(bigram_freq)
    # find_entropy(bigram_freq, 2)

    enctext = readfile('forencode.txt')
    enctext = filtertext_without_spaces(enctext)
    key = readfile('key.txt')
    key = filtertext_without_spaces(key)
    dectext = encode_vigenere(enctext, key)
    letters = letter_appearance(dectext)
    index_of_matching(letters)
    #print(dectext)