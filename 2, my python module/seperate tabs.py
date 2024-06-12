#separate_tabs
from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that mannages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab1
tab2 = Frame(notebook) #new frame for tab2

notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack(expand=True,fill="both") #expand = expand to fill any space not otherwise used
                                       #fill= fill space on x and y axis
Label(tab1,text="Hello, this is tab1",width=50,height=25).pack()
Label(tab2,text="Seeya, this is tab2",width=50,height=25).pack()


window.mainloop()