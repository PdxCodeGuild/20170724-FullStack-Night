import random

width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4
player_inventory = {}
treasure_count = 0

# add 4 enemies in random locations
for i in range(random.randint(10, 50)):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

treasure_amount = random.randint(5, 25)
for i in range(treasure_amount):
    treasure_i = random.randint(0, height - 1)
    treasure_j = random.randint(0, width - 1)
    board[treasure_i][treasure_j] = 'φ'


def find_treasure():
    treasures = ['gold piece', 'sword', 'silver ring', 'beer']
    generate_treasure = random.choice(treasures)
    return generate_treasure

# loop until the user says 'done' or dies
while True:
    command = input('what is your command? ')  # get the command from the user
    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player_j -= 1  # move left
    elif command == 'right':
        player_j += 1  # move right
    elif command == 'up':
        player_i -= 1  # move up
    elif command == 'down':
        player_i += 1  # move down
    elif command == 'check inventory':
        for treasure in player_inventory:
            print(f'{treasure}: {player_inventory[treasure]}')

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hesitated and were slain')
            break

    # check is player is on the same space as the treasure
    if board[player_i][player_j] == 'φ':
        print('You found something!')
        inventory_items = list(player_inventory.items())
        treasure = find_treasure()
        action = input('What will you do? ')
        if action == 'pick up':
            print(f'It\'s a new {treasure} for your adventure!')
            board[player_i][player_j] = ' '  # remove the treasure from the board
            treasure_count += 1
            if treasure not in player_inventory:
                player_inventory[treasure] = 1
            else:
                player_inventory[treasure] += 1

        else:
            print(f'You missed out on some sweet treasure, it was a {treasure}.')
            break
    if treasure_count == treasure_amount:
        print('Wow! You collected all the treasures, you win!!!!')
        for treasure in player_inventory:
            print(f'{treasure}: {player_inventory[treasure]}')


            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()



