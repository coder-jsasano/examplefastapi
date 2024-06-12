#message_box 

from tkinter import*
from tkinter import messagebox #import message box library

def click():
    #messagebox.showinfo(title="This is an info message box mf",message="You are a bitch-ass cunt")
    #messagebox.showwarning(title="WARNING!",message="Too hot to handle!")
    #messagebox.showerror(title="Error",message="Something went wrong:(")
    
    #if messagebox.askokcancel(title="ask ok to cancel",message="Do you wanna do it?"):
    #    print("You did it!")
    #else:
    #    print("You canceled it!")

    #if messagebox.askretrycancel(title="ask ok to cancel",message="Do you wanna retry it?"):
    #    print("You retried it!")
    #else:
    #    print("You canceled it!")
    
    #if messagebox.askyesno(title="ask yes or no",message="Do you fuck with him?"):
    #    print("I fuck with him too")
    #else:
    #    print("Me neither")

    #answer = messagebox.askquestion(title="ask question",message="Ever been to Japan?")
    #if(answer == 'yes'):
    #    print("I have")
    #else:
    #    print("Never")

    answer = (messagebox.askyesnocancel(title="ask yes no cancel",message="Do you like IshowSpeed?",icon='info'))
    if(answer == True):
        print("Yessir!!")
    elif(answer == False):
        print("You ass")
    else:
        print("Don't run away from my question")

    



window = Tk()

button = Button(window,command=click,text='Click me')
button.pack()

window.mainloop()