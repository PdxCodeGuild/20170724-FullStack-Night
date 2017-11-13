#   Lab 30  Adventure Game

# set the game board
# define the pieces
# define the enemies
# define the movement of pieces/enemies
# define the actions


import random



class Entity:
    def __init__(self, i, j, health, attack, defense):
        self.i = i
        self.j = j
        self.health = health
        self.attack = attack
        self.defense = defense

    def character_create(self):

        print('Warrior \n'
                 'Warlock \n'
                 'Warm-blood')
        p = input('Pick a primary class ').lower()

        print('Light \n'
                   'Shadow \n'
                   'Astral')
        s = input('Pick your beginning ').lower()
        primary_class = ['warrior', 'warlock', 'warm-blood']
        sub_class = ['light', 'shadow', 'astral']
        # weapon = []

        if p == primary_class[0]:
            self.health += 6
            self.defense += 2
        elif p == primary_class[1]:
            self.health += 8
            self.defense -= 1
            self.attack += 2
        elif p == primary_class[2]:
            self.health += 10
            self.defense -= 1

        if s == sub_class[0]:
            self.health += 2
        elif s == sub_class[1]:
            self.defense += 2
        elif s == sub_class[2]:
            self.attack += 2

    def __str__(self):
        return f'health: {self.health}, attack: {self.attack}, defense: {self.defense}'


def create_board():
    width = 11 # the width of the board
    height = 11  # the height of the board

    # create a board with the given width and height
    # we'll use a list of list to represent the board
    board = []  # start with an empty list
    for i in range(height):  # loop over the rows
        board.append([])  # append an empty row
        for j in range(width):  # loop over the columns
            board[i].append(' ')  # append an empty space to the board
    for i in range(4):
        enemy_i = random.randint(0, height - 1)
        enemy_j = random.randint(0, width - 1)
        board[enemy_i][enemy_j] = '§'
    return height, width, board






def enemy_name():
    enemies = ['Yellow Snake', 'Red Snake', 'Blue Snake', 'Silly Snake']
    pass


def roll_die():
    return random.randint(1,6)


def damage_counter():
    pass


def battle(player, enemy):
    result = ''
    print(f'You\'ve encountered an enemy with {enemy.health} health!')
    print(f'Your health is: {player.health}')
    print(f'Enemy health is: {enemy.health}')
    while True:
        print('attack, run, play dead')
        action = input('what will you do? ')
        if action == 'run':
            break
        if action == 'play dead':
            result = 'dead'
            break
        if action == 'attack':
            player_die = roll_die()
            enemy_die = roll_die()
            print(f'Player rolled {player_die}')
            print(f'Enemy rolled {enemy_die}')
            if player_die == enemy_die:
                continue
            elif player_die > enemy_die:
                damage = player_die - enemy_die
                enemy.health -= damage
            elif player_die < enemy_die:
                damage = enemy_die - player_die
                player.health -= damage
            print(f'Player Health: {player.health}\n'
                  f'Enemy Health: {enemy.health}')
            if player.health <= 0:
                result = 'dead'
                break
            elif enemy.health <= 0:
                result = 'won'
                break

    return result


def main():
    height, width, board = create_board()
    #enemy = Entity(random.randint(0, height), random.randint(0, width), 5, 0, 0)  # enemy initializes the Class Entity with parameters of position i, j health, attack, defense


    player = Entity(5, 5, 0, 0, 0)           # player intitializes the Class Entity with parameters of position i, j health,
    player.character_create()
    print(player)

    # loop until the user says 'done' or dies
    while True:

        command = input('what is your command? ')  # get the command from the user

        if command == 'done':
            break  # exit the game
        elif command == 'left':
            player.j -= 1  # move left
        elif command == 'right':
            player.j += 1  # move right
        elif command == 'up':
            player.i -= 1  # move up
        elif command == 'down':
            player.i += 1  # move down
        # check if the player is on the same space as an enemy
        if board[player.i][player.j] == '§':
            enemy = Entity(random.randint(0, height), random.randint(0, width), 5, 0, 0)
            result = battle(player, enemy)
            if result == 'won':
                print('you\'ve slain the enemy')
                board[player.i][player.j] = ' '
            elif result == 'dead':
                print('You hesitated and were slain.')
                print('Game Over')
                break
                # print out the board
        for i in range(height):
            for j in range(width):
                # if we're at the player location, print the player icon
                if i == player.i and j == player.j:
                    print('☺', end=' ')
                else:
                    print(board[i][j], end=' ')  # otherwise print the board square
            print()

main()

