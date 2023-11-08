'''
    Проверка подписи по алгоритму Эль-Гамаля.
'''
from castom_lab_one import fast_module_exp


def test_el_gamal(y, r, s, g, h, P):
    '''Проверка подписи.'''
    print('\nШаг 1. Вычисляем h = H(m).')
    print(f'\tХеш функция: {h}')

    print('\nШаг 2. Проверяем равенство y^r * r^s = g^h (mod P).')
    temp1 = (fast_module_exp(y, r, P) * fast_module_exp(r, s, P)) % P
    temp2 = fast_module_exp(g, h, P)
    if temp1 == temp2:
        return False
    else:
        return True
