#sliding scale
#from tkinter import *

#def submit():
#    print('The temperature is: '+str(scale.get())+' degree C')

#window = Tk()

#window.geometry('100x1000')

#hotImage = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\fire.png')
#width, height = hotImage.width(), hotImage.height()
#resized_hotImage = hotImage.subsample(15, 15) #smaller number, the bigger
#hotLabel = Label(image=resized_hotImage)
#hotLabel.pack()



#scale = Scale(window,
#              from_=100,to=0, #make sure to put _ after from
#              length=400,
#              orient=VERTICAL, #or Holizontal
#              font=('Consolas',20),
#              tickinterval=10, #adds numeric indicators on the scale
#              #showvalue=0, #hide current value
#              #resolution=5, #increment of slider
#              troughcolor='#69EAFF', #change the color of gauge
#              fg='#FF1C00', bg='black')
#scale.set(100) #set the default value
#scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set the default number at middle
#scale.pack()

#coldImage = PhotoImage(file='C:\\Users\\junpe\\Python code\\Tutorials\\Python Tutorial\\snowflake.png')
#width, height = coldImage.width(), coldImage.height()
#resized_coldImage = coldImage.subsample(10, 10) #smaller number, the bigger
#coldLabel = Label(image=resized_coldImage)
#coldLabel.pack()

#button = Button(window, text='Submit', command=submit)
#button.pack()
#window.mainloop()
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#listbox = a listing of selectable text items within it's own container
#from tkinter import *

#def submit():

#    food = []

#    for index in listbox.curselection():
#        food.insert(index,listbox.get(index))


#    print('You have ordered: ')
#    for index in food:
#        print(index)
    #print(listbox.get(listbox.curselection()))

#def add():
#    listbox.insert(listbox.size(), entryBox.get())
#    listbox.config(height=listbox.size())

#def delete():

#    for index in reversed(listbox.curselection()):
#        listbox.delete(index)
    #listbox.delete(listbox.curselection())
#    listbox.config(height=listbox.size())

#window = Tk()

#listbox = Listbox(window,
#                  bg='#f7ffde',
#                  font=('Arial',30),
#                  width=12,
#                  selectmode=MULTIPLE, #enable to select multiple items
#                  )
#listbox.pack()

#listbox.insert(1,'Ramen')
#listbox.insert(2,'Gyoza')
#listbox.insert(3,'Chaofan')
#listbox.insert(4,'Shrimp chili')
#listbox.insert(5,'Salad')

#listbox.config(height=listbox.size())

#entryBox = Entry(window)
#entryBox.pack()

#submit_button = Button(window,text='Submit',command=submit)
#submit_button.pack()

#add_Button = Button(window, text='Add', command=add)
#add_Button.pack()

#delete_Button = Button(window, text='Delete', command=delete)
#delete_Button.pack()

#window.mainloop()
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#message box
#from tkinter import *
#from tkinter import messagebox #import messagebox library

#def click():
    #showinfo
#    messagebox.showinfo(title='This is an info message box', message='You are a ling-ling')
    
    #show warning
#    messagebox.showwarning(title='WARNING!', message='You got a VIRUS!!!!!')

    #show error
#    messagebox.showerror(title='Error', message='Something went off')

    #ask ok or cancel
#    if messagebox.askokcancel(title='ask ok cancel', message='Are you gon fuck that bitch?'):
#        print('Bro shes trans so You gaaay!!!!')
#    else:
#        print('You a real chad')

    #ask retry or cancel
#    if messagebox.askretrycancel(title='ask retry cancel', message='You still chasing her'):
#        print('Stop simping!!!!')
#    else:
#        print('You a real chad')
    
    #ask yes or no    
 #   if messagebox.askyesno(title='ask yes or no', message='You gym?'):
 #       print('You a real chad. You gym, I gym, they gym, we gym!')
 #   else:
 #       print('You need to learn some pain...')

    #ask question
#    answer = messagebox.askquestion(title='ask question', message='Do you do calisthenics?')
#    if answer == 'yes':
#        print('Lets do some muscle up')
#    else:
#        print('Why not?:(')

    #ask yes, no or cancel
#    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you love calisthenics?',icon='warning')
#    if answer == True:
#        print('Fire')
#    elif answer == False:
#        print('You gymrat or some?')
#    else:
#        print('You have dodged the most important question')   


    


#window = Tk()

#button = Button(window, command=click, text='Click Me')
#button.pack()

#window.mainloop()
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#color chooser
#from tkinter import *
#from tkinter import colorchooser

#def click():
    #color = colorchooser.askcolor()
    #print(colorHex)
#    window.config(bg=colorchooser.askcolor()[1]) #change background color

#window = Tk()
#window.geometry('420x420')
#button = Button(text='click me', command=click)
#button.pack()
#window.mainloop()
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#text widget = functions like a text area, you can enter multiple lines of text

from  tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window,
            fg='#00FF00',
            bg = 'black',
            font=('Arial',20),
            height = 8,
            width=20,
            padx=20, pady=20)
text.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()




