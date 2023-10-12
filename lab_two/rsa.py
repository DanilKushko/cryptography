from random import randint

from lib_lab_one import (fast_module_exp, extended_euclidean,
                         generate_prime)


def generate_P_Q():
    '''Генерация чисел P и Q'''
    while True:
        P = generate_prime()
        Q = generate_prime()
        if P != Q:
            return P, Q


def bob_think():
    '''
    Боб вычисляет:
    f = (P - 1)(Q - 1)
    закрытый ключ - d
    открытый ключ - c
    '''
    Pb, Qb = generate_P_Q()
    N = Pb * Qb
    f = (Pb - 1) * (Qb - 1)

    while True:
        d = randint(2, f - 1)
        gcd = extended_euclidean(d, f)
        if gcd == 1:
            break

    c = 1
    while (d * c) % f != 1:
        c += 1

    return Pb, Qb, N, d, c


def alice_think(Pb, Qb, N, d, c):
    '''Алиса получает числа Боба, формирует криптограмму'''
    N = Pb * Qb
    m = randint(1, N - 1)
    e = fast_module_exp(m, d, N)
    return e, m


def bob_decryption(e, c, N, m):
    '''Боб делает дешифровку'''
    m_res = fast_module_exp(e, c, N)
    if m_res == m:
        return m_res
    else:
        return 'Error'


if __name__ == '__main__':
    Pb, Qb, N, d, c = bob_think()
    print(f'Публичные ключи Боба: P = {Pb}, Q = {Qb}')
    print(f'Закрытый и открытый ключи Боба: d = {d}, c = {c}')

    e, m = alice_think(Pb, Qb, N, d, c)
    print(f'Алиса отправляет зашифрованное сообщение (e): {e}')
    print(f'Сообщение Алисы: m = {m}')

    result = bob_decryption(e, c, N, m)
    print(f'Боб дешифровал сообщение: {result}')
