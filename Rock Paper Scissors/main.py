import tkinter as tk
import random

win = tk.Tk()
win.title("RPS")

def play(choice):
    comp = random.choice(["Rock", "Paper", "Scissors"])
    result["text"] = "You: " + choice + "\nComputer: " + comp

tk.Button(win, text="Rock", command=lambda: play("Rock")).pack()
tk.Button(win, text="Paper", command=lambda: play("Paper")).pack()
tk.Button(win, text="Scissors", command=lambda: play("Scissors")).pack()

result = tk.Label(win, text="")
result.pack()

win.mainloop()
