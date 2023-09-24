'''
2) Функция, реализующая обобщённый алгоритм Евклида. Функция
должна позволять находить наибольший общий делитель и обе
неизвестных из уравнения
'''
from my_const import a, b


def GCD(a, b):
    if b != 0:
        return GCD(b, a % b)
    else:
        return a


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


# a = float(input('Введите число А: '))
# b = float(input('Введите число B: '))

gcd_value = GCD(a, b)
extended_gcd_values = extended_gcd(a, b)


# print(f'Наибольший общий делитель: {gcd_value}')
# print(f'Расширенный алгоритм Евклида:'
#       f' x = {extended_gcd_values[1]}, y = {extended_gcd_values[2]}')
def resulteuclid():
    print(f'Результат: gcd⁡({a},{b}),x,y)='
          f'({extended_gcd_values[1]},{extended_gcd_values[2]})')


resulteuclid()
