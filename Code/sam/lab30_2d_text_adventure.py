import random

width = 10 # the width of the board
height = 10 # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = [] # start with an empty list
for i in range(height): # loop over the rows
    board.append([]) # append an empty row
    for j in range(width): # loop over the columns
        board[i].append(' ') # append an empty space to the board

# define the player position
player_i = 4
player_j = 4


riddles = []
for i in range(3):
    riddle_i = random.randint(0, height-1)
    riddle_j = random.randint(0, width-1)
    board[riddle_i][riddle_j] ='*'
    riddles.append([riddle_i, riddle_j])


def random_riddle():
    riddle_list = ['What flies without wings?',
                   'What goes through towns and over hills but never moves?',
                   'What has cities, but no houses; forests, but no trees; and water, but no fish?']
    answers = ['time', 'a road', 'a map']
    riddle_id = random.randint(0, len(riddle_list)-1)
    user_input = input(riddle_list[riddle_id]).lower().strip()
    if user_input == answers[riddle_id]:
        print('Correct!')
        return True
    else:
        print('Wrong!')
        return False






# loop until the user says 'done' or dies
while True:
    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ') # otherwise print the board square
        print()


    command = input('what is your command? ') # get the command from the user

    if command == 'done':
        break # exit the game
    elif command == 'left':
        if player_j > 0:
            player_j -= 1 # move left
    elif command == 'right':
        if player_j < width-1:
            player_j += 1 # move right
    elif command == 'up':
        if player_i > 0:
            player_i -= 1 # move up
    elif command == 'down':
        if player_i < height-1:
            player_i += 1 # move down

    for i in range(len(riddles)):
        if player_i == riddles[i][0] and player_j == riddles[i][1]:
            print('--RIDDLE--')
            random_riddle()


            break

