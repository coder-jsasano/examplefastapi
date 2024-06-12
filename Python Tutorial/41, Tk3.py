#file reading on tk
#from tkinter import *
#from tkinter import filedialog

#def openFile():
#    filepath = filedialog.askopenfilename(title='Open file',
#                                          filetype=(("text files","*.txt"),
#                                          ("all files","*.*")))
    #print(filepath) = show the directory of a selected file
#    file = open(filepath, 'r')
#    print(file.read())
#    file.close()


#window = Tk()

#button = Button(text='Open', command=openFile)
#button.pack()

#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#save file on tk

#from tkinter import *
#from tkinter import filedialog

#def saveFile():
#    file = filedialog.asksaveasfile(
#                                    defaultextension='.txt',
#                                    filetypes=[("Text file",".txt"),
#                                               ("HTML file",".html"),
#                                               ("All file",".*")]
#                                               )
    #Enable to save empty files
#    if file is None:
#        return
    
#    filetext = str(text.get(1.0,END)) #Write in a text area
    #filetext = input("Enter some text: ") #Write in a console window
#    file.write(filetext)
#    file.close()

#window = Tk()

#button = Button(text='Save', command=saveFile)
#button.pack()

#text = Text(window)
#text.pack()

#window.mainloop()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# Menu bar

#from tkinter import *

#def openFile():
#    print('File has been opended!')

#def saveFile():
#    print('File has been saved!')

#def cut():
#    print('You cut!')

#def copy():
#    print('You copied!')

#def paste():
#    print('You pasted!')


#window = Tk()

#menubar = Menu(window)
#window.config(menu=menubar)

#fileMenu = Menu(menubar, tearoff=0, font=('MV Boli',10))
#menubar.add_cascade(label='File', menu=fileMenu)
#fileMenu.add_command(label="Open", command=openFile)
#fileMenu.add_command(label="Save", command=saveFile)
#fileMenu.add_separator()
#fileMenu.add_command(label="Exit", command=quit)

#editMenu = Menu(menubar, tearoff=0)
#menubar.add_cascade(label='Edit', menu=editMenu)
#editMenu.add_command(label="Cut", command=cut)
#editMenu.add_command(label="Copy", command=copy)
#editMenu.add_command(label="Paste", command=paste)


#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#frames = a rectangular container to group and hold widgets

#from tkinter import *

#window = Tk()

#frame = Frame(window, bg='pink', bd=5, relief=RAISED)
#frame.pack()
#frame.place(x=0,y=0)

#Button(frame, text='W',font=('Consolas',25), width=3).pack(side=TOP)
#Button(frame, text='A',font=('Consolas',25), width=3).pack(side=LEFT)
#Button(frame, text='S',font=('Consolas',25), width=3).pack(side=LEFT)
#Button(frame, text='D',font=('Consolas',25), width=3).pack(side=LEFT)

#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#create new window on tk

#from tkinter import *

#def create_window():
    #new_window = Toplevel() # new window on top of other windows, linked to a bottom window
#    new_window = Tk() # new independent window 

    #window.destroy() #close out of a previous window

#window = Tk()

#Button(window, text='Create New Window', command=create_window).pack()

#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#separate tabs = notebook widgets

#from tkinter import *
#from tkinter import ttk

#window =Tk()

#notebook = ttk.Notebook(window) #widget the manages a collection of windows/displays

#tab1 = Frame(notebook) #new frame for tab1
#tab2 = Frame(notebook) #new frame for tab2

#notebook.add(tab1, text='Tab 1')
#notebook.add(tab2, text='Tab 2')
#notebook.pack(expand=True,  #expand = expand to fill any space not otherwise used
#               fill='both') #fill = fill space on both x and y axis

#Label(tab1, text='Hello, this is tab #1', width=50, height=25).pack()
#Label(tab2, text='Bye', width=50, height=25).pack()


#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#grid() = geometry manager that organizes widgets in a table-like structure in a parenthesis

#from tkinter import *

#window = Tk()

#titleLabel = Label(window, text='Enter your info', font=('Arial',25)).grid(row=0, column=0, columnspan=2)

#firstNameLabel = Label(window, text='First name: ', width=20).grid(row=1,column=0)
#firstNameEntry = Entry(window).grid(row=1,column=1)

#lastNameLabel = Label(window, text='Last name: ').grid(row=2,column=0)
#lastNameEntry = Entry(window).grid(row=2,column=1)

#emailLabel = Label(window, text='Email: ').grid(row=3,column=0)
#emailEntry = Entry(window).grid(row=3,column=1)

#submit_button = Button(window, text='Submit').grid(row=4, column=0, columnspan=2)

#window.mainloop()

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#Progress bar

from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while (x<tasks):
        time.sleep(1)
        bar['value'] += 10
        download += 1
        percent.set(str(int((x/tasks)*100))+'%')
        text.set(str(x)+'/'+str(tasks)+' tasks completed')
        window.update_idletasks()

def start2():
    GB = 100
    download = 0
    speed = 1
    while (download<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100 
        download += speed
        percent.set(str(int((download/GB)*100))+'%')
        text.set(str(download)+'/'+str(GB)+' GB completed')
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

download_button = Button(window, text='Download', command=start2).pack()


window.mainloop()




