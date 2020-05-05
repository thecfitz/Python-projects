# Colton Fitzjarrald

# winning_numbers comprises all of the numerical lists in locations that win the game.
winning_numbers = {
    'row1': ['1', '2', '3'], 'row2': ['4', '5', '6'], 'row3': ['7', '8', '9'],
    'column1': ['1', '4', '7'], 'column2': ['2', '5', '8'], 'column3': ['3', '6', '9'],
    'cross1': ['1', '5', '9'], 'cross2': ['3', '5', '7']
}

# gives numerical values for each index when iterated with board.
locations = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


# 2nd for loop displays the current status of the board. Displays '-' for all empty spaces. 1st for loop displays numerical values for each 'space' on the board.
def display_board(board):
    if board == locations:
        for row in locations:
            for column in row:
                    print(column, end=' ')
            print()
    else:
        for row in board:
            for index, column in enumerate(row):
                if column == 'X':
                    print(column, end=' ')
                elif column == 'O':
                    print(column, end=' ')
                else:
                    row[index] = '-'
                    print(row[index], end=' ')
            print()


def get_move(board, locations, player):
    # inputs 'x' or 'o' into the board, and then displays the current board.
    # the for loops find the index of user input in locations and then assigns the appropriate symbol to the coordinating index of board.
    execution = 0
    print('%s, enter your move:' % player, end='')
    position = input()
    if '1' <= position <= '9' and len(position) == 1:
        display = 0
        if player == player1:
            for nested_list, row in enumerate(locations):
                for index, column in enumerate(row):
                    while column == position and execution == 0:        #while loop makes if/else statement only execute at correct index. execution increment is for infinite loop.
                        execution += 1
                        if board[nested_list][index] == '-':             #if/else statement checks if space is taken.
                            board[nested_list][index] = 'X'
                        else:
                            print('Invalid. There is already a piece in that location.')
                            get_move(board, locations, player1)
                            display += 1
        elif player == player2:
            for nested_list, row in enumerate(locations):
                for index, column in enumerate(row):
                    while column == position and execution == 0:
                        execution += 1
                        if board[nested_list][index] == '-':
                            board[nested_list][index] = 'O'
                        else:
                            print('Invalid. There is already a piece in that location.')
                            get_move(board, locations, player2)
                            display += 1
        while display == 0:                                      # The while 'display' loop and display incrementation in for loops is to prevent excessive calling of display_board.
            display_board(board)
            display += 1
    else:
        print('Invalid move. Try again.')
    return


def win(board, symbol):
    # two_step function. first loop iterates board for all 'X''O' inputs, then obtains indices, then relates them to location's indices, returns the values at those indices, and appends them to the empty place-value.
    #Second loop uses dict.values() function to return an ordered list of key values that can then be iterated like a nested list. Win_meter keeps track of how many elements in a particular dictionary key's value exist inside of place_value.
    place_value = []
    for nested_list, row in enumerate(board):
        for index, column in enumerate(row):
            if column == symbol:
                place_value.append(locations[nested_list][index])
    for key in winning_numbers.values():
        win_meter = 0
        for value in key:
            if value in place_value:
                win_meter += 1
                if win_meter == 3:
                    return True


def tie_game(board):
    # for loop iterates through board and increments empty_spot for every '-' on the board. Once empty_spot = 0, the game is tied.
    empty_spot = 0
    for row in board:
        for index, column in enumerate(row):
            if row[index] == '-':
                empty_spot += 1
    if empty_spot == 0:
        return True
    elif empty_spot != 0:
        return False



