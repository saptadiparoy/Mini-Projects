import random
#create and display the board for tic tac toe game

def display_board(board):
    print ("\n"*5)
    print(board[1] + '|' + board[2] + '|' + board[3])
    #print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    #print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

#assign markers to players
def player_input():
    #keep asking player1 to choose X or O
    marker = '' 
    while marker != 'X' and marker != 'O':
        marker = input("Player1: X or O?:    ").upper()

    #assign player2 the opposite marker
    player1 = marker
    if player1 == "X":
        player2 = "O"

    else:
        player2 = "X"
        
    return(player1,player2)

#function to place marker on board as per given position
def place_marker(board, marker, position ):
    board[position] = marker

test_board = ["#", 'X', 'O', 'X', 'O','X', 'O', 'X', 'O', 'X']
"""place_marker(test_board, '%', 8)
display_board(test_board)"""

#a function to check wins
def win_check(board ,mark):
    #all row, column and diagonal combos
    #rows
    return ((board[1] == board[2] == board[3] == mark) or #first row
            (board[4] == board[5] == board[6] == mark) or #second row
            (board[7] == board[8] == board[9] == mark) or #third row
            (board[1] == board[4] == board[7] == mark) or #first column
            (board[2] == board[5] == board[8] == mark) or #second column
            (board[3] == board[6] == board[9] == mark) or #third column
            (board[1] == board[5] == board[9] == mark) or #left diagonal
            (board[3] == board[5] == board[7] == mark)) #right diagonal

#function to randomly choose a player to go first
def choose_first():
    choose = random.randint(1,2)
    if choose == 1:
        return 'player1'
    else :
        return 'player2'
    
#function to check if space on board is free
def space_check(board , position):
    return board[position] == " "

#a function to check if the board is full
def full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#fucntion that asks for players next position and then space checks, if blank return
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Enter a position to place your marker:    "))

    return position

#function to ask if players want to replay
def replay():
    choice = input("Continue Playing? (Y/N):    ").upper()
    return choice == "Y"

#compiling all functions to make the game
#while loop to keep the game running
print ("Welcome to Tic-Tac-Toe!")
while True:
    #play the game

    ##set the board
    board = [" "]*10
    player1_marker, player2_marker = player_input()

    turn  = choose_first()
    print (turn + "Will go first!")

    play_game = input("Start game? (Y/N):  ").upper()
    if play_game == "Y":
        game_on = True

    else:
        game_on = False

    #game play
    while game_on:
        if turn == "Player 1":
            #displaying the board
            display_board(board)

            #choose a position
            position = player_choice(board)

            #place the marker at the position
            place_marker(board, player1_marker, position)

            #check if they won
            if win_check(board , player1_marker):
                display_board(board)
                print ("Player 1 Won!")
                game_on = False
            
            else:
                if full_check(board):
                    display_board

                    print ("TIE!!")

                else:
                    turn = "Player 2"

        else:
            #displaying the board
            display_board(board)

            #choose a position
            position = player_choice(board)

            #place the marker at the position
            place_marker(board, player2_marker, position)

            #check if they won
            if win_check(board , player2_marker):
                display_board(board)
                print ("Player 2 Won!")
                game_on = False
            
            else:
                if full_check(board):
                    display_board

                    print ("TIE!!")

                else:
                    turn = "Player 1"

    if not replay():
        print("Goodbye!")
        break


