from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg = 'blue', fg = 'white', borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name:  ")


def myClick():
    hello = "Hello  " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()

myButton = Button(root, text="Please Enter Your Name", padx=50, pady = 20, command=myClick, fg='blue')
myButton.pack()

root.mainloop()
