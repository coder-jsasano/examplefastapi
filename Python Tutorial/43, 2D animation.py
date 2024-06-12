#2D animation
#from tkinter import *
#import time

#Constant variable = All uppercase and reuseable
#WIDTH = 500
#HEIGHT = 500
#xVelocity = 3
#yVelocity = 2

#window = Tk()

#canvas = Canvas(window,width=WIDTH,height=HEIGHT)
#canvas.pack()

#Gojo_image = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Gojo.png')
#width, height = purple_energey_image.width(), purple_energey_image.height()
#resized_purple_energey_image = purple_energey_image.subsample(3, 3) #smaller number, the bigger
#Gojo = canvas.create_image(0,0,image=Gojo_image,anchor=NW)

#purple_energey_image = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\purple.png')
#width, height = purple_energey_image.width(), purple_energey_image.height()
#resized_purple_energey_image = purple_energey_image.subsample(3, 3) #smaller number, the bigger
#purple_energey = canvas.create_image(0,0,image=resized_purple_energey_image,anchor=NW)


#image_width = resized_purple_energey_image.width()
#image_height = resized_purple_energey_image.height()

#while True:
#    coordinates = canvas.coords(purple_energey)
#    print(coordinates)
#    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
#        xVelocity = -xVelocity
#    if(coordinates[1]>=(WIDTH-image_height) or coordinates[1]<0):
#        yVelocity = -yVelocity
#    canvas.move(purple_energey,xVelocity,yVelocity)
#    window.update()
#    time.sleep(0.01)    

#window.mainloop()

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#Multiple objects animation

from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,'yellow')
tennis_ball = Ball(canvas,0,0,30,4,3,'green')
basket_ball = Ball(canvas,0,0,120,8,7,'orange')
base_ball = Ball(canvas,0,0,30,2,3,'white')


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    base_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
