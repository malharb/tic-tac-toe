#tic tac toe by Malhar started: 27/09/19. *finished 28/09/19


def board(gboard):
    print("\n"*100)
    print(gboard[7]+'|'+gboard[8]+'|'+gboard[9])
    print(gboard[4]+'|'+gboard[5]+'|'+gboard[6])
    print(gboard[1]+'|'+gboard[2]+'|'+gboard[3])


def outcome(gboard,player1,player2):
    global ini
    if player1 == 'X':
        playerX = "Player 1"
        playerO = "Player 2"
    else:
        playerX = "Player 2"
        playerI = "Player 1"


    if(player1=='X'):
        if(gboard[1] == 'X' and gboard[2] == 'X' and gboard[3] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[4] == 'X' and gboard[5] == 'X' and gboard[6] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[7] == 'X' and gboard[8] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[1] == 'X' and gboard[4] == 'X' and gboard[7] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[2] == 'X' and gboard[5] == 'X' and gboard[8] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[3] == 'X' and gboard[6] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[1] == 'X' and gboard[5] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[3] == 'X' and gboard[5] == 'X' and gboard[7] == 'X'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        ##

        if(gboard[1] == 'O' and gboard[2] == 'O' and gboard[3] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[4] == 'O' and gboard[5] == 'O' and gboard[6] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[7] == 'O' and gboard[8] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[1] == 'O' and gboard[4] == 'O' and gboard[7] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[2] == 'O' and gboard[5] == 'O' and gboard[8] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[3] == 'O' and gboard[6] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[1] == 'O' and gboard[5] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[3] == 'O' and gboard[5] == 'O' and gboard[7] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini


    elif(player1=='O'):
        if(gboard[1] == 'X' and gboard[2] == 'X' and gboard[3] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[4] == 'X' and gboard[5] == 'X' and gboard[6] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[7] == 'X' and gboard[8] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[1] == 'X' and gboard[4] == 'X' and gboard[7] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[2] == 'X' and gboard[5] == 'X' and gboard[8] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[3] == 'X' and gboard[6] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[1] == 'X' and gboard[5] == 'X' and gboard[9] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        if(gboard[3] == 'X' and gboard[5] == 'X' and gboard[7] == 'X'):
            print('The winner is Player 2!')
            ini = 0
            return ini

        ##

        if(gboard[1] == 'O' and gboard[2] == 'O' and gboard[3] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[4] == 'O' and gboard[5] == 'O' and gboard[6] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[7] == 'O' and gboard[8] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[1] == 'O' and gboard[4] == 'O' and gboard[7] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[2] == 'O' and gboard[5] == 'O' and gboard[8] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[3] == 'O' and gboard[6] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[1] == 'O' and gboard[5] == 'O' and gboard[9] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini

        if(gboard[3] == 'O' and gboard[5] == 'O' and gboard[7] == 'O'):
            print('The winner is Player 1!')
            ini = 0
            return ini






def exec():
    move_counter = 0
    global ini
    ini = 1
    winner = 'X'
    outcomes = ['X','O']

    print("Welcome to Tic Tac Toe!")
    print("Here's how the game works:\nEach number on the keypad represents a place on the table.")
    print("For example the number 1 stands for the box in column 1 row 3, while number 6 stands for column 3 row 2.")
    print("You will tell the computer where you wish to play using this system!")
    print("\n"*2+"Here is a visual representation of the board and the key numbers: ")
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')
    print('If you wish to play X in the middle, you tell the computer to place X in position 5. Here is how a blank board will evolve:')
    print(' | | ')
    print(' |X| ')
    print(' | | ')
    print("So. Let's play!")

    player2 = None

    while True:
        player1 = input('Player 1, would you like to be X or O(represents the letter)?: ')
        player1 = player1.upper()
        if player1 == 'X' or player1 == 'O':
            break
        else:
            print("Invalid selection. Please choose again!")

    player1 = player1.upper()
    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    print(f"Ok. Player 1 is {player1} and so that means that Player 2 is {player2}")


    gboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while True:
        move = int(input('Player 1, where would you like to play?: '))
        gboard[move] = player1
        move_counter += 1
        board(gboard)
        outcome(gboard,player1,player2)
        if(ini == 0):
            break
        if(move_counter == 9 and ini == 1):
            print('The game is a TIE!')
            break

        move2 = int(input('Player 2, where would you like to play?: '))
        gboard[move2] = player2
        move_counter += 1
        board(gboard)
        outcome(gboard,player1,player2)

        if(ini == 0):
            break
        if(move_counter == 9 and ini == 1):
            print('The game is a TIE!')
            break





    print('Game over!!')
    print('Thank you for playing!')

def execagain():
    move_counter = 0
    global ini
    ini = 1
    winner = 'X'
    outcomes = ['X','O']

    player2 = None
    player1 = input('Player 1, would you like to be X or O(represents the letter)?: ')
    player1 = player1.upper()
    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    print(f"Ok. Player 1 is {player1} and so that means that Player 2 is {player2}")


    gboard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while True:
        move = int(input('Player 1, where would you like to play?: '))
        gboard[move] = player1
        move_counter += 1
        board(gboard)
        outcome(gboard,player1,player2)
        if(ini == 0):
            break
        if(move_counter == 9 and ini == 1):
            print('The game is a TIE!')
            break

        move2 = int(input('Player 2, where would you like to play?: '))
        gboard[move2] = player2
        move_counter += 1
        board(gboard)
        outcome(gboard,player1,player2)

        if(ini == 0):
            break
        if(move_counter == 9 and ini == 1):
            print('The game is a TIE!')
            break





    print('Game over!!')
    print('Thank you for playing!')


def replay():
    global choice
    choice = input('Would you like to play again? Y/N: ')
    choice = choice.upper()
    if choice == 'Y':
        execagain()
    else:
        print("Okay. Good bye!")

def game():
    global choice
    choice = 'N'
    exec()
    replay()
    while choice == 'Y':
        replay()

game()
input('Press ENTER to exit')
