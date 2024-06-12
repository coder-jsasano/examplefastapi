#Tic-Tac-Toe
from tkinter import *
import random

def button_click(row, column):
    global player
    buttons[row][column].config(text=player)
    next_turn(row, column)
    player = "o" if player == "x" else "x"
    label.config(text=player + " turn")
    print("Button clicked")

def next_turn(row, column):
    global player
    print("Next turn called")
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins!"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+" wins!"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():
    # Check rows for a win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
        
    # Check columns for a win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
        
    # Check diagonals for a win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    
    # Check for a tie
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return False
    return True  # If no empty spaces left and no winner, it's a tie




def empty_spaces():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
        
        if spaces == 0:
            return False
        else:
            return True
        


def new_game():
    
    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#F0F0F0')


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()



for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas',40), width=5, height=2,
                                      command=lambda row=row, column=column:  button_click(row, column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()