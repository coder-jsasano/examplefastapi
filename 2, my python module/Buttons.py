#button = you click it, then it does stuff

#from tkinter import*

#def click():
#    global count
#    print("You clicked the button!")
#    count += 1
#    print(count)

#window = Tk()

#photo = PhotoImage(file='photo name or location')

#count = 0

#button = Button(window,
#                text="click me!",
#                command=click,
#                font=("Comic Sans",30),
#                fg="#00FF00",
#                bg="Blue",
#                activeforeground="#00FF00",
#                activebackground="Blue",)
                #state=ACTIVE,
                #image=photo,
                #compound='top')

#button.pack()

#window.mainloop()

#----------------------------------------------------------------------
#Checkbutton
#from tkinter import*

#def display():
#    if(x.get()==1):
#        print("You agree!")
#    else:
#        print("You don't agree :(")

#window = Tk()

#x = IntVar() #BooleanVar(), StrVar()

#photo = PhotoImage(file='photo name or location')

#check_button = Checkbutton(window,
#                           text="I agree to something",
#                           variable=x,
#                           onvalue=1,  #True,  "Yes"
#                           offvalue=0, #False, "No"
#                           command=display,
#                           font=('Arial',20),
#                           fg='#00FF00',
#                           bg='Black',
#                           activeforeground='#00FF00',
#                           activebackground='Black',
#                           padx=25,
#                           pady=10
                           #image=photo,
                           #compound='left'
#                           )

#check_button.pack()
#window.mainloop()

#----------------------------------------------------------------------------------------------------
#radio_button = similar to checkbox, but you can only select only select one from a group
from tkinter import*

food = ["Ramen","Sushi","Hamburger"]

def order():
    if(x.get()==0):
        print("You ordered Ramen!")
    elif(x.get()==1):
        print("You ordered Sushi!")
    elif(x.get()==2):
        print("You ordered Hamburger!")
    else:
        print("huh?")

window = Tk()

#RamenImage = PhotoImage(file=('photo location or name'))
#SushiImage = PhotoImage(file=('photo location or name'))
#HamburgerImage = PhotoImage(file=('photo location or name'))
#foodImages = [RamenImage,SushiImage,HamburgerImage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x,       #groups radiobuttons together if they share the same variables
                              value=index,      #assigns each radiobutton a different value
                              padx=25,
                              font=('Impact',50),
                              #image=foodImages[index],  #adds image to radio button
                              #compound='left'
                              indicatoron=0, #eliminate circle indicators
                              width=375,
                              command=order  #set command of radiobutton to function
                              )      
    
    
    radiobutton.pack(anchor=W)

window.mainloop()

