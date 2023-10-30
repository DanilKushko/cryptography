from hashlib import sha256
from random import randint

from lib_lab_one import generate_prime, extended_euclidean, fast_module_exp


def generate_P_Q():
    '''Генерация P, Q'''
    P = generate_prime()
    Q = generate_prime()
    while P == Q:
        Q = generate_prime()
    print('Числа P, Q получены!')
    return P, Q


m = 'Hello'
h = int(sha256(m.encode('utf-8')).hexdigest(), 16)
print(h)
print('Сейчас сгенерируются числа P, Q, P != Q...')
P, Q = generate_P_Q()
print(f'Числа получены. P = {P}, Q = {Q}.')
N = P * Q
print(N)