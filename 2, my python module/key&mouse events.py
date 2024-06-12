#key_event

#from tkinter import *

#def doSome(event):
#    print("You pressed: "+ event.keysym)
#    label.config(text=event.keysym)


#window = Tk()

#window.bind("<Key>"#"<Return>" #"<q>"
#            ,doSome)

#label = Label(window,font=('Helvetica',50))
#label.pack()

#window.mainloop()

#-------------------------------------------------------------------------------------------------
#mouse_event
from tkinter import *

def doSome(event):
    print("Mouse coordinates" + str(event.x)+","+str(event.y))

window = Tk()

#window.bind("<Button-1>",doSome) #left mouse click
#window.bind("<Button-2>",doSome)  #scroll wheel
#window.bind("<Button-3>",doSome)  #right mouse click
#window.bind("<ButtonRelease>",doSome) 
#window.bind("<Enter>",doSome) #enter the window
#window.bind("<Leave>",doSome) #leave the window
#window.bind("<Motion>",doSome) #where the mouse moved

window.mainloop()

