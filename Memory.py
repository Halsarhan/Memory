"""This is a 4 x 4 memory game that has the number 1-16 representing cards
and letters A-H representing objects that could be matching if two similar
ones are picked at the same time. When the user wins by having all the 
cards flipped and uncovered, the program congragulates him, tells him
how much time and how many trials it took him to finish the game.
"""

#Hamza Alsarhan
#05/12/14


import random
import time


LETTERS = ['A','B','C','D','E','F','G','H','A','B','C','D','E','F','G','H']
CARD_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def number_board():
    """
    Prints a the 4-4 number board with numbers 1-16
    """
    num_board =   '1  2  3  4  ' + '\n' + '5  6  7  8  ' + '\n' \
           + '9  10 11 12 ' + '\n' + '13 14 15 16 '
 
    return num_board
 
    
def letter_board():
    """
    Assigns letter A-H to each number in the number_board, and creates 
    a letter board underneath the number board.
    """
    random.shuffle(LETTERS) #shuffles letters and makes the order random
    
    num_letter = {1:'', 2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:'', 9:'', 10:'', 11:'', 12:'', 13:'', 14:'', 15:'', 16:''}
       
    
    for i in range(1, len(LETTERS)+1):
       
        num_letter[i] = LETTERS[i-1]
    
    return num_letter



def game():
    """
    Inquires the user for 2 guesses to show the letters under the cards.
    Counts guesses the user makes. Also, changes numbers in the CARD_NUMS
    list to guessed letters and print the most recent number_board on the 
    screen. It also checks for validity of user entries. 
    """
    
    guesses = 0  #sets num of guesses to zero
    num_board = number_board()
    num_letter = letter_board()
   
    #create a new variable for game_on and set it equal to a binary number"
    game_on = 1
    
    while game_on == 1: #start of game, will end when game_on != 1
                 
        print 100*'\n'
        print num_board  
        num_of_squares ='\n' + raw_input("""Guess 2 different numbers:  """)        
       
        response = num_of_squares.split() #to separate the two numbers
        
        #Changes user guesses from strings to integers. 
        for num_square in range(0, len(response)):
            response[num_square] = int(response[num_square]) 
      
        #checks validity of user entry    
        while response[1] not in CARD_NUMS or response[0] \
        not in CARD_NUMS or response[1] == response[0]:
            num_of_squares = raw_input("Invalid guess, please try again: ")
            
            response = num_of_squares.split()                
            
            #Changes other user guesses from strings to integers            
            for num_square in range(0, len(response)):
                response[num_square] = int(response[num_square])             
      
      
        if num_letter[response[0]] == num_letter[response[1]]: #if letters match
        
            for i in range(2):
                
                if len(str(response[i])) == 2:
                    space = ' '
                elif len(str(response[i])) == 1:
                    space = '  '                        
                
                num_block = str(response[i]) + space
    
                letter_block = num_letter[response[i-1]] + '  '
                
                num_board = num_board.replace(num_block, letter_block, 1)
            
                CARD_NUMS[response[i]-1] = LETTERS[response[i]-1]
        
        else:
            old = num_board #save current board and change the other copy of it
            for i in range(2):
                
                if len(str(response[i])) == 2:
                    space = ' '
                elif len(str(response[i])) == 1:
                    space = '  '    
                    
                num_block = str(response[i]) + space
                letter_block = num_letter[response[i]] + '  '
                
                #swaps numbers with their matching letters 
                num_board = num_board.replace(num_block, letter_block, 1)        
            
            print 100*'\n'
            print num_board
            time.sleep(2) #pauses the program for two seconds to show board
            
            num_board = old #goes back to unedited board if letters don't match
            
        guesses += 1 #increments the guesses by 1 every time the user guesses
        
        if CARD_NUMS == LETTERS: #when all letters are guessed
            game_on = 0  #end game   
            print 100*'\n'
            print num_board #letter board
    return guesses


def end_game_statistics():
    """
    Times the user and prints num of guesses and time taken to finish the
    game, along with a congratulatory phrase. 
    """
    
    start_time = time.time()
    guesses = game() #gets num of guesses from game() function
         
    end_time = time.time()
    total_time = end_time - start_time        
        
    print "You win! Congratulations buddy!"
    print "It took you: " + str(total_time) + " seconds and " + "\n" +\
          str(guesses) + " guesses"
    
 
#Runs program if run, and print a statement if imported    
if __name__ == "__main__":
    end_game_statistics()    
else:
    print "You are importing me, I can't work."