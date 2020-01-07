from tkinter import *
from PIL import ImageTk, Image

from tkinter import messagebox

root = Tk()
root.title("Working with Message Box")
root.iconbitmap("icon.ico")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():

    messagebox.askquestion("This is a Popup", "Hellow World, I a popped up")
    response = messagebox.askyesno("This is a Popup", "Hellow World, I a popped up")
    Label(root, text=response).pack()
    if response== 1:
        Label(root, text="You Clicked Yes").pack()
    else:
        Label(root, text="You Clicked No").pack()



Button(root, text="Popup", padx=10, pady=10, borderwidth=2, command=popup).pack()


root.mainloop()