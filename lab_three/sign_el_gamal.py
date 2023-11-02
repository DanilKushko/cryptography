'''
    Часть 2.
  "Подпись Эль - Гамаля"

UPD: для корректной работы в файле
    prime_generate в ф-ии generate_prime_and_check
    рекомендуется передавать BITS_GAMAL
'''
from sympy import primitive_root
from random import randint
from hashlib import sha256

from prime_generate import prime_generate
from castom_lab_one import (miller_test, fast_module_exp,
                            extended_euclidean)
from my_const import K
from test_el_gamal import test_el_gamal


def Alice_create_P_Q():
    '''
    Алиса выбирает такое число P,
    которое P = 2 * Q + 1'''
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
    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)
    if h < P:
        print(f'\tХеш (h): {h}\n')
        return h
    else:
        return ('Error')


def selection_k_r(P, g):
    '''Выбирается число k, считается r.'''
    while True:
        k = int(randint(1, P - 1))
        k_calc = k ** -1
        k_test = fast_module_exp(k * k_calc, -1, P - 1)
        if extended_euclidean(k, P - 1) == 1 and k_test == 1:
            r = fast_module_exp(g, k, P)
            print('Получено число k, которое удовлетворяет',
                  'условию "kk^(-1) mod (P-1)=1".')
            return k, r, k_calc


def sign_doc(h, x, r, P, k_calc):
    '''Вычисляются числа u, s.'''
    u = (h - x * r) % (P - 1)
    s = (k_calc * u) % (P - 1)
    print('Числа u, s посчитаны.\n')
    return u, s


def sign_el_gamal():
    '''Основная логика работы подписывания документа'''
    m = 'Hello'
    P = Alice_create_P_Q()

    g = find_primitive_root(P)
    x, y = Alice_create_keys(g, P)

    print('Числа P, g, y публикуются в открытом доступе...\n',
          f'\tx = {x}\n\ty = {y}')

    h = Alice_hash(m, P)
    k, r, k_calc = selection_k_r(P, g)
    u, s = sign_doc(h, x, r, P, k_calc)
    print('Документ подписан!\n')

    choice = int(input('Если желаете увидеть проверку, нажмите 1  '))
    if choice == 1:
        test_el_gamal(m, y, r, s, g, h, P)
    else:
        return 'Проверки видимо не будет.'


if __name__ == '__main__':
    sign_el_gamal()
