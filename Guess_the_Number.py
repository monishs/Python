# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
Range = 100
Guess_Number = 7
Rand_Number = 0

# helper function to start and restart the game
def new_game():
    global Range
    global Guess_Number 
    
    if (Range == 1000):
        Guess_Number = 10
        
    else:
        Guess_Number = 7

    print "New Game. Range is from 0 to", Range
    print "Number of remaining guesses:", Guess_Number
    
    global Rand_Number
    Rand_Number = random.randrange(0, Range, )
    #print "Random Number is", Rand_Number
    print " "
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global Range
    Range = 100
      
    new_game()
   
def range1000():
    # button that changes range to range [0,1000) and restarts
    global Range
    Range = 1000
 
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global Rand_Number
    #print "Rand_Number", Rand_Number
    #print " "
    
    print "Guess was", guess
    global Guess_Number
    
    if ( (int(guess) > int(Rand_Number)) and Guess_Number > 0 ):
      Guess_Number = Guess_Number - 1
      print "You have", Guess_Number ,"guesses left" 
      print "Lower!\n"
        
    elif ( int(guess) < int(Rand_Number) ):
      Guess_Number = Guess_Number - 1
      print "You have", Guess_Number ,"guesses left"  
      print "Higher!\n"
    
    else:
        Guess_Number = Guess_Number - 1
        print "Correct! And you had", Guess_Number, "guesses left.\n"
        new_game()
        
    if (Guess_Number <= 0):
        print "Sorry! You ran out of guesses. The number was", Rand_Number 
        print "\n\n"
        new_game()
        
# create frame
frame = simplegui.create_frame("GTN", 200, 200)

# register event handlers for control elements
frame.add_button('Range [1,100)', range100, 200)
frame.add_button('Range [1,1000)', range1000, 200)

frame.add_input('Guess the number', input_guess, 200)


# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
