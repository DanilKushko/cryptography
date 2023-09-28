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
    y = 1
    binary_x = decimal_to_binary(x)

    for bit in binary_x:
        y = (y * y) % p
        if bit == '1':
            y = (y * a) % p

    return y


def miller_test(n, k=50):
    '''
    Проверка числа на простоту с помощью
    теста Миллера-Рабина
    '''
    d = n - 1
    for _ in range(k):
        a = 2 + random.randint(0, n - 4)
        x = fast_module_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue

        while d != n - 1:
            x = (x * x) % n
            d *= 2

            if x == 1:
                return False

            if x == n - 1:
                break

        if x != n - 1:
            return False

    return n  # Возвращаем простое число


def generate_prime():
    '''Генерация числа Софи Жермен Q и безопасного числа P'''
    while True:
        Q = random.randint(ONE_HUNDRED, VERY_LARGE_NUMBER)
        prime_Q = miller_test(Q)
        if prime_Q:
            P = 2 * prime_Q + 1
            prime_P = miller_test(P)
            if prime_P:
                return prime_Q, P


def g_mod_P(Q, P):
    '''Генерация g'''
    g = 0
    while fast_module_exp(g, Q, P) == 1:
        g = random.randint(2, P - 1)
    return g


def diffie_hellman(Q, P):
    '''Сборка всех ключей'''
    g = g_mod_P(Q, P)
    Xa = random.randint(1, P - 1)
    Xb = random.randint(1, P - 1)
    Ya = fast_module_exp(g, Xa, P)
    Yb = fast_module_exp(g, Xb, P)
    Zab = fast_module_exp(Yb, Xa, P)
    Zba = fast_module_exp(Ya, Xb, P)
    return Q, P, g, Xa, Xb, Ya, Yb, Zab, Zba


if __name__ == '__main__':
    while True:
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
            break
