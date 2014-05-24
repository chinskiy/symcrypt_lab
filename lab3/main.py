from lab3.functions import *

if __name__ == '__main__':
    gener = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    n_arr = polyn_reduction([1] + [0] * (2**7), gener)
    m_arr = polyn_reduction([1] + [0] * (2**5), gener)
    print(gener)
    print(n_arr)
    print(m_arr)