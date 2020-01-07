from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Working With Frames")
root.iconbitmap("icon.ico")

#frame = LabelFrame(root, text="This is my Frame ...", padx=50, pady=50)
frame = LabelFrame(root, text="", padx=50, pady=50)
frame.pack(padx=55, pady=55)

b = Button(frame, text="Don't Click Here!")
b.grid(row=0, column=0)
b2 = Button(frame, text=" Or Here!")
b2.grid(row=1, column=1)
root.mainloop()