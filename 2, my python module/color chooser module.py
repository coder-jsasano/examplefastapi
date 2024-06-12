#color_chooser

from tkinter import*
from tkinter import colorchooser #required

def click():
    #color = colorchooser.askcolor()
    #window.config(bg=color[1])#change background color
    window.config(bg=colorchooser.askcolor()[1])#change background color

window = Tk()
window.geometry("420x420")
button = Button(text="Click mf",command=click)
button.pack()

window.mainloop()

