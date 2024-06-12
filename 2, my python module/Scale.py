#Sliding scale

from tkinter import*

def submit():
    print("The temperature is: "+ str(scale.get())+" degree Celsius")

window = Tk()

#hotImage = PhotoImage(file='photo name or location')
#hotLabel = Label(image=hotImage)
#hotLabel.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,   #orientation of scale VERTICAL or HOLIZONTAL
              font=('Consolas',20),
              tickinterval=10,   #numeric indicator on the scale
              #showvalue=0, #hide current value
              troughcolor='#69FAFF',
              fg='#FF1C00',
              bg='Black',
              )

scale.set((scale['from']-scale['to'])/2+scale['to']) #set current value of slider

scale.pack()

#coldImage = PhotoImage(file='photo name or location')
#coldLabel = Label(image=coldImage)
#coldLabel.pack()

button = Button(window,text='Submit',command=submit)
button.pack()
window.mainloop()