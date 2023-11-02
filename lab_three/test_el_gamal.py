'''
    Проверка подписи по алгоритму Эль-Гамаля.
'''
from castom_lab_one import fast_module_exp


def test_el_gamal(m, y, r, s, g, h, P):
    '''Проверка подписи.'''
    print('\nШаг 1. Вычисляем h = H(m).')
    print(f'\tХеш функция: {h}')

    print('\nШаг 2. Проверяем равенство y^r * r^s=g^h (mod P).')
    temp1 = pow(y, r + s) % P
    temp2 = fast_module_exp(g, h, P)
    if temp1 == temp2:
        print('Равенство верное.')
    else:
        print('\tОшибка подписи:(')
        print(temp1)
        print(temp2)
        # print(len(str(temp3)))
        # print(len(str(temp4)))
