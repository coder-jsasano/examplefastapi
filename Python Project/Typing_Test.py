#typing test
import curses
from curses import wrapper #allows you to write on the screen
import time
import random

def start_screen(stdscr):
    stdscr.clear() #clear the entire screen
    stdscr.addstr('Welcome to the Speed Typing Test!') #Print(row, column, str, curses.init_pair)
    stdscr.addstr('\nPress any key to begin!')
    stdscr.refresh()
    stdscr.getkey() #Wait for the user to type something without this the screen immediately disappear

#Overlaying text
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target) #Print(row, column, str, curses.init_pair)
    stdscr.addstr(1,0,f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text():
    with open("C:\\Users\\junpe\\Python code\\Tutorials\\Python Project\\typingtext.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True) #Even if the user dont hit keys, wpm calculation activates

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5)

        stdscr.clear() #clear the entire screen except for what the user write
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        #Assign escape key ASCII to break the loop
        if ord(key) == 27: 
            break
        #Activate backspace key
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)



        

def main(stdscr): #stdscr = standard screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) #(reference num, foreground, background)make sure to make it inside a function
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) #make sure to make it inside a function
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, 'You completed the text! Press any key to continue or esc to quit...')
        key = stdscr.getkey()
        if ord(key) == 27:
            break
       

wrapper(main)


