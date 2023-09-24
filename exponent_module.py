'''
1) Функция быстрого возведения числа в степень по модулю
'''
from my_const import a, x, p


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


result = fast_module_exp(x, a, p)
print(f'    Остаток (mod): {result}')
