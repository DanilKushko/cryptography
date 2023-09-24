'''
3) Функция построения общего ключа для двух абонентов по схеме
Диффи-Хеллмана
'''
import random
import math


def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'

    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

    return binary_num


def fast_module_exp(x, a, p):
    y = 1
    binary_x = decimal_to_binary(x)

    for x in binary_x:
        y = (y * y) % p
        if x == '1':
            y = (y * a) % p

    return y


# Тест Миллера-Рабина
def miller_test(n, d):
    a = 2 + random.randint(0, n - 4)
    x = fast_module_exp(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


# Проверка на простоту P=2Q+1
def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1

    while d % 2 == 0:
        d /= 2

    for _ in range(k):
        if not miller_test(n, d):
            return False

    return True


# Поиск первообразного корня
def find_primitive_root(p, q):
    g = 0
    for i in range(2, p - 1):
        if fast_module_exp(i, q, p) != 1:
            g = i
            break
    return g


# Протокол Диффи-Хеллмана
def diffie_hellman(Q):
    while True:
        if Q % 2 == 0:
            Q += 1

        if is_prime(Q, int(math.log2(Q))):
            P = 2 * Q + 1
            g = find_primitive_root(P, Q)
            break
        else:
            Q += 2

    print('Q =', Q)
    print('P =', P)
    print('g =', g)

    Xa = random.randint(1, Q - 1)
    Xb = random.randint(1, Q - 1)

    Ya = fast_module_exp(g, Xa, P)
    Yb = fast_module_exp(g, Xb, P)

    Zab = fast_module_exp(Yb, Xa, P)
    Zba = fast_module_exp(Ya, Xb, P)

    print('Xa =', Xa)
    print('Xb =', Xb)
    print('Ya =', Ya)
    print('Yb =', Yb)
    print('Zab =', Zab)
    print('Zba =', Zba)

    return Zab


Q = int(input('Введите число Q: '))
print(diffie_hellman(Q))
