'''
    Часть 3.
  "Подпись ГОСТ"
'''
import random
from hashlib import sha256

from castom_lab_one import miller_test, fast_module_exp
from prime_generate import prime_generate
from test_gost import test_GOST
from my_const import bit_size_p, K


def generate_p_b(q):
    '''Генерируем p так, чтобы старшие биты равнялись 1.'''
    bit_size_q = len(str(q))
    while True:
        b = random.getrandbits(bit_size_p - bit_size_q)
        p = b * q + 1
        if miller_test(p, K):
            return p, b


def get_a(p, b):
    '''Вычисление a.'''
    a = 0
    while a < 1:
        g = random.randint(1, p - 1)
        a = fast_module_exp(g, b, p)
    return a


def generate_amount(q):
    '''Формируется случайное число меньше чем q'''
    k = random.randint(0, q)
    # print(f'\tРазмер числа k (k) в битах = {len(str(k))}')
    return k


def hash(m, q):
    '''Вычисляется хеш функции.'''
    print(f'\tСодержание документа: {m}')

    h = int(sha256(m.encode('utf-8')).hexdigest(), 16)
    if h < q:
        print(f'\tРазмер хеша (h) в битах = {len(str(h))}')
        return h
    else:
        return 'Error'


def get_sign(a, p, q, h):
    '''
    Вычисляется r = (a^k mod p) mod q,
    а если все слава богу, то и число
    s = (k * h + x * r) mod q.
    '''
    k = generate_amount(q)
    x = generate_amount(q)
    # print(f'\tСлучайное 0 < k < q, k = \n = {k}\n')

    r = fast_module_exp(a, k, p) % q
    if r == 0:
        k = generate_amount(q)
    else:
        s = (k * h + x * r) % q
        if s == 0:
            k = generate_amount(q)
    return r, s, x


def GOST():
    '''Основная логика работы подписывания документа'''
    # Генерируем q размером 256 бит
    q = prime_generate()

    print('\tПолучаем число Q =')
    print(f'= {q}\n\n')

    m = 'hello, my dear!'
    # абонент получает хеш сообщения 0 < h < q
    h = hash(m, q)
    print(f'\tХеш (h): {h}\n\n')

    # вызываются функции формирования чисел p, b
    p, b = generate_p_b(q)
    print('\tПолучаем числа p, b...')
    print(f'\t\tp = {p}\n ')
    print(f'\t\tb = {b}\n\n')

    # из полученных p, b формируется число а
    a = get_a(p, b)
    print('\tПолучаем число a')
    print(f'\t\ta = {a}\n\n')

    r, s, x = get_sign(a, p, q, h)
    print('\n\nДокумент подписан.\n')

    choice = int(input('Если желаете увидеть проверку, нажмите 1  '))
    if choice == 1:
        test_GOST(r, s, q, h, a, x, p)
    else:
        return 'Проверки видимо не будет.'


if __name__ == "__main__":
    GOST()
