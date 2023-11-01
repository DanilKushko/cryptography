'''
    Здесь генерируются очень большие,
    простые числа.
'''
from random import getrandbits
import gmpy2

from castom_lab_one import miller_test
from my_const import BITS_GHOST, K


def generate_prime_and_check(bits: int, k: int) -> int:
    '''
    Генерация простого числа длиной указанных бит,
    а также вызов проверок на просту
    '''
    while True:
        candidate = getrandbits(bits)
        if candidate % 2 == 0:
            candidate += 1
        if candidate < 3:
            candidate = 3
        if candidate & 1:
            if miller_test(candidate, k):
                return candidate


def return_big_amount() -> int:
    '''
    Возврат большого числа указанных бит
    '''
    large_prime = generate_prime_and_check(BITS_GHOST, K)
    return large_prime


def prime_generate() -> int:
    '''
    Дополнительная проверка
    '''
    amount = int(return_big_amount())
    number_to_check = gmpy2.mpz(amount)

    if miller_test(number_to_check, K):
        return number_to_check
    else:
        return 'Error'


if __name__ == '__main__':
    amount = prime_generate()
    print(amount)
