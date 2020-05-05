#Colton Fitzjarrald

import tictactoeModule

#opening lines. gets players names and shows the numerical outline of the board.
print('This program will allow two players to play the game of tic-tac-toe.')
print('player 1 has \'X\', and player 2 has \'O\'. ')
player1 = input('Enter the name of player 1:')
player2 = input('Enter the name of player 2:')
print('Enter your mark using the board positions shown below')
display_board(locations)


symbol = 'X'
print(player1, 'you start. You are playing as \'X\'.')        #the three lines preceeding the while loop assign an initial string value for symbol, and provide a current display of the board.
display_board(board)

#while loop switches back and forth between the players and checks for winning moves and a tie game.
while win(board, symbol) is not True and tie_game is not True:
    symbol = 'X'
    get_move(board, locations, player1)
    if win(board, symbol) is True:
        print('%s, you win!' % player1)
        break
    elif tie_game(board) is True:
        print('We have a tie!')
        break
    else:
        symbol = 'O'
        get_move(board, locations, player2)
        if win(board, symbol) is True:
            print('%s, you win!' % player2)
            break
        elif tie_game(board) is True:
            print('We have a tie!')
            break

