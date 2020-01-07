'''
# Program 1
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Working with Radio Buttons")
root.iconbitmap("icon.ico")

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


myLabel = Label(root, text=r.get())
myLabel.pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop()

'''
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Working with Radio Buttons")
root.iconbitmap("icon.ico")

Toppings = [("Pepperoni", "Pepperoni"),
         ("Cheese", "Cheese"),
         ("Mushroom", "Mushroom"),
         ("Onion", "Onion")
         ]
pizz = StringVar()
pizz.set("Pepperoni")

for text,topping in Toppings:
    Radiobutton(root, text=text, variable=pizz, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizz.get()))
myButton.pack()

root.mainloop()

