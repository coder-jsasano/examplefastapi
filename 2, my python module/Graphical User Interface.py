#Graphical User Interface(GUI)

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = servec as a container to hold or contain these widgets

from tkinter import *

#window = Tk() #instantiate an instance of a window
#window.geometry("420x420") #In this case, you can't use * instead x
#window.title("Jquan's first lame-ass program")

#icon = PhotoImage(file='April_logo.png')
#window.iconphoto(True,icon)
#window.config(background="Yellow") #If you want some specific color, you need to put a hex value

#window.mainloop() #place window on computer screen, listen for events

#------------------------------------------------------------------------------------------------------------------
#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file='image name or location')


label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='Blue',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              compound='bottom')


label.pack()
#label.place(x=0,y=0)

window.mainloop()