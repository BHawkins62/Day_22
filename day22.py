# --- Day 22: Crab Combat ---

import numpy as np

nl: str = '\n'


def filter_list(arr):
    f_list = []
    for element in arr:
        try:
            int(element)
            f_list.append(int(element))
        except ValueError:
            pass
    return f_list


def sum_of(a_list):
    np_a = np.flip(np.array(a_list))
    np_b = np.arange(1, len(np_a) + 1)
    return np.sum(np_a * np_b)


read_file = open('input.txt', 'r', encoding='utf-8')
data = list(map(str, read_file.read().split('\n')))
data_elements = int(len(data) / 2) - 2
all_cards = filter_list(data)
player1 = all_cards[:data_elements]
player2 = all_cards[data_elements:]
while player1 and player2:
    if player1[0] > player2[0]:
        player1.append(player1.pop(0))
        player1.append(player2.pop(0))
    elif player1[0] < player2[0]:
        player2.append(player2.pop(0))
        player2.append(player1.pop(0))
if player1:
    print(f'Player 1 wins with a score of {sum_of(player1)}')
else:
    print(f'Player 2 wins with a score of {sum_of(player2)}')
