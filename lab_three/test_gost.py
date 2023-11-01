'''
    Проверка подписи по алгоритму ГОСТ.
'''
from castom_lab_one import fast_module_exp


def test_GOST(r, s, q, h, a, x, p):
    '''Проверка подписи.'''
    print('\nШаг 1. Вычисляем h = H(m).')
    print(f'\tХеш функция: {h}')

    print('\nШаг 2. Проверяем неравенство 0 < r, s < q.')
    if 0 < r and s < q:
        print('\tr > 0, s < q')
        print('\tвычисляем далее...')
    else:
        print('\tДействительно ошибка :(')

    print('\nШаг 3. Вычисляем u...')
    u_s = (s * pow(h, -1, q)) % q
    u_r = (-r * pow(h, -1, q)) % q
    # print(f'\tu_s = {u_s}')
    # print(f'\tu_r = {u_r}')

    print('\nШаг 4. Вычисляем v...')
    y = fast_module_exp(a, x, p)
    r1 = fast_module_exp(a, u_s, p)
    r2 = fast_module_exp(y, u_r, p)
    result = (r1 * r2) % p
    v = result % q

    print('\nШаг 5. Сравниваем полученные значения.')
    if v == r:
        print('Подпись документа прошла успешно!')
    else:
        print('Ошибка подписи :(')
