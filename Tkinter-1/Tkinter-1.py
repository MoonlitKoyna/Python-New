from tkinter import *

window = Tk()
window.title("Sample Tkinter Window")
window.geometry("300x200")

greeting = Label(text= "Hello! Welcome to Tkinter.", fg="blue", bg="yellow")
button= Button(text= "Click Me!", bg= "green", fg="white")
entry= Entry(fg="black", bg="lightgrey")
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master= window, relief= RAISED, borderwidth= 2)
frame.pack()
label= Label(master= frame, text= "Sample Frame")
label.pack()

textbox= Text(fg= "black", bg= "white")
textbox.pack()

window.mainloop()