card1 = input('What is your first card? \n')
card2 = input('What is your second card? \n')
card3 = input('What is your third card? \n')

def value_cards(card1):
    if card1 == 'A':
        return 1
    elif card1 == '2':
        return 2
    elif card1 == '3':
        return 3
    elif card1 == '4':
        return 4
    elif card1 == '5':
        return 5
    elif card1 == '6':
        return 6
    elif card1 == '7':
        return 7
    elif card1 == '8':
        return 8
    elif card1 == '9':
        return 9
    elif card1 == 'J':
        return 10
    elif card1 == 'Q':
        return 10
    elif card1 == 'K':
        return 10
value_card1 = value_cards(card1)
value_card2 = value_cards(card2)
value_card3 = value_cards(card3)

def main():
    total_cards = value_card1 + value_card2 + value_card3
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

