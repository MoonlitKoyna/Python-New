import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You Win"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Win"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You Win"
    else:
        result = "Computer Wins"