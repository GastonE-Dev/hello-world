theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L' : ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# This is the empty Tic Tac Toe board, as per Chapter 5.

# The following code was added in later, we create a function to print the board dictionary onto the screen.






def printBoard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])

    print('-+-+-')

    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])

    print('-+-+-')

    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# Added the following function to check if either 'X' or 'O' player has won, and if so, print a message indicating so.

def checkWin(board):
    # Horizontal lines
    if (board['top-L'] == board['top-M'] == board['top-R'] != ' ' or
        board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ' or
        board['low-L'] == board['low-M'] == board['low-R'] != ' '):
            return True
    # Vertical lines
    if (board['top-L'] == board['mid-L'] == board['low-L'] != ' ' or
        board['top-M'] == board['mid-M'] == board['low-M'] != ' ' or
        board['top-R'] == board['mid-R'] == board['low-R'] != ' '):
            return True
    # Diagonal lines
    if (board['top-L'] == board['mid-M'] == board['low-R'] != ' ' or
        board['top-R'] == board['mid-M'] == board['low-L'] != ' '):
            return True
    return False


printBoard(theBoard)


# The following code was added last, it allows players to enter their moves.


turn = 'X'
won = False

for i in range(9):

    printBoard(theBoard)

    print('Turn for ' + turn + '. Move on which space?')

    move = input()

    theBoard[move] = turn

    if checkWin(theBoard):
        won = True
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

if won:
    print('Player', turn, 'has won!')
