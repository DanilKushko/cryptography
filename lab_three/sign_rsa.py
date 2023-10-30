'''
    Часть 1.
  "Подпись RSA"
'''
from random import randint
from hashlib import sha256
from gmpy2 import mpz, invert

from castom_lab_one import fast_module_exp, extended_euclidean
from prime_generate import prime_generate


def generate_P_Q():
    '''Генерация P, Q'''
    P = prime_generate()
    Q = prime_generate()
    while P == Q:
        Q = prime_generate()
    print('\nЧисла P, Q созданы!\n')
    return P, Q


def born_d(P, Q):
    '''
    Вычисление d, c (аналогично 2 лабе).
    но с ипользованием GMP.
    mpz - тип данных, для работы с большими числами.
    invert - обратный элемент для d по модулю f
    '''
    phi_N = (mpz(P) - 1) * (mpz(Q) - 1)

    d = None
    while d is None:
        potential_d = mpz(randint(2, phi_N - 1))
        if extended_euclidean(potential_d, phi_N) == 1:
            d = potential_d

    c = invert(d, phi_N)

    return int(phi_N), int(d), int(c)


def alice_hash(N, m, c):
    '''Алиса подпишет документ m'''
    print(f'\tСодержание документа: {m}')

    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)
    print(f'\tХеш (h): {h}\n\n')

    if h < N:
        s = fast_module_exp(h, c, N)
        return m, s
    else:
        print('\tОпаньки, а хеш больше числа N')
        return None


def bob_unpacked_hash(m, s, N, d):
    '''Боб и значение е'''
    print('Боб получил(<m, s> и N, d): ')
    print(f'm: {m}')
    print(f's = {s}')
    print(f'd = {d}')
    print(f'N = {N}')

    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)

    if s < N:
        e = fast_module_exp(s, d, N)
        print(f'e = {e}')

        if e == h:
            return (f'Боб вычислил е = {e}')
        else:
            return 'Error'
    else:
        return 'Error'


if __name__ == '__main__':
    m = input('Заполните документ m: ')
    P, Q = generate_P_Q()

    print('\tПолучаем числа P, Q')
    print(f'\t\tP = {P} ')
    print(f'\t\tQ = {Q}\n\n')
    N = P * Q

    print('\tВычислим F(N) = (P - 1)(Q - 1), получим d, c')
    f, d, c = born_d(P, Q)
    # print(f'\tF(N) = (P - 1)(Q - 1) = {f} ')
    print('\tАлиса публикует ключи: ')
    print(f'\t\td = {d}')
    print(f'\t\tc = {c}\n\n')

    print('\tАлиса хеширует документ (h = H(m), h < N)')
    m, s = alice_hash(N, m, c)

    e = bob_unpacked_hash(m, s, N, d)
