theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
            }

#printBoard function
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
# for loop which updates the board after every turn, for a max of 9 turns for 9 spaces
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

#calling printBoard function by passing theBoard as arg val 
printBoard(theBoard)