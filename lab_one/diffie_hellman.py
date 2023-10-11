"""
Функция построения общего ключа для двух абонентов по схеме
Диффи-Хеллмана
"""
import random

from my_const import ONE_HUNDRED, VERY_LARGE_NUMBER


def decimal_to_binary(decimal_num):
    '''Перевод из двоичной в десятичную'''
    if decimal_num == 0:
        return '0'

    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

    return binary_num


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
    '''Генерация числа Софи Жермен Q и безопасного числа P'''
    while True:
        Q = random.randint(ONE_HUNDRED, VERY_LARGE_NUMBER)
        prime_Q = miller_test(Q)
        if prime_Q:
            P = 2 * prime_Q + 1
            prime_P = miller_test(P)
            if prime_P:
                return prime_Q, prime_P


def g_mod_P(Q, P):
    '''Генерация числа g в соответствии с протоколом Диффи-Хеллмана'''
    while True:
        g = random.randint(2, P - 1)
        if fast_module_exp(g, Q, P) != 1:
            return g


def diffie_hellman(Q, P):
    '''Сборка всех ключей по протоколу Диффи-Хеллмана'''
    g = g_mod_P(Q, P)
    Xa = random.randint(1, P - 1)
    Xb = random.randint(1, P - 1)
    Ya = fast_module_exp(g, Xa, P)
    Yb = fast_module_exp(g, Xb, P)
    Zab = fast_module_exp(Yb, Xa, P)
    Zba = fast_module_exp(Ya, Xb, P)
    return Q, P, g, Xa, Xb, Ya, Yb, Zab, Zba


if __name__ == '__main__':
    Q, P = generate_prime()
    Q, P, g, Xa, Xb, Ya, Yb, Zab, Zba = diffie_hellman(Q, P)
    if Zab == Zba:
        print(f'Q: {Q}, '
              f'P: {P} '
              f'g: {g}, '
              f'Xa: {Xa}, '
              f'Xb: {Xb}, '
              f'Ya: {Ya}, '
              f'Yb: {Yb} ')
        print(f'Общий закрытый ключ создан: {Zab}')
    else:
        print('Ошибка при генерации закрытого ключа.')
