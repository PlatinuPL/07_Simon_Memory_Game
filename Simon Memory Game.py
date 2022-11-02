import tkinter as tk
import random
from tkinter import ACTIVE, DISABLED, StringVar, NORMAL


root = tk.Tk()
root.title("Simon Memory Game")
root.iconbitmap("simon.ico")
root.geometry("400x400")
root.resizable(0,0)

# Define fonts and colors
game_font_1 = ("Arial", 12)
game_font_2 = ("Arial", 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f6f7f8"
root_color =  "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg = root_color)

# Set global variables for the game
time = 500
score = 0
game_sequence = []
player_sequence = []

# Define functions
def pick_sequence():
    while True:
        value =  random.randint(1,4)
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break
        elif value!= game_sequence[-1]:
            game_sequence.append(value)
            break

    play_sequence()
    
def play_sequence():
    change_label("Playing!")
    delay = 0
    for value in game_sequence:
        if value == 1:
            root.after(delay, lambda:animate(white_button))
        elif value ==2:
            root.after(delay, lambda:animate(magenta_button))
        elif value ==3:
            root.after(delay, lambda:animate(cyan_button))
        elif value ==4:
            root.after(delay, lambda:animate(yellow_button))

        delay += time


def animate(button):
    button.config(state= ACTIVE)
    root.after(time, lambda:button.config(state=NORMAL))


def change_label(massage):
    start_button.config(text=massage)

    if massage == "Wrong!":
        start_button.config(bg="red")
    else:
        start_button.config(bg = game_color)


def set_difficulty():
    global time
    if difficulty.get() == "Easy":
        time = 1000
    elif difficulty.get() == "Medium":
        time = 500
    else:
        time = 200

def disable():
    white_button.config(state=DISABLED)
    magenta_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)

def enable():
    white_button.config(state=NORMAL)
    magenta_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)

    pick_sequence()


def press(value):
    player_sequence.append(value) 

    if len(player_sequence) ==len(game_sequence):
        check_round()

def check_round():
    global player_sequence
    global game_sequence
    global score

    if player_sequence == game_sequence:
        change_label("Correct!")
        score += len(player_sequence) + int(1000/time)
        root.after(500, pick_sequence)
    else:
        change_label("Wrong!")
        score = 0
        disable()
        game_sequence = []

        root.after(2000, lambda:change_label("New Game"))

    player_sequence = []

    score_label.config(text = "Score: " + str(score))
    

# Define Layout

# Define frames
info_frame = tk.Frame(root, bg = root_color)
game_frame = tk.LabelFrame(root, bg = game_color)
info_frame.pack(pady = (10,20))
game_frame.pack()

# Define layout for the info frame
start_button = tk.Button(info_frame, text = "New Game", font = game_font_1, bg = game_color, command=enable)
score_label = tk.Label(info_frame, text = "Score: " + str(score), font = game_font_1, bg = root_color)
start_button.grid(row=0,column=0, padx=20, ipadx= 30)
score_label.grid(row=0,column=1)

# Define layout for the game frame
white_button = tk.Button(game_frame, bg = white, activebackground= white_light, borderwidth=3, state= DISABLED, command=lambda:press(1))
white_button.grid(row = 0, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx = 60, ipady = 50)
magenta_button = tk.Button(game_frame, bg = magenta, activebackground= magenta_light, borderwidth=3, state= DISABLED, command=lambda:press(2))
magenta_button.grid(row = 0, column= 2, columnspan= 2, padx= 10, pady= 10, ipadx = 60, ipady = 50)
cyan_button = tk.Button(game_frame, bg = cyan, activebackground= cyan_light, borderwidth=3, state= DISABLED,command=lambda:press(3))
cyan_button.grid(row = 1, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx = 60, ipady = 50)
yellow_button = tk.Button(game_frame, bg = yellow, activebackground= yellow_light, borderwidth=3, state= DISABLED, command=lambda:press(4))
yellow_button.grid(row = 1, column= 2, columnspan= 2, padx= 10, pady= 10, ipadx = 60, ipady = 50)

# Define radio buttons
difficulty = StringVar()
difficulty.set("Medium")
tk.Label(game_frame, text = "Difficulty: ", font = game_font_2, bg = game_color).grid(row = 2, column = 0)
tk.Radiobutton(game_frame, text = "Easy", variable = difficulty, value = "Easy", font = game_font_2, bg = game_color, command= set_difficulty).grid(row=2, column= 1)
tk.Radiobutton(game_frame, text = "Medium", variable = difficulty, value = "Medium", font = game_font_2, bg = game_color, command= set_difficulty).grid(row=2, column= 2)
tk.Radiobutton(game_frame, text = "Hard", variable = difficulty, value = "Hard", font = game_font_2, bg = game_color, command= set_difficulty).grid(row=2, column= 3)


# Root main loop
root.mainloop()