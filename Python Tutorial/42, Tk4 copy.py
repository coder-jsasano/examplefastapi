#canvas widget = widgets that is used to draw graphs, plots, images in a window

#from tkinter import *

#window = Tk()

#canvas = Canvas(window, height=500, width=500)
#canvas.create_line(0,0,500,500, fill='Blue', width=5)
#canvas.create_line(500,0,0,500, fill='Red', width=5)

#canvas.create_rectangle(50,50,250,250, fill='purple')

#points = [250,0,500,500,0,500]
#canvas.create_polygon(points, fill='yellow', outline='black', width=5)

#canvas.create_arc(0,0,500,500, fill='green', style=PIESLICE, start=180, extent=180)

#Pokeball
#canvas.create_arc(0,0,500,500, fill='red', extent=180, width=10)
#canvas.create_arc(0,0,500,500, fill='white', start=180, extent=180, width=10)
#canvas.create_oval(190,190,310,310, fill='white', width=10)
#canvas.create_oval(220,220,280,280, fill='white', width=5)

#canvas.pack()

#window.mainloop()

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#Key event

#from tkinter import *

#def doSomething(event):
#    #print('You pressed: ' + event.keysym)
#    label.config(text=event.keysym)

#window = Tk()

#window.bind(event,function) = set a key to an event, function activates when the key pressed 
#window.bind("<Return>", doSomething)
#window.bind("<Key>", doSomething) #Entire key assigned

#label = Label(window, font=('Helbetica', 100))
#label.pack()

#window.mainloop()

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#Mouse event

#from tkinter import *

#def doSome(event):
    #print('You did a thing')
#    print('Mouse coordination ' + str(event.x) + ',' + str(event.y))

#window = Tk()

#window.bind("<Button-1>",doSome) #Left click
#window.bind("<Button-2>",doSome)  #Mouse wheel click
#window.bind("<Button-3>",doSome) #Right click
#window.bind("<ButtonRelease>",doSome) #When you release click
#window.bind("<Enter>",doSome) #When you enter the window
#window.bind("<Leave>",doSome) #When you leave the window
#window.bind("<Motion>",doSome) #When the mouse move in window

#window.mainloop()

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#Drag and Drop widgets

#from tkinter import *

#def drag_start(event):
#    widget = event.widget
#    widget.startX = event.x
#    widget.startY = event.y

#def drag_motion(event):
#    widget = event.widget
    #(top-left coner of coordinate) - (coordinate where you catch the label) +  (x coordinate where we dragged)
#    x = widget.winfo_x() - widget.startX + event.x
#    y = widget.winfo_y() - widget.startY + event.y
#    widget.place(x=x, y=y)


#window = Tk()

#label = Label(window, bg='red', width=10, height=5)
#label.place(x=0,y=0)

#label2 = Label(window, bg='blue', width=10, height=5)
#label2.place(x=100,y=100)

#label.bind("<Button-1>", drag_start)
#label.bind("<B1-Motion>", drag_motion)

#label2.bind("<Button-1>", drag_start)
#label2.bind("<B1-Motion>", drag_motion)

#window.mainloop()

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

#Move image on window

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


Toyota86 = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Toyota_86.png')
width, height = Toyota86.width(), Toyota86.height()
resized_86 = Toyota86.subsample(2, 2) #smaller number, the bigger

label = Label(window, image=resized_86)
label.place(x=0,y=0)


window.mainloop()

#------------------------------------------------------------------------------------------------------------------------

#Move image on canvas

from tkinter import *

def move_up(event):
    canvas.move(myRX8,0,-10)

def move_down(event):
    canvas.move(myRX8,0,10)

def move_left(event):
    canvas.move(myRX8,-10,0)

def move_right(event):
    canvas.move(myRX8,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

RX8 = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\RX-8.png')
width, height = RX8.width(), RX8.height()
resized_RX8 = RX8.subsample(2, 2) #smaller number, the bigger

myRX8 = canvas.create_image(0,0,image=resized_RX8, anchor=NW)

window.mainloop()