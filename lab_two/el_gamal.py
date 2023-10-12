from random import randint

from lib_lab_one import (fast_module_exp, extended_euclidean,
                         generate_prime)


def generate_g(p):
    '''Генерация числа g для Боба'''
    while True:
        g = randint(2, p - 1)
        if extended_euclidean(g, p - 1) == 1:
            return g


def create_secret_Bob(p, g):
    '''Вычисление x, у Боба'''
    x = randint(2, p - 1)
    y = fast_module_exp(g, x, p)
    return x, y


def alice_create_k(p, g):
    x, y = create_secret_Bob(p, g)
    m = randint(1, p - 1)
    k = randint(2, p - 1)
    a = fast_module_exp(g, k, p)
    b = (m * fast_module_exp(y, k, p))
    return x, y, a, b, m


def bob_think():
    p = generate_prime()
    g = generate_g(p)
    x, y, a, b, m = alice_create_k(p, g)
    a_exp = p - 1 - x
    m_rev = (b * fast_module_exp(a, a_exp, p)) % p
    print('--Переменные шифра--')
    print(f'    x = {x}')
    print(f'    y = {y}')
    print(f'    p = {p}')
    print(f'    g = {g}')
    print(f'    p - 1 - x = {a_exp}')
    print(f'    a = {a}')
    print(f'    b = {b}')
    if m == m_rev:
        print('--Код выполнен успешно--')
        print(f'    m" = {m_rev}')
        print(f'    m = {m}')
    else:
        print('--Ошибка шифрования--')


if __name__ == '__main__':
    bob_think()
