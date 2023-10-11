'''
2) Функция, реализующая обобщённый алгоритм Евклида. Функция
должна позволять находить наибольший общий делитель и обе
неизвестных из уравнения
'''
from my_const import a, b


def extended_euclidean(a, b):
    U = [a, 1, 0]
    V = [b, 0, 1]
    T = [0, 0, 0]
    q = 0

    while V[0] != 0:
        q = U[0] // V[0]
        T[0] = U[0] % V[0]
        T[1] = U[1] - q * V[1]
        T[2] = U[2] - q * V[2]

        for i in range(3):
            U[i] = V[i]
            V[i] = T[i]

    return U


result = extended_euclidean(a, b)


def resulteuclid():
    print(f'Результат НОД: {result[0]}')
    print(f'Результат: gcd⁡({a},{b}),x,y)='
          f'({result[1]},{result[2]})')


resulteuclid()
