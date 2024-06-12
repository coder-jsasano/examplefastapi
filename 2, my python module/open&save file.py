#open file = file dialog
#from tkinter import*
#from tkinter import filedialog

#def openFile():
#    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\junpe\\Python code\\Tutorials\\my python module",
#                                          title="Open file ok?",
#                                          filetypes=(("text files","*.txt"),
#                                          ("all files","*.*")))
#    #print(filepath) #show file location
#    file = open(filepath,'r')
#    print(file.read())
#    file.close()

#window = Tk()

#button = Button(text="Open",command=openFile)
#button.pack()
#window.mainloop()

#----------------------------------------------------------------------
#save files 
from tkinter import*
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\junpe\\Python code\\Tutorials\\my python module",
                                    defaultextension=".txt",
                                    filetypes=[("Text file",".txt"),
                                                ("HTML file",".html"),
                                                ("All files",".*")])
                                                 
    
    if file is None:
        return
    #filetext = str(text.get(1.0,END))
    filetext = input("Enter some shit you dumbass hahaha: ")
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()


