from gmpy2 import mpz, invert
from random import randint


def mod_inverse(P):
    while True:
        k = randint(1, P - 1)
        try:
            k_inverse = invert(mpz(k), P - 1)
            if (k * k_inverse % (P - 1)) == 1:
                return int(k), int(k_inverse)
        except ZeroDivisionError:
            pass


def extended_euclidean_premium(a, b):
    a = mpz(a)
    b = mpz(b)
    x, y, u, v, m, n = 0, 1, 1, 0, a, b

    while n != 0:
        q = m // n
        u, x = x - q * u, u
        v, y = y - q * v, v
        m, n = n, m % n

    gcd = m
    return gcd, x, y


def extended_euclidean(a, b):
    '''Алгоритм Евклида (mod)'''
    U = mpz(a)
    V = mpz(b)

    while V != 0:
        U, V = V, U % V

    return int(U)


def fast_module_exp(x, a, p):
    '''Быстрое возведение по модулю'''
    x = mpz(x)
    result = mpz(1)
    x = x % p

    a = mpz(a)
    while a > 0:
        if a % 2 == 1:
            result = (result * x) % p
        a = a // 2
        x = (x * x) % p

    return int(result)


def miller_test(n: int, k: int) -> bool:
    '''
    Проверка числа на простоту с помощью теста Миллера-Рабина.
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
