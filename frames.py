from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World")
root.iconbitmap("icon.ico")

frame = LabelFrame(root, text="This is my Frame ...", padx=5, pady=5)
frame.pack()

root.mainloop()