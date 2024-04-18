import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input("Choose: [r]ock, [p]aper, [s]cissors: ")

# Setting player moves
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

# Setting random computer move
computer_random_number = random.randint(1, 3)

computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 3:
    computer_move = paper
elif computer_random_number == 2:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

# Declaring the result of the game
if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("Congrats!")
    print("You win!")

elif player_move == computer_move:
    print("Draw! There is no winner!")

else:
    print("Oh no, you lose!")
    print("Try again!")
