# implementation of card game - Memory

import simplegui
import random

WIDTH = 800
HEIGHT = 100
CARDWIDTH = 50
NUMBERS = 8
NUMBER_SIZE = 20

cardlist = []
cardpos = []
exposed = []


# helper function to initialize globals
def create_list_of_random_numbers(numbers):
    numberlist = range(numbers)
    random.shuffle(numberlist)
    
    print "Number list is:",numberlist
    return numberlist


def new_game():
    global cardlist, cardpos, exposed, CLICKS, TURNS
    
    CLICKS = 0
    TURNS = 0
    label.set_text("Turns = " + str(TURNS))
    
    # Concatenate the two separate random number lists of range 8 to make it 16 numbers
    cardlist =  create_list_of_random_numbers(NUMBERS) + create_list_of_random_numbers(NUMBERS)
    random.shuffle(cardlist)  #Shuffles the 16 numbers inside the list
    print "Shuffled Cardlist is:", cardlist
    
    # Center the Card number position in the CARDWIDTH size 
    cardpos=[(CARDWIDTH/2)*(2*index+1) for index in range(len(cardlist))]
    exposed=["F" for index in range(len(cardlist))]
    
    print "Card number positions are:", cardpos,
    #print cardpos[1]
    #print "\n"
   
     
# define event handlers
def mouseclick(pos):
   global click_pos, CLICKS, TURNS, card, card1, card2
    
   click_pos = list(pos)
    
    # add game state logic here
   card = click_pos[0]/CARDWIDTH
   
   if( exposed[card] == "F" ):
        exposed[card] = "T"
        if CLICKS == 0:
            card1 = card
            CLICKS = 1
            #print "Card1 index", card1
        elif CLICKS == 1:
            card2 = card
            #print "Card2 index", card2
            CLICKS = 2	
            TURNS += 1
        else:
            #print "Card3 index", card
            CLICKS = 3
 
        
   #print "Exposed list", exposed
   print "\nClicks is", CLICKS
   label.set_text("Turns = " + str(TURNS)) 
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CLICKS, card1
    
    for index in range(NUMBERS*2):
        if( exposed[index] == "F" ):
            #canvas.draw_polyline([(0, 0), (25, 0), (25, HEIGHT)],CARDWIDTH, 'GREEN')
            #canvas.draw_polyline([(50, 0), (75, 0), (75, HEIGHT)],CARDWIDTH, 'GREEN')
            canvas.draw_polyline([((CARDWIDTH/2)*(2*index+1)-CARDWIDTH/2, 0), ((CARDWIDTH/2)*(2*index+1), 0), ((CARDWIDTH/2)*(2*index+1), HEIGHT)],CARDWIDTH, 'GREEN')
        elif( exposed[index] == "T" ):   
            canvas.draw_text(str(cardlist[index]), [cardpos[index],HEIGHT/2], NUMBER_SIZE, "White")
            
            if( CLICKS == 3 ):
                if( cardlist[card2] != cardlist[card1] ):   # because comparison is at the 3rd open card
                    exposed[card2] = exposed[card1] = "F" 
                    print "NOW CLICKS is", CLICKS 
                    
                print "NOW Card1, Card2, Card3 indexes are:", card1, card2, card
                CLICKS = 1       # Its 3 clicks so reset back to 1 click for 1 Open card
                card1 = card   
                print "..AFTER Reset to 1 click, Card1, Card2, Card3 indexes are:", card1, card2, card
                   
        canvas.draw_line((CARDWIDTH*(index+1), 0), (CARDWIDTH*(index+1), HEIGHT), 1, 'WHITE')

        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
