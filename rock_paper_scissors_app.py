import random
from tkinter import *


# Declaring the result of the game
def winner(player_sing):

    # Setting player moves
    global player_move
    if player_sing == "✊":
        player_move = rock
    elif player_sing == "✋":
        player_move = paper
    elif player_sing == "✌":
        player_move = scissors

    # Setting computer moves
    computer_random_number = random.randint(1, 3)
    computer_move = ""

    global computer_sign
    if computer_random_number == 1:
        computer_move = rock
        computer_sign = "rock (✊)"
    elif computer_random_number == 3:
        computer_move = paper
        computer_sign = "paper (✋)"
    elif computer_random_number == 2:
        computer_move = scissors
        computer_sign = "scissors (✌)"

    # Setting result of the game
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        label.config(text=f"The computer chose {computer_sign}."
                          f"\nCongrats!"
                          f"\nYou win!")

    elif player_move == computer_move:
        label.config(text=f"The computer chose {computer_sign}."
                          f"\nDraw! There is no winner!")

    else:
        label.config(text=f"The computer chose {computer_sign}."
                          f"\nOh no, you lose!"
                          f"\nTry again!")


# Creating the app window
app = Tk()
app.title("The Rock-Paper-Scissors Game")

label = Label(app, text="Choose: Rock (✊), Paper (✋), Scissors (✌)", font=("Arial", 20, "bold"), pady=20)
label.grid(columnspan=4, row=0, column=0, sticky='NSEW')

# Setting window measures
app.geometry("750x580")

# Specifying grid
Grid.rowconfigure(app, 1, weight=1)
Grid.columnconfigure(app, 1, weight=1)
Grid.rowconfigure(app, 2, weight=1)
Grid.columnconfigure(app, 2, weight=1)
Grid.rowconfigure(app, 3, weight=1)
Grid.columnconfigure(app, 3, weight=1)

# Setting the font and size of the buttons
Font_signs = ("Courier New", 100, "bold")

# Setting the buttons
rock = Button(app, text="✊", activebackground='blue',
              command=lambda: winner("✊"), height=18, width=15)
rock.grid(rowspan=3, row=1, column=1, sticky="NSEW")
rock.configure(font=Font_signs)

paper = Button(app, text="✋", activebackground='blue',
               command=lambda: winner("✋"), height=18, width=15)
paper.grid(rowspan=3, row=1, column=2, sticky="NSEW")
paper.configure(font=Font_signs)

scissors = Button(app, text="✌", activebackground='blue',
                  command=lambda: winner("✌"), height=18, width=15)
scissors.grid(rowspan=3, row=1, column=3, sticky="NSEW")
scissors.configure(font=Font_signs)

app.mainloop()
