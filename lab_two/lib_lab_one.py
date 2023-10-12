import random

BIG_AMOUNT = 10**5


def extended_euclidean(a, b):
    '''Алгоритм Евклида (mod)'''
    U = a
    V = b

    while V != 0:
        U, V = V, U % V

    return U


def fast_module_exp(x, a, p):
    '''Быстрое возведение по модулю'''
    result = 1
    x = x % p

    while a > 0:
        if a % 2 == 1:
            result = (result * x) % p
        a = a // 2
        x = (x * x) % p

    return result


def is_prime_trial_division(n):
    '''Проверка числа на простоту методом перебора делителей'''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def miller_test(n):
    '''Проверка числа на простоту с помощью теста Миллера-Рабина'''
    k = 25
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0:
        return False

    if is_prime_trial_division(n):
        return n

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = fast_module_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = (x * x) % n

            if x == n - 1:
                break
        else:
            return False

    return n


def generate_prime():
    '''Генерация простого числа P'''
    while True:
        amount = random.randint(2, BIG_AMOUNT)
        prime_amount = miller_test(amount)
        if prime_amount:
            return prime_amount
