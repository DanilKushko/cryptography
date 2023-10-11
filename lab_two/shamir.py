import random

from lib_lab_one import (fast_module_exp, extended_euclidean,
                         miller_test)

BIG_AMOUNT = 10000


def generate_prime():
    '''Генерация простого числа P'''
    while True:
        P = random.randint(2, BIG_AMOUNT)
        prime_P = miller_test(P)
        if prime_P:
            return prime_P


def generate_key_Alice(p):
    '''Генерация пары чисел Са, Da Алисы'''
    while True:
        Ca = random.randint(2, p - 1)
        gcd = extended_euclidean(Ca, p - 1)
        if gcd == 1:
            break

    Da = 1
    while (Ca * Da) % (p - 1) != 1:
        Da += 1

    return Ca, Da


def generate_key_Bob(p):
    '''Генерация пары чисел Сb, Db Боба'''
    while True:
        Cb = random.randint(2, p - 1)
        gcd = extended_euclidean(Cb, p - 1)
        if gcd == 1:
            break

    Db = 1
    while (Cb * Db) % (p - 1) != 1:
        Db += 1

    return Cb, Db


def shamir_algorithm(p):
    '''Основная логика Шамира'''
    print('---Создаем числа p, m...---')
    m = random.randint(1, p - 1)
    print(f'    Число m = {m}')
    print(f'    Число p = {p}')
    keys_Alice = generate_key_Alice(p)
    keys_Bob = generate_key_Bob(p)
    print('--Ключи Алисы--')
    print(f'    Ca = {keys_Alice[0]}')
    print(f'    Da = {keys_Alice[1]}')
    print('--Ключи Боба--')
    print(f'    Cb = {keys_Bob[0]}')
    print(f'    Db = {keys_Bob[1]}')
    print('---Вычисления ключей---')
    x1 = fast_module_exp(m, keys_Alice[0], p)
    print(f'    x1 = {x1}')
    x2 = fast_module_exp(x1, keys_Bob[0], p)
    print(f'    x2 = {x2}')
    x3 = fast_module_exp(x2, keys_Alice[1], p)
    print(f'    x3 = {x3}')
    x4 = fast_module_exp(x3, keys_Bob[1], p)
    if x4 == m:
        print(f'    x4 = {x4}')
        print('---Ключи вычислены ---')
    else:
        print('---Ошибка шифрования---')
    return


if __name__ == '__main__':
    p = generate_prime()

    if p < 2:
        print('p должно быть больше или равно 2')
    else:
        P = shamir_algorithm(p)
        print(P)
