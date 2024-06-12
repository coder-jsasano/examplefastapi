#move widgets in window

#from tkinter import *

#def move_up(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

#def move_down(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

#def move_left(event):
#    label.place(x=label.winfo_x()-10, y=label.winfo_y())

#def move_right(event):
#    label.place(x=label.winfo_x()+10, y=label.winfo_y())


#window = Tk()
#window.geometry("500x500")

#window.bind("<w>",move_up)
#window.bind("<s>",move_down)
#window.bind("<a>",move_left)
#window.bind("<d>",move_right)
#window.bind("<Up>",move_up)
#window.bind("<Down>",move_down)
#window.bind("<Left>",move_left)
#window.bind("<Right>",move_right)

#myimage = PhotoImage(file='photo name or location')
#label = Label(window,image=myimage)

#window.mainloop()

#----------------------------------------------------------------------------------------------------------

#from tkinter import *

#def move_up(event):
#    canvas.move(myimage,0,-10)

#def move_down(event):
#    canvas.move(myimage,0,10)

#def move_left(event):
#    canvas.move(myimage,-10,0)

#def move_right(event):
#    canvas.move(myimage,10,0)


#window = Tk()

#window.bind("<w>",move_up)
#window.bind("<s>",move_down)
#window.bind("<a>",move_left)
#window.bind("<d>",move_right)
#window.bind("<Up>",move_up)
#window.bind("<Down>",move_down)
#window.bind("<Left>",move_left)
#window.bind("<Right>",move_right)

#canvas = Canvas(window,width=500,height=500)
#canvas.pack()

#photoimage = PhotoImage(file='photo name or location')
#myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

#window.mainloop()

#-----------------------------------------------------------------------------------------------------
#2D Animation
#from tkinter import *
#import time

#WIDTH = 500
#HEIGHT = 500
#xVelocity = 3
#yVelocity = 2

#window = Tk()

#canvas = Canvas(window,width=WIDTH,height=HEIGHT)
#canvas.pack()

#background_photo = PhotoImage(file='photo name or location')
#background = canvas.create_image(0,0,image=background_photo,anchor=NW)

#photo_image = PhotoImage(file='photo name or location')
#my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)



#image_width = photo_image.width()
#image_height = photo_image.height()

#while True:
#    coordinates = canvas.coords(my_image)
#    print(coordinates)
#    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#        xVelocity = -xVelocity
#    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
#        yVelocity = -yVelocity
#    canvas.move(my_image,xVelocity,yVelocity)
#    window.update()
#    time.sleep(0.01)
    
#window.mainloop()

#--------------------------------------------------------------------------------------------------------------
#Animate multiple objects
from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"Yellow")
tennis_ball = Ball(canvas,0,0,30,4,3,"Light Green")
basket_ball = Ball(canvas,0,0,125,8,7,"Orange")


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)
    
window.mainloop()

