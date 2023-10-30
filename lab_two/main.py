'''
В этом файле происходит основной запуск всех
частей данной работы. Здесь собраны функции main
файлов:
    shamir.py
    el_gamal.py
    vernama.py
    rsa.py
'''
from shamir import shamir_algorithm
from el_gamal import bob_think
from rsa import alice_think, bob_decryption
from vernama import generate_random_key, encrypt, decrypt
from lib_lab_one import generate_prime


def shamir_start():
    p = generate_prime()

    if p < 2:
        print('p должно быть больше или равно 2')
    else:
        P = shamir_algorithm(p)
        print(P)


def el_gamal_start():
    bob_think()


def vernama_start():
    message = input('Введите сообщение: ')
    message_bytes = message.encode('utf-8')

    key = generate_random_key(len(message_bytes))

    encrypted_message = encrypt(message_bytes, key)
    decrypted_message = decrypt(encrypted_message, key)

    print(f'Исходное сообщение: {message_bytes.decode("utf-8")}')
    print(f'Зашифрованное сообщение: {encrypted_message}')
    print(f'Расшифрованное сообщение: {decrypted_message.decode("utf-8")}')


def rsa_start():
    Pb, Qb, N, d, c = bob_think()
    print(f'Публичные ключи Боба: P = {Pb}, Q = {Qb}')
    print(f'Закрытый и открытый ключи Боба: d = {d}, c = {c}')

    e, m = alice_think(Pb, Qb, N, d, c)
    print(f'Алиса отправляет зашифрованное сообщение (e): {e}')
    print(f'Сообщение Алисы: m = {m}')

    result = bob_decryption(e, c, N, m)
    print(f'Боб дешифровал сообщение: {result}')


if __name__ == '__main__':
    print('Добро пожаловать в мою в 2-ю лабораторную работу!')
    print('Пожалуйста, выбирайте часть л.р. ...')

    choice = int(input('Введите целое число от 1 - 4: '))
    if choice == 1:
        shamir_start()
    if choice == 2:
        el_gamal_start()
    if choice == 3:
        vernama_start()
    if choice == 4:
        rsa_start()
    else:
        print('Ошибка, такой части работы нет')
