# rock paper scissors game
# create a list
# let the computer randomly choose one of it
# take user input
# compute the two and display the results

import random

print("WELCOME TO PY ROCK PAPER SCISSORS")
l = ['rock', 'paper', 'scissors']

# since you cant directly randomise the list, take the lenght of it and then  randomise to generate a random element

comp_choice = random.choice(l)

# taking user input
choice = input("enter rock, paper or  scissors ")

if choice == 'rock' and comp_choice == 'rock':
    print("draw.")
elif choice == 'rock' and comp_choice == 'paper':
    print("you lost.")
elif choice == 'rock' and comp_choice == 'scissors':
    print("yay! you won")

elif choice == 'paper' and comp_choice == 'paper':
    print("Draw.")
elif choice == 'paper' and comp_choice == 'scisssors':
    print("you lost.")
elif choice == 'paper' and comp_choice == 'rock':
    print("Yay! you won")

elif choice == 'scissors' and comp_choice == 'scissors':
    print("draw.")
elif choice == 'scissors' and comp_choice == 'rock':
    print("you lost.")
elif choice == 'scissors' and comp_choice == 'paper':
    print("yay! you won")
