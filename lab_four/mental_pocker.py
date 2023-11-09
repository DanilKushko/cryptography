from random import randint

from prime_generate import prime_generate
from castom_lab_one import (miller_test, mod_inverse,
                            extended_euclidean, fast_module_exp)

# Количество карт в колоде
K = 52
# Количество игроков в игре
n = randint(2, K)


def Sofi_Jermen_P_Q():
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
            return P, Q


def selection_C_D(P):
    '''Выбираются ключи С, D - инверсия числа С.'''
    C, D = mod_inverse(P)
    return C, D
