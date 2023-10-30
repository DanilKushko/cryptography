from gmpy2 import mpz


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
