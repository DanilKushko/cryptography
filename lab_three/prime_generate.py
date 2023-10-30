from random import getrandbits, randint
import gmpy2

# Длина числа в битах для генерации
BITS = 156
# Кол-во итерраций проверки на простоту
K = 5


def miller_test(n: int, k: int) -> bool:
    '''
    Проверка числа на простоту с помощью теста Миллера-Рабина.
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


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
    large_prime = generate_prime_and_check(BITS, K)
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
