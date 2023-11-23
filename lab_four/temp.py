from random import randint, shuffle
from prime_generate import prime_generate
from castom_lab_one import miller_test, fast_module_exp, mod_inverse

num_players = 3
num_cards = 6
amount_cards_hand = 2
num_result_cards = num_players * amount_cards_hand


class CardGame:
    '''Базовый класс карточной игры.'''

    def __init__(self):
        self.num_players = num_players
        self.num_cards = num_cards
        self.P, self.Q = self.Sofi_Jermen_P_Q()
        self.keys_c, self.keys_d = self.selection_C_D(self.P, self.num_players)
        self.cards_array = self.create_card_dict(self.P)

        print('\nКолода до шифрования:')
        print(self.cards_array)

        self.encrypted_cards_dict = self.player_encrypts_card()

    def Sofi_Jermen_P_Q(self):
        '''Генерация числа Софи-Жермен.'''
        print('Начинаем генерацию чисел P, Q...\n')
        while True:
            Q = prime_generate()
            P = 2 * Q + 1
            if miller_test(P, self.num_cards):
                print(f'\tЧисла\n\tP = {P},\n\tQ = {Q}\n')
                return P, Q

    def create_card_dict(self, P):
        '''Создание колоды карт.'''
        card_dict = {}
        for i in range(self.num_cards):
            card = randint(2, P - 1)
            card_dict[f'{i + 1} карта'] = card

        print('\n\tПолученные карты в колоду: ')
        for key, value in card_dict.items():
            print("{0}: {1}".format(key, value))

        return list(card_dict.values())

    def selection_C_D(self, P, n):
        key_c_dict = {}
        key_d_dict = {}
        for i in range(n):
            C, D = mod_inverse(P)
            key_c_dict[i + 1] = C
            key_d_dict[i + 1] = D

        print('\tИгроки подтверждают игру:\n')
        for key, value in key_c_dict.items():
            print("{0}: {1}".format(key, value))

        return key_c_dict, key_d_dict

    def player_encrypts_card(self):
        '''Игроки шифруют и мешают карты.'''
        encrypted_cards_dict = {}
        print('\n\tИгроки приступили к шифрованию и перемешиванию...')

        prev_player_cards = self.cards_array
        for player, key_value in self.keys_c.items():
            player_cards = list(prev_player_cards)
            for i in range(self.num_cards):
                player_cards[i] = fast_module_exp(
                    player_cards[i], key_value, self.P
                )
            shuffle(player_cards)
            encrypted_cards_dict[player] = list(player_cards)
            prev_player_cards = encrypted_cards_dict[player]

        return encrypted_cards_dict

    def distribute_cards(self):
        '''Раздача карт на спавне.'''
        distribute_dict = {i + 1: [] for i in range(self.num_players)}

        last_player_cards = list(self.encrypted_cards_dict.values())[-1]

        for i in range(amount_cards_hand):
            for player_number in range(1, self.num_players + 1):
                if last_player_cards:
                    distribute_dict[player_number].append(
                        last_player_cards.pop(0)
                    )

        return distribute_dict

    def decipher_card(self, distribute_dict, keys_d):
        '''Расшифровка карт каждым игроком по очереди.'''
        all_cards = []
        for player_cards in distribute_dict.values():
            all_cards.extend(player_cards)

        for player, d_key in self.keys_d.items():
            for i in range(len(all_cards)):
                decrypted_card = fast_module_exp(all_cards[i], d_key, self.P)
                all_cards.append(decrypted_card)

        decrypted_cards = all_cards[-num_result_cards:]

        return decrypted_cards

    def check_results(self, decrypted_cards):
        '''Проверка успешной расшифровки.'''
        if set(decrypted_cards) == set(self.cards_array):
            print('Расшифровка карт прошла успешно')
        else:
            print('Расшифровка карта не удалась')


if __name__ == '__main__':
    game = CardGame()

    print('\nКолода после шифрования:')
    for player, cards in game.encrypted_cards_dict.items():
        print(f'{player}: {cards}')

    distribute_dict = game.distribute_cards()
    print('\nРаздаем карты каждому игроку:')
    for player, cards in distribute_dict.items():
        print(f'Игрок {player}: {cards}')

    decrypted_cards = game.decipher_card(distribute_dict, game.keys_d)
    print('\nРасшифрованные карты игроков:')
    print(decrypted_cards)

    game.check_results(decrypted_cards)
