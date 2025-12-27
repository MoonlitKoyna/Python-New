from tkinter import*
from PIL import Image, ImageTk

root=Tk()
root.title("Image Example")
root.geometry("400x400")

upload=Image.open("catimg.jpg")
image=ImageTk.PhotoImage(upload)

label= Label(root, image=image, height=300, width=300)
label.place(x=50, y=50)
label2= Label(root, text= "This is how we add image in Tkinter window")
label2.place(x=80, y=10)

root.mainloop()