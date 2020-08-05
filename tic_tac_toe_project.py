#!/usr/bin/env python3
# step 1: write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation

def display_board(board):
    print('-------------')
    for i in range(len(board)-1,0,-3):
        print('|',board[i-2],'|',board[i-1],'|',board[i],'|')
        print('-------------')


#step 2: write a function that can take in a player input and assign their marker as 'X' Or 'O'. keep asking until you get correct answer.

def player_input():
    # Program will accept Player name and Player Mark 'X' or 'O'
    # Accepting first players name
    player1_name=input('Player Name1: ')
    
    #Accepting Player 1 marker, it will keep asking till entering 'X' or 'O'
    player1_marker=''
    while player1_marker not in ['X','O']:
        player1_marker=input('Enter Player Marker: ')
    
    #Accepting Player second players name
    player2_name=input('Player Name2: ')

    
    #Finding second players marker
    #if first player choose 'X' second should choose 'O'
    #if first player choose 'O' second should choose 'X'

    if player1_marker=='O':
        player2_marker='X'
    else:
        player2_marker='O'
    
    
    # Returning player names and Player marker as two list
    return [player1_name,player2_name],[player1_marker,player2_marker]


#step 3: write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assign it to the board.

def place_marker(board, marker, position):
    
    board[position]=marker



#step 4: write a function that takes in a board and a mark (X or O)and then checks to see if that mark has won

import numpy as np
def win_check(board, mark):
    board=board[1:] # Removing fist element('#') of board list 

    board=np.matrix(list(map(lambda x:x==mark,board)))# convert board to matrix in boolean form 
    board.shape=(3,3) # Row matrix is converted in to 3 x 3 matrix

    check_main_dia=np.diagonal(board).all() # checking diagonal one has same mark
    check_main_dia_2=np.diagonal(np.fliplr(board)).all() #checking diagonal two has same mark
    
    check_row=[]
    check_col=[]
    for i in range(3):
        check_row.append(board[i,:].all()) #checking coloumn wise for same mark
        check_col.append(board[:,i].all()) #checking coloumn wise for smae mark
    
    #return true if any of diagonal, coloumn, row has same mark
    return check_main_dia|check_main_dia_2|any(check_row)|any(check_col)
    


#step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to check random.randint(). Return a string of which player went first.

import random

def choose_first():
    return random.randint(0,1)

#step 6: write a function that returns a boolean indicating whether a space on athe board is freely available.

def space_check(board, position):
    # if the position is not marked 
    # it retun True
    # else retuen False

    return board[position] not in ['X','O']

#print(space_check(test_board,8))
#step 7: write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    #Return True when all the point 
    return all(list(map(lambda x:x in['X','O'],board[1:])))
#print(full_board_check(test_board))

#step 8: write a function that asks for player's next position (as a number  1-9) and then uses the function from step 6 to check if it is a free position. If it is, then return the position for later use.

def player_choice(board):

    position=int(input('Enter next position: '))
    while not space_check(board,position):
        position=int(input('Enter next position: '))
    return position

#step 9: write a function that asks thye player if they want to play again and returns boolean Trur if they want to play again

def replay():
    replay=input('Do you want to play again? (Y/N): ')
    return replay.upper()=='Y' 

#step 10: use while loop and functions you have created above to run the game!

print("Welcome to Tic Tac Toe!")
while True:
    board=['#']+[str(i) for i in range(1,10)]
    marker=['X','O']
    
    player_name,player_marker=player_input()
    
    player_index=choose_first()
    
    display_board(board)
    while not full_board_check(board):
        print('----------',player_name[player_index]+'\'s','Trun ----------')
        position=player_choice(board)
        
        place_marker(board,player_marker[player_index],position)
        
        display_board(board)
        if win_check(board,player_marker[player_index]):
            print('*****************************************************')
            print('                  ',player_name[player_index],'won !......')
            print('*****************************************************')
            break

        if player_index==1:
            player_index=0
        else:
            player_index+=1
    else: 
       print('*****************************************************')
       print('                     IT IS A TIE !!!                 ')
       print('*****************************************************')
    if not replay():
        break
  

'''
while True:
    #set the game up here
    #pass

    #while game on:
        #player 1 Turn

        #player 2's Turn
            
            #pass
    #if not replay():
        #break
'''        
