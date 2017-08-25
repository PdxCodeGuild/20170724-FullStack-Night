#   Lab 18  BlackJack Advice

import random

'''                                     In progress, buggy as I need to execute the total value for each cards as it happening
def ace_value(card):
    cards = 0
    total = 0
    while total < 22:
        if card == 'A':
            if total < 11:
                card_value = 11
                total += card_value
                cards += 1
                return card_value
            elif total > 11:
                card_value = 1
                total += card_value
                cards += 1
                return card_value
'''


def card_value(card):
    '''
    card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    card_index = card_list.index(card)
    card_value = card_values[card_index]

    return card_value

'''
    if card == 'A':
        card_value = ace_value(card)
        return card_value
    if card == 'J' or 'Q' or 'K':
        card_value = 10
        return card_value
    else:
        card = int(card)
        card_value = card
        return card_value


def random_card():
    random_cards = []
    i = 0
    while i < 3:
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card = random.choice(cards)
        random_cards.append(card)        # password = password + character
        i = i + 1                        # add i until it reaches n
    #print(random_cards)
    card_1 = random_cards[0]
    card_2 = random_cards[1]
    card_3 = random_cards[2]
    return card_1, card_2, card_3


def advice_reference(total):
    if total < 17:
        return 'Hit'
    elif 21 > total >= 17:
        return 'Stay'
    elif total == 21:
        return 'Blackjack'
    elif total > 21:
        return 'Already Busted'


def main():
    card_1, card_2, card_3 = random_card()
    print(card_1, card_2, card_3)

    card_1_value = card_value(card_1)
    #print(card_1_value)
    card_2_value = card_value(card_2)
    #print(card_2_value)
    card_3_value = card_value(card_3)
    #print(card_3_value)

    total = card_1_value + card_2_value + card_3_value
    #print(total)

    advice = advice_reference(total)
    print(advice)


main()
