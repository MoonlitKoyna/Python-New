from tkinter import *
win = Tk()
win.title("Grid of Frames")

Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
Entry(win).grid(row=0, column=1, padx=10, pady=10)

Label(win, text="Password").grid(row=1, column=0, padx=10, pady=10)
Entry(win, show="*").grid(row=1, column=1, padx=10, pady=10)
Button(win, text="Register").grid(row=2, columnspan=2, pady=10)

win.mainloop()