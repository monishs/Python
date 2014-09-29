# template for "Stopwatch: The Game"

import simplegui

# define global variables
Time = 0
Interval = 100
Ticks = 0
Wins = 0
Attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global Time
    
    val = str(t)
    if( int(val) >= 0 ):
        Mins = int(val[0:])/600
        Secs = (float(val[0:])/600 - Mins) * 60
        #print "Mins & Secs", Mins, Secs
    if ( len(str(Secs)) == 3):    ## eg: 0.1
        Secs = "0" + str(Secs)
        #print Secs
    else:                         ## eg: 59.9
        Secs = str(Secs)    
        #print Secs
    Time = str(Mins) + ":" + Secs
    return Time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
     timer.start()

def stop():
      global Time, Wins, Attempts
      
      if( timer.is_running() ):
            timer.stop()  
            
            if( Time[4:6] == ".0" ):
                Wins = Wins + 1
                Attempts = Attempts + 1
            
            else:
                Attempts = Attempts + 1
    
      score_handler()      
            
def reset():
     global Ticks, Wins, Attempts
     Ticks = 0
     Wins = 0
     Attempts = 0
     
     timer.stop()
      
        
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global Ticks
    Ticks = Ticks + 1
    
# define Score handler 
def score_handler():
    DisplayScore = str(Wins) + "/" + str(Attempts)
    return DisplayScore

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(Ticks), [50,100], 36, "White")
    canvas.draw_text(score_handler(), [140,20], 25, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 200, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(Interval, timer_handler)


# start frame
frame.start()
