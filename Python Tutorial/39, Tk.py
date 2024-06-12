#Grafical User Interface = GUI
#Tkinter GUI

#from tkinter import *

#widgets = GUI elements: buttons, textboxes, label, images
#windows = serves as a container to hold or contain these widgets

#window = Tk() #instantiate an instance of a window
#window.geometry("420x420") #change size of window
#window.title("Jslash blunt") #change title

#icon = PhotoImage(file="C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Toji_Fushiguro.png")
#window.iconphoto(True, icon) #change icon image
#window.config(background='#601aa9')#change background color

#window.mainloop() #place window on computer screen 
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#label = an area widget that holds text and/or an image within a window

#from tkinter import *
#from PIL import Image, ImageTk  # Import necessary classes from Pillow

#window = Tk()

# Load the image with Pillow
#image = Image.open('C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\developer.png')
#photo = ImageTk.PhotoImage(image)  # Convert the image for use by Tkinter

#window.title('Label')
#label = Label(window,
#              text='Do you enjoy coding?',
#              font=('Arial', 40, 'bold'),
#              fg='#00FF00', bg='black',
#              relief=RAISED, bd=10,   #create boader
#              padx=20, pady=20,       #create space between text and label
#              image=photo,
#              compound='bottom')  # Option to position text and image relative to each other

#label.pack()  # put label into window
#label.place(x=0,y=0)  # place label to specified coordination

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#button = you click it, then it does stuff

#from tkinter import *

#count = 0

def click():
    global count
    count += 1
    print('You clicked the button!!!')
    print(count)

#window = Tk()

#photo = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\follow_button.png')

#button = Button(window,
#                text='Click me!',
#                command=click,    #without ()
#                font=('Comic Sans',30),
#                fg='#00D1FF',
#                bg='black',
#                activeforeground='#00D1FF',
#                activebackground='black',
#                state=ACTIVE,   #Can choose the button get active or disabled
#                image=photo3,
#                compound='bottom')     
#button.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#entry widget = textbox that accepts a single line of user input

#from tkinter import *

#def submit():
#    username = entry.get()
#    print('Hello '+username)
#    entry.config(state=DISABLED)

#def delete():
#    entry.delete(0,END)

#def backspace():
#    entry.delete(len(entry.get())-1,END)

#window = Tk()

#entry = Entry(window,
#              font=('Arial',50),
#              fg='yellow',
#              bg='black')
              
#entry.insert(0,"Mr./Ms.") #insert a default text
#entry.config(show='*') #show only specified characters when you type but the original one still remain as you type
#entry.pack(side=LEFT)

#submit_button = Button(window,
#                       text='Submit',
#                       command=submit)
#submit_button.pack(side=RIGHT)

#delete_button = Button(window,
#                       text='Delete',
#                       command=delete)
#delete_button.pack(side=RIGHT)

#backspace_button = Button(window,
#                       text='Backspace',
#                       command=backspace)
#backspace_button.pack(side=RIGHT)
#window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#check button

#from tkinter import *

#def display():
#    if(x.get()):
#        print('Smash!')
#    else:
#        print('Pass:(')

#window = Tk()

#x = BooleanVar() #StringVar(), IntVar()

#toji_photo = PhotoImage(file="C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Toji_Fushiguro.png")

#Resize photo
#width, height = toji_photo.width(), toji_photo.height()
#resized_toji_photo = toji_photo.subsample(2, 2) #smaller number, the bigger

#check_button = Checkbutton(window,
#                           text='Smash or Pass',
#                           variable=x,
#                           onvalue=True,offvalue=False,
#                           command=display,
#                           font=('Arial',20),
#                           fg='#00FF00',bg='black',
#                           activeforeground='#00FF00',
#                           activebackground='black',
#                           padx=25,pady=10,
#                           image=resized_toji_photo,
#                           compound="left")
#check_button.pack()

#window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["Ramen","Udon", "Soba"]

window = Tk()

ramen_image = PhotoImage(file="C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Ramen.png" )
udon_image = PhotoImage(file="C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Udon.png" )
soba_image = PhotoImage(file="C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\Soba.png" )

width, height = ramen_image.width(), ramen_image.height()
resized_ramen_image = ramen_image.subsample(5, 5) #smaller number, the bigger

width, height = udon_image.width(), udon_image.height()
resized_udon_image = udon_image.subsample(10, 10) #smaller number, the bigger

width, height = soba_image.width(), soba_image.height()
resized_soba_image = soba_image.subsample(3, 3) #smaller number, the bigger

food_images = [resized_ramen_image,resized_udon_image,resized_soba_image]

def order():
    if(x.get() == 0):
        print('You ordered ramen')
    elif(x.get() == 1):
        print('You ordered udon')
    elif(x.get() == 2):
        print('You ordered soba')
    else:
        print('Huh?')
    

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx=25,
                              font=('Impact',50),
                              image = food_images[index], #add image to radio button
                              compound='left',
                              indicatoron=0, #eliminate circle indicators and create buttons
                              width=375, #sets width of buttons
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()




