'''
Миллер провалился на тестах :(
'''
import random


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


def miller_test(n, k=50):
    d = n - 1
    for _ in range(k):
        a = 2 + random.randint(0, n - 4)
        x = fast_module_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue

        while d != n - 1:
            x = (x * x) % n
            d *= 2

            if x == 1:
                return False
            if x == n - 1:
                break

        if x != n - 1:
            return False

    return True


def generate_prime():
    while True:
        Q = random.randint(1, 100)
        if miller_test(Q):
            return Q


prime_number = generate_prime()
print("Простое число:", prime_number)
