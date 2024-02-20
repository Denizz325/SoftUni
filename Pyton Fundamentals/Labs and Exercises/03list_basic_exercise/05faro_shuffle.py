cards = input().split()
number_of_shuffles = int(input())


for current_shuffle in range(number_of_shuffles):
    middle_of_deck = len(cards) // 2

    left_part = cards[0:middle_of_deck]
    right_part = cards[middle_of_deck:]

    shuffled_card_list = []
    for card_index in range(len(left_part)):
        shuffled_card_list.append(left_part[card_index])
        shuffled_card_list.append(right_part[card_index])

    cards = shuffled_card_list

print(shuffled_card_list)