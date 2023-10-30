from hashlib import sha256
from random import randint

from lib_lab_one import generate_prime, extended_euclidean, fast_module_exp


def generate_P_Q():
    '''Генерация P, Q'''
    P = generate_prime()
    Q = generate_prime()
    while P == Q:
        Q = generate_prime()
    print('Числа P, Q получены!')
    return P, Q


def born_d(P, Q):
    '''Вычисление ключей c, d'''
    f = (P - 1) * (Q - 1)

    while True:
        d = randint(2, f - 1)
        gcd = extended_euclidean(d, f)
        if gcd == 1:
            break

    c = 1
    while (d * c) % f != 1:
        c += 1

    return f, d, c


def alice_hash(N, m, c):
    '''Алиса подпишет документ m'''
    print(f' Содержание документа: {m}')
    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)
    if h < N:
        s = fast_module_exp(h, c, N)
        return m, s


def bob_unpacked_hash(m, s, N, d):
    '''Боб и значение е'''
    print('Боб получил подписанный <m, s> и N, d')
    print(f'm: {m}')
    print(f's = {s}')
    print(f'd = {d}')
    print(f'N = {N}')
    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)

    if s < N:
        e = fast_module_exp(s, d, N)
        print(f'e = {e}')

        if e == h:
            return e
        else:
            return 'Error'
    else:
        return 'Error'


if __name__ == '__main__':
    m = 'М'
    print('Сейчас сгенерируются числа P, Q, P != Q...')
    P, Q = generate_P_Q()

    print(f'Числа получены. P = {P}, Q = {Q}.')
    N = P * Q

    print('Вычислим F(N) = (P - 1)(Q - 1), получим d, c')
    f, d, c = born_d(P, Q)
    print(f'F(N) = (P - 1)(Q - 1) = {f} ')
    print(f'Алиса публикует ключи d = {d}, c = {c}')

    print('Алиса сейчас вычислит h = H(m), h < N')
    m, s = alice_hash(N, m, c)

    e = bob_unpacked_hash(m, s, N, d)
