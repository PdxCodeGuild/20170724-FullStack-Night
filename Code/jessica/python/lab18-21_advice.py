def value_cards(card):
    if card == 'A':
        return 1
    elif card == '2':
        return 2
    elif card == '3':
        return 3
    elif card == '4':
        return 4
    elif card == '5':
        return 5
    elif card == '6':
        return 6
    elif card == '7':
        return 7
    elif card == '8':
        return 8
    elif card == '9':
        return 9
    elif card == 'J':
        return 10
    elif card == 'Q':
        return 10
    elif card == 'K':
        return 10
    return int(card)


def main():
    card1 = input('What is your first card? \n')
    card2 = input('What is your second card? \n')
    card3 = input('What is your third card? \n')

    total_cards = value_cards(card1) + value_cards(card2) + value_cards(card3)

    print(total_cards)
    if total_cards < 17:
        print('hit')
    elif total_cards < 21:
        print('stay')
    elif total_cards == 21:
        print('Blackjack!')
    elif total_cards > 21:
        print('Already Busted')



main()

