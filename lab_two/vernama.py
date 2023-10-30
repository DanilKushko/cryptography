import random


def generate_random_key(message_length):
    '''Генерация случайного ключа заданной длины'''
    key_bytes = []

    for _ in range(message_length):
        random_byte = random.randint(0, 255)
        key_bytes.append(random_byte)

    key = bytes(key_bytes)
    print(f'Сгенерированный ключ: {key}')
    return key


def encrypt(message, key):
    '''Проверка, что длина сообщения и ключа совпадает'''
    if len(message) != len(key):
        raise ValueError('Длина сообщения и ключа должна совпадать.')
    print(message ^ key)
    encrypted_message = []
    for m, k in zip(message, key):
        encrypted_byte = m ^ k
        encrypted_message.append(encrypted_byte)

    encrypted_message_bytes = bytes(encrypted_message)
    return encrypted_message_bytes


def decrypt(encrypted_message, key):
    '''Проверка, что длина зашифрованного сообщения и ключа совпадает'''
    if len(encrypted_message) != len(key):
        raise ValueError('Длины сообщений и ключей не должны совпадать.')

    decrypted_message = []
    for e, k in zip(encrypted_message, key):
        decrypted_byte = e ^ k
        decrypted_message.append(decrypted_byte)

    decrypted_message_bytes = bytes(decrypted_message)
    return decrypted_message_bytes


if __name__ == '__main__':
    message = input('Введите сообщение: ')
    message_bytes = message.encode('utf-8')

    key = generate_random_key(len(message_bytes))

    encrypted_message = encrypt(message_bytes, key)
    decrypted_message = decrypt(encrypted_message, key)

    print(f'Исходное сообщение: {message_bytes.decode("utf-8")}')
    print(f'Зашифрованное сообщение: {encrypted_message}')
    print(f'Расшифрованное сообщение: {decrypted_message.decode("utf-8")}')
