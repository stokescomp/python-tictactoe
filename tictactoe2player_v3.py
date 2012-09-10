# I posted it here: http://studio.sketchpad.cc/wXuu2IgJkV
# I turned the game into a repeatable game. A menu pops up and asks if you want to play again. I changed the numbers to 1 - 9 and made it smarter so it will make sure the input is 1 - 9 and not more or less and it tells you if the input isn't a letter at all. I made it show the game board at the begining and also before winning text so you see it when you win. I reinitialize the game board when you start a new game and so I had to use a global variable since the game is in its own function.
# in version 2 I have added 2 player support and I will make it so you can switch to 1 or 2 player moe before you start playing.
#in version 3 we will be adding computer logic so it will try to pick 3 in a row if possible
#make logic to check if there are 2 characters in a row and the third is free. hen use this either to check when you are about to win or if the other player is about to win, then put your move there. If the other player was about to move there then make a comment sanig: You thought you were smart didn't you!
# Python: Tic Tac Toe Game

import random
# initialize board
board = [1,2,3,4,5,6,7,8,9]
current_turn = 1;

def initBoard():
    global board
    # Reinitialize Game Board
    board = [1,2,3,4,5,6,7,8,9]
    #board = ['X','O','O',4,'X',6,'X',8,9]

def show():
    #global board
    print board[0],'|',board[1],'|',board[2]
    print '---------'
    print board[3],'|',board[4],'|',board[5]
    print '---------'
    print board[6],'|',board[7],'|',board[8],"\n"

#for testing the result and returning it in the same place
def test_result(value):
    test_result.the_value = value
    #print "test:" + str(value)
    return value
    
def check_all(char):
    if check_line(char, 0, 1, 2):
        return True
    if check_line(char, 3, 4, 5):
        return True
    if check_line(char, 6, 7, 8):
        return True
    if check_line(char, 0, 3, 6):
        return True
    if check_line(char, 1, 4, 7):
        return True
    if check_line(char, 2, 5, 8):
        return True
    if check_line(char, 0, 4, 8):
        return True
    if check_line(char, 2, 4, 6):
        return True

def check_all_partial(char):
    #print str(test_result(check_line(char, 0, 4, 8, True)))+" checkline"+str(check_line(char, 0, 4, 8, True))
    while test_result(check_line(char, 0, 1, 2, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 3, 4, 5, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 6, 7, 8, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 0, 3, 6, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 1, 4, 7, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 2, 5, 8, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 0, 4, 8, True)) is not False:
        return test_result.the_value
    while test_result(check_line(char, 2, 4, 6, True)) is not False:
        return test_result.the_value
    return False

def check_line(char, spot1, spot2, spot3, partial = False):
    if partial != False:
        #we are checking for 2 in a row to look for a winning move
        #print "checking"+ str(spot1)+","+ str(spot2)+","+ str(spot3)
        count = 0
        spot_not_taken = False
        if board[spot1] == char:
            count += 1
        #if the spot isn't taken check if it is available for current player so we can move there
        elif board[spot1] != 'X' and board[spot1] != 'O':
            spot_not_taken = spot1
        if board[spot2] == char:
            count += 1
        elif board[spot2] != 'X' and board[spot2] != 'O':
            spot_not_taken = spot2
        if board[spot3] == char:
            count += 1
        elif board[spot3] != 'X' and board[spot3] != 'O':
            spot_not_taken = spot3
        #print "end of picking: spot not taken: "+str(spot_not_taken)
        if count == 2:
            return spot_not_taken
        #print "returning false"
        return False
    else:
        #print "checking"+ str(spot1)+","+ str(spot2)+","+ str(spot3)
        if board[spot1] == char and board[spot2] == char and board[spot3] == char:
            return True
    

def menu():
    print "Welcome to a game of TicTacToe.\nMade by Jream and edited by stokescomp"
    userinput = raw_input("Do you want to start a new TicTacToe game? Yes or No: ")
    if userinput.lower() == 'yes':
        while True:
            userinput = raw_input("Do you want to play with 1 or 2 players: ")
            if userinput == '1':
                print "Starting a "+str(userinput)+" player game of TicTacToe"
                start_game(1)
                break
            elif userinput == '2':
                print "Starting a "+str(userinput)+" player game of TicTacToe"
                start_game(2)
                break
            else:
                print "Enter 1 or 2 to pick the number of players\n"
            
    elif userinput.lower() == 'no':
        print "OK, quiting the game ..."
    else:
        print "You didn't answer yes or no\n"
        menu()

def pick_spot(char):
    input = raw_input("Select a spot: ")
    # check for digit only
    if input.isdigit():
        input = int(input)
        if input > 0 and input < 10:
            return input
        else:
            print "Enter a number between 1 and 9"
    else:
        print "You didn't enter a number. Enter a number between 1 and 9"
    return False

        
def check_for_winner(char):
    # check for a winner
    if check_all(char) == True:
        show()
        print "~~ " + char.upper() + " WINS ~~\n\n"
        menu()
        return True
    return False


def play_turn(char):
    #player takes a spot
    print "It is player "+str(current_turn)+"'s turn. Play your "+char
    while True:
        while True:
            input = pick_spot(char)
            if input != False:
                break
        #check player
        if board[input-1] != 'X' and board[input-1] != 'O':
            board[input-1] = char
            if check_for_winner(char) == True:
                return True
            break
        else:
            print 'This spot is taken!'
    return False

def switch_turn():
    global current_turn
    if current_turn == 1:
        current_turn = 2
    else:
        current_turn = 1

def check_cat():
    for x in board:
        #if we find a number then we are still playing and its not a cat
        if type(x) == int:
            return False
    return True

def computer_turn(computer_char):
    if computer_char == 'X':
        player_char = 'O'
    else:
        player_char = 'X'
    #check if computer is about to win then check if the player is abou to win
    computer_winning_place = check_all_partial(computer_char)
    player_winning_place = check_all_partial(player_char)
    #print "computer choices: computer_win_move:" + str(computer_winning_place) + " player_win_move: " + str(player_winning_place)
    #print "computer choices: computer_win_move:" + str(computer_winning_place) + " player_win_move: " + str(player_winning_place) + str(computer_winning_place is not False)
    #print "computer choices: player_win_move: " + str(player_winning_place)
    if computer_winning_place is not False:
        print "got to comp winning"
        return int(computer_winning_place)
    elif player_winning_place is not False:
        print "got in player win"
        print "Ha Ha, I stopped you!"
        return int(player_winning_place)
    else:
        print "got to random"
        random.seed() # Gives a random generator
        return random.randint(0,8)
    

def start_game(number_of_players):
    global board, current_turn
    char = 'X'
    initBoard()
    while True:
        if current_turn == 1:
            char = 'X'
            show()
            if play_turn(char) == True:
                break
        elif current_turn == 2:
            char = 'O'
            if number_of_players == 1:
                while True:
                    opponent = computer_turn(char)
                    #print "move to:"+str(opponent)
                    #print "look at choice place: " + str(board[opponent])+" look at:"+str(opponent)
                    if board[opponent] != 'X' and board[opponent] != 'O':
                        board[opponent] = char
                        if check_for_winner(char) == True:
                            break
                        break
            else:
                show()
                if play_turn(char) == True:
                    break
        if check_cat():
            print "This is a Cat game. Good job.\n"
            menu()
            break
        switch_turn()

#start the menu
menu()
