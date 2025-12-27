from tkinter import*

root=Tk()
root.geometry("400x400")
root.title("Main Window")

def topwin():
    top = Toplevel()
    top.geometry("300x300")
    top.title("Top Level Window")

    l2= Label(top, text="This is a Top level window")
    l2.pack()

    top.mainloop()
l=Label(root, text= "this is a root window")
btn= Button(root, text="Click here to open top level window", command=topwin)
l.pack()
btn.pack()
root.mainloop()