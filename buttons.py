from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look!!, I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click Me", padx=50, pady = 20, command=myClick, fg='blue')
myButton.pack()

root.mainloop()
