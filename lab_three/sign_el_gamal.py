'''
    Часть 1.
  "Подпись Эль Гамаля"

UPD: для корректной работы в файле
    prime_generate в ф-ии generate_prime_and_check
    рекомендуется передавать BITS_GAMAL
'''
from sympy import primitive_root
from random import randint
from gmpy2 import mpz, invert
from hashlib import sha224

from prime_generate import prime_generate
from test_el_gamal import test_el_gamal
from castom_lab_one import (miller_test, fast_module_exp)
from my_const import K


def mod_inverse(P):
    '''Жеское нахождение k его инверсии числа.'''
    while True:
        k = int(randint(1, P - 1))
        k_inverse = invert(mpz(k), P - 1)
        if (k * k_inverse % (P - 1)) == 1:
            return int(k), int(k_inverse)


def Alice_create_P_Q():
    '''
    Алиса выбирает такое число P,
    которое P = 2 * Q + 1
    '''
    print('Начинаем генерацию чисел P, Q...\n')
    while True:
        Q = prime_generate()
        P = 2 * Q + 1
        if miller_test(P, K):
            print(f'\tЧисла\n\tP = {P},\n\tQ = {Q}\n')
            return P


def find_primitive_root(P):
    '''Вызов функции нахождения первообразного корня g от P'''
    g = primitive_root(P)
    print(f'Ищем первообразный корень g от Р...\n\tg = {g}\n')
    return g


def Alice_create_keys(g, P):
    '''
    Алиса формирует:
    открытый ключ - y
    закрытый ключ - х
    '''
    x = int(randint(1, P - 1))
    y = fast_module_exp(g, x, P)
    return x, y


def Alice_hash(m, P):
    '''Алиса подписывает документ.'''
    h = int(sha224(m.encode('utf-8')).hexdigest(), 16)

    if h < P:
        print(f'\tХеш (h): {h}\n')
        return h
    else:
        print('Ошибка: хеш больше или равен P.')
        return None


def selection_k_r(P, g):
    '''Выбирается число k, считается r.'''
    k, k_test = mod_inverse(P)
    r = fast_module_exp(g, k, P)

    print('Получено число k, которое удовлетворяет',
          'условию "kk^(-1) mod (P-1)=1".')
    return k, r, k_test


def sign_doc(h, x, r, P, k_test):
    '''Вычисляются числа u, s.'''
    if h is None:
        print('Ошибка в вычислении хеша.')
        return None, None
    u = (h - x * r) % (P - 1)
    s = (k_test * u) % (P - 1)
    print('Числа u, s посчитаны.\n')
    return s


def sign_el_gamal():
    '''Основная логика работы подписывания документа'''
    m = 'Кушко Данил с группы АБ-109 хорошо постарался и хочет 5'
    P = Alice_create_P_Q()

    g = find_primitive_root(P)
    x, y = Alice_create_keys(g, P)

    print('Числа P, g, y публикуются в открытом доступе...\n',
          f'\tx = {x}\n\ty = {y}')

    h = Alice_hash(m, P)
    k, r, k_test = selection_k_r(P, g)
    s = sign_doc(h, x, r, P, k_test)

    if test_el_gamal(y, r, s, g, h, P) is not False:
        print('\n\tДокумент подписан!\n')
        print(f'r = {r}, \ns = {s}')
    else:
        print('Проверки видимо не будет.')


if __name__ == '__main__':
    sign_el_gamal()
