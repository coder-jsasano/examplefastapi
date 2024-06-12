#listbox = A listing of selectable text items within it's own container

def submit():
    
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You've ordered: ")
    for index in food:
        print(index)
    #print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


from tkinter import*

window = Tk()

listbox = Listbox(window,
                  bg='#F7FFDE',
                  font=('Constantia',40),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"Ramen")
listbox.insert(2,"Sushi")
listbox.insert(3,"Tonkatsu")
listbox.insert(4,"Rice")
listbox.insert(5,"Tempura")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

addButton = Button(window,text="Add",command=add)
addButton.pack()

deleteButton = Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()
